#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "playwright>=1.40.0",
#     "pyyaml>=6.0.1",
#     "python-slugify>=8.0.1",
#     "llm>=0.12.0"
# ]
# ///

import urllib.parse
from playwright.sync_api import sync_playwright
import yaml
from datetime import datetime, timedelta
import os
import re
import sys
from pathlib import Path
from slugify import slugify
import llm
import json
from typing import Tuple, List, Optional

def clean_url(url):
    """Clean URL by removing query parameters and fragments."""
    parsed = urllib.parse.urlparse(url)
    return urllib.parse.urlunparse((parsed.scheme, parsed.netloc, parsed.path, '', '', ''))

def extract_page_content(url):
    """Extract title and content from a webpage using Playwright."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.wait_for_load_state('networkidle')
        title = page.title()
        content = page.content()
        browser.close()
        return title, content

def process_content(content, model_name):
    """Process content using llm to generate summary and tags."""
    try:
        # Configure LLM with OpenAI API key
        llm_config = {}
        if api_key := os.getenv('OPENAI_API_KEY'):
            llm_config['openai_api_key'] = api_key
        else:
            raise ValueError("OPENAI_API_KEY environment variable is required")
        
        model = llm.get_model(model_name, **llm_config)
        
        # Generate summary
        summary_response = model.prompt(
            content,
            system="Summarize this content in a concise, technical style suitable for Michael Bargury's link log. Focus on key technical insights and implications. Keep it under 200 words."
        )
        summary = summary_response.text().strip()
        
        # Generate tags with structured output
        tags_response = model.prompt(
            content,
            system="Generate 3-5 relevant technical tags for this content. Return the tags as a JSON array of strings.",
            response_format={"type": "json_array"}
        )
        tags = json.loads(tags_response.text())
        
        return summary, tags
    except Exception as e:
        print(f"Error processing content: {e}", file=sys.stderr)
        return content, []

def check_existing_file(toread_dir, clean_url):
    """Check if URL already exists in recent files."""
    six_months_ago = datetime.now() - timedelta(days=180)
    
    for file in os.listdir(toread_dir):
        if not file.endswith('.md'):
            continue
        try:
            file_date = datetime.strptime(file[:10], '%Y-%m-%d')
            if file_date >= six_months_ago:
                with open(f'{toread_dir}/{file}') as f:
                    file_content = f.read()
                    front_matter = yaml.safe_load(file_content.split('---')[1])
                    if front_matter['link'] == clean_url:
                        return file
        except:
            continue
    return ''

def create_filename(title):
    """Create a filename from the title using slugify for safe filenames."""
    # Generate a slug from the title
    slug = slugify(title, lowercase=True, max_length=100)
    
    # Get today's date
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Combine date and slug
    filename = f'{today}-{slug}.md'
    
    # Ensure the filename is valid for the filesystem
    return Path(filename).name

def save_file(toread_dir, filename, title, tags, clean_url, content, model_name):
    """Save the article to a file with proper front matter."""
    # Process the content to get summary and tags
    summary, generated_tags = process_content(content, model_name)
    
    # Combine provided tags with generated tags, removing duplicates
    all_tags = list(set(tags + generated_tags))
    
    # Format tags for YAML front matter
    tags_yaml = '\n   - '.join([''] + all_tags)
    
    file_content = f'''---
title: "{title}"
tags:{tags_yaml}
link: {clean_url}
date: {datetime.now().strftime('%Y-%m-%d')}
---

{summary}
'''
    with open(f'{toread_dir}/{filename}', 'w') as f:
        f.write(file_content)

def main():
    if len(sys.argv) != 4:
        print("Usage: python process_url.py <url> <toread_dir> <model_name>")
        sys.exit(1)
    
    url = sys.argv[1]
    toread_dir = sys.argv[2]
    model_name = sys.argv[3]
    
    # Process URL
    clean_url = clean_url(url)
    title, content = extract_page_content(clean_url)
    
    # Check for existing file
    existing_file = check_existing_file(toread_dir, clean_url)
    if existing_file:
        print(f"existing_file={existing_file}")
        sys.exit(0)
    
    # Create and save new file
    filename = create_filename(title)
    save_file(toread_dir, filename, title, [], clean_url, content, model_name)
    print(f"filename={filename}")

if __name__ == '__main__':
    main() 