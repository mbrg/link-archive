#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pyyaml>=6.0.1",
#     "python-slugify>=8.0.1",
#     "python-dotenv>=1.0.0"
# ]
# ///

import yaml
import sys
import os
import json
from pathlib import Path
from datetime import datetime
from slugify import slugify
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

def read_archive_file(archive_path):
    """Read and parse an archive file."""
    with open(archive_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split frontmatter and content
    if content.startswith('---\n'):
        parts = content.split('---\n', 2)
        if len(parts) >= 3:
            frontmatter = yaml.safe_load(parts[1])
            markdown_content = parts[2].strip()
        else:
            raise ValueError("Invalid frontmatter format")
    else:
        raise ValueError("No frontmatter found")
    
    return frontmatter, markdown_content

def extract_paragraph_for_line(content_lines, line_number):
    """Extract the full paragraph containing the specified line."""
    if line_number <= 0 or line_number > len(content_lines):
        return ""
    
    target_line = content_lines[line_number - 1].strip()
    if not target_line:
        return ""
    
    # Find paragraph boundaries (empty lines)
    start = line_number - 1
    end = line_number - 1
    
    # Go backward to find paragraph start
    while start > 0 and content_lines[start - 1].strip():
        start -= 1
    
    # Go forward to find paragraph end  
    while end < len(content_lines) - 1 and content_lines[end + 1].strip():
        end += 1
    
    # Extract the paragraph
    paragraph_lines = content_lines[start:end + 1]
    return ' '.join(line.strip() for line in paragraph_lines if line.strip())

def parse_pr_comments(comments_json):
    """Parse PR review comments from GitHub API JSON."""
    try:
        comments_data = json.loads(comments_json)
        
        # Extract review comments (line-specific comments)
        review_comments = []
        if 'review_comments' in comments_data:
            for comment in comments_data['review_comments']:
                review_comments.append({
                    'line': comment.get('line'),
                    'diff_hunk': comment.get('diff_hunk', ''),
                    'body': comment['body'],
                    'author': comment['user']['login']
                })
        
        # Extract general PR comments
        pr_comments = []
        if 'comments' in comments_data:
            for comment in comments_data['comments']:
                pr_comments.append({
                    'body': comment['body'],
                    'author': comment['user']['login']
                })
        
        return review_comments, pr_comments
        
    except json.JSONDecodeError as e:
        print(f"Error parsing comments JSON: {e}", file=sys.stderr)
        return [], []

def create_weblog_entry(frontmatter, archive_content, review_comments, pr_comments, archive_filename):
    """Create weblog entry with quoted paragraphs and comments."""
    
    # Create weblog frontmatter
    weblog_frontmatter = {
        'title': frontmatter['title'],
        'date': datetime.now().strftime('%Y-%m-%d'),
        'original_link': frontmatter['link'],
        'archive_link': f"archive/{Path(archive_filename).name}",
        'tags': frontmatter.get('tags', []) + ['weblog'],
        'type': 'weblog'
    }
    
    # Start building the weblog content
    weblog_content = [f"# {frontmatter['title']}\n"]
    weblog_content.append(f"**Original:** [{frontmatter['title']}]({frontmatter['link']})")
    weblog_content.append(f"**Archive:** [Local copy]({weblog_frontmatter['archive_link']}) (in case of link rot)\n")
    
    if frontmatter.get('summary'):
        weblog_content.append(f"**Summary:** {frontmatter['summary']}\n")
    
    # Process line-specific comments with quoted paragraphs
    archive_lines = archive_content.split('\n')
    
    if review_comments:
        weblog_content.append("## Key Points & Commentary\n")
        
        for comment in review_comments:
            if comment.get('line'):
                # Extract the paragraph for this line
                paragraph = extract_paragraph_for_line(archive_lines, comment['line'])
                if paragraph:
                    weblog_content.append(f"> {paragraph}\n")
                    weblog_content.append(f"**My take:** {comment['body']}\n")
    
    # Add general comments
    if pr_comments:
        general_comments = [c for c in pr_comments 
                          if not c['body'].lower().startswith(('lgtm', 'approved', 'looks good'))]
        if general_comments:
            weblog_content.append("## Additional Thoughts\n")
            for comment in general_comments:
                weblog_content.append(f"{comment['body']}\n")
    
    return weblog_frontmatter, '\n'.join(weblog_content)

def generate_weblog_filename(title, date_str=None):
    """Generate filename for weblog entry."""
    if date_str is None:
        date_str = datetime.now().strftime('%Y-%m-%d')
    
    slug = slugify(title)
    return f"{date_str}-{slug}.md"

def create_weblog_file(frontmatter, content, output_dir="weblog"):
    """Create the weblog markdown file."""
    
    filename = generate_weblog_filename(frontmatter['title'])
    filepath = Path(output_dir) / filename
    
    # Create the final weblog content
    final_content = f"""---
{yaml.dump(frontmatter, default_flow_style=False)}---

{content}
"""
    
    # Write the file
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    return str(filepath)

def main():
    if len(sys.argv) < 3:
        print("Usage: python weblog_processor.py <archive_file> <comments_json>")
        sys.exit(1)
    
    archive_file = sys.argv[1]
    comments_json = sys.argv[2]
    
    try:
        # Read the archive file
        frontmatter, archive_content = read_archive_file(archive_file)
        
        # Parse PR comments
        review_comments, pr_comments = parse_pr_comments(comments_json)
        
        # Create weblog entry
        weblog_frontmatter, weblog_content = create_weblog_entry(
            frontmatter, archive_content, review_comments, pr_comments, archive_file
        )
        
        # Create the weblog file
        weblog_file = create_weblog_file(weblog_frontmatter, weblog_content)
        
        # Output for GitHub Actions
        print(f"weblog_file:{weblog_file}")
        print(f"title:{weblog_frontmatter['title']}")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
