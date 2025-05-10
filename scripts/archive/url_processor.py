#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "firecrawl-py>=0.1.0",
#     "pyyaml>=6.0.1",
#     "python-slugify>=8.0.1",
#     "llm>=0.12.0",
#     "python-dotenv>=1.0.0"
# ]
# ///

import urllib.parse
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
from firecrawl import FirecrawlApp
import logging
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

def clean_url_string(url):
    """Clean URL by removing query parameters and fragments."""
    parsed = urllib.parse.urlparse(url)
    return urllib.parse.urlunparse((parsed.scheme, parsed.netloc, parsed.path, '', '', ''))

def extract_page_content(url):
    """Extract title and content from a webpage using Firecrawl."""
    api_key = os.getenv('FIRECRAWL_API_KEY')
    if not api_key:
        raise ValueError("FIRECRAWL_API_KEY environment variable is required. Please set it in .env file or environment variables.")
    
    app = FirecrawlApp(api_key=api_key)
    result = app.scrape_url(url, formats=['markdown'])
    logging.debug(f"Firecrawl results:\n---{result}\n---\n")

    title = result.title if result.title else result.metadata.get("title", "")
    return title, result.markdown

def process_content(content, model_name):
    """Process content using llm to generate summary and tags."""
    # Configure LLM with OpenAI API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is required. Please set it in .env file or environment variables.")
    
    model = llm.get_model(model_name)
    model.api_key = api_key
    
    # Generate summary
    summary_response = model.prompt(
        content,
        system="Summarize this content in a concise, technical style suitable for Michael Bargury's link log (mbgsec.com). Focus on key technical insights and implications. Keep it under 100 words."
    )
    summary = clean_string(summary_response.text())
    
    # Generate tags with structured output
    tags_response = model.prompt(
        content,
        system="Generate 3-5 relevant technical tags for this content. Return the tags as a JSON array of strings.",
        schema=llm.schema_dsl("mbgsec_blog_tag", multi=True)
    )
    tags = [clean_string(tag["mbgsec_blog_tag"]) for tag in json.loads(tags_response.text())["items"]]

    # Generate title
    title_response = model.prompt(
        content,
        system="Reply with a concise one-liner title for this content. "
    )
    title = clean_string(title_response.text().strip('"'))
    
    return title, summary, tags

def clean_string(text):
    return text.strip().replace('"', '\\"').split('\n')[0]

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

def save_file(toread_dir, filename, title, tags, clean_url, content, generatedsummary, generated_tags):
    """Save the article to a file with proper front matter."""
    # Combine provided tags with generated tags, removing duplicates
    all_tags = list(set(tags + generated_tags))
    
    # Format tags for YAML front matter
    tags_yaml = '\n   - '.join([''] + all_tags)
    
    file_content = f'''---
title: "{generated_title if title == '' else title}"
tags:{tags_yaml}
link: {clean_url}
date: {datetime.now().strftime('%Y-%m-%d')}
summary: "{generated_summary}"
---

{content}
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
    clean_url = clean_url_string(url)
    title, content = extract_page_content(clean_url)
    
    # Check for existing file
    existing_file = check_existing_file(toread_dir, clean_url)
    if existing_file:
        print(f"existing_file:{existing_file}")
        print(f"title:{title}")
        sys.exit(0)
    
    # Process the content to get summary and tags
    generated_title, generated_summary, generated_tags = process_content(content, model_name)
    title_to_use = generated_title if title == '' else title
    
    # Create and save new file
    filename = create_filename(title_to_use)
    save_file(toread_dir, filename, title_to_use, [], clean_url, content, generated_summary, generated_tags)
    print(f"filename:{filename}")
    print(f"title:{title}")
    print("existing_file:")

if __name__ == '__main__':
    main() 