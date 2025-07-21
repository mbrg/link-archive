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
    """Extract the full paragraph containing the specified line, expanding until empty lines."""
    if line_number <= 0 or line_number > len(content_lines):
        return ""
    
    target_line = content_lines[line_number - 1].strip()
    if not target_line:
        return ""
    
    # Start with the target line
    start = line_number - 1
    end = line_number - 1
    
    # Go backward until we hit an empty line or beginning of file
    while start > 0:
        prev_line = content_lines[start - 1].strip()
        if not prev_line:  # Empty line - stop here
            break
        start -= 1
    
    # Go forward until we hit an empty line or end of file
    while end < len(content_lines) - 1:
        next_line = content_lines[end + 1].strip()
        if not next_line:  # Empty line - stop here
            break
        end += 1
    
    # Extract the full paragraph including all non-empty lines in range
    paragraph_lines = []
    for i in range(start, end + 1):
        line = content_lines[i].strip()
        if line:  # Only include non-empty lines
            paragraph_lines.append(line)
    
    return ' '.join(paragraph_lines)

def parse_pr_comments(comments_input):
    """Parse PR review comments from GitHub API JSON."""
    try:
        # Always treat as a file path
        print(f"Trying to open file: {comments_input}", file=sys.stderr)
        print(f"File exists: {Path(comments_input).exists()}", file=sys.stderr)
        print(f"File size: {Path(comments_input).stat().st_size if Path(comments_input).exists() else 'N/A'}", file=sys.stderr)
        
        with open(comments_input, 'r', encoding='utf-8') as f:
            contents = f.read()
            print(f"File contents length: {len(contents)}", file=sys.stderr)
            print(f"First 100 chars: {contents[:100]}", file=sys.stderr)
            comments_data = json.loads(contents)
        
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
        
        # Extract general PR comments (excluding bot comments)
        pr_comments = []
        if 'comments' in comments_data:
            for comment in comments_data['comments']:
                # Skip GitHub bot comments
                if comment['user']['login'] != 'github-actions[bot]':
                    pr_comments.append({
                        'body': comment['body'],
                        'author': comment['user']['login']
                    })
        
        # Extract ALL review-level comments (approval comments, change requests, etc.)
        review_approval_comments = []
        if 'reviews' in comments_data:
            for review in comments_data['reviews']:
                # Include ALL reviews with comments, regardless of state
                if review.get('body') and review['body'].strip():
                    review_approval_comments.append({
                        'body': review['body'],
                        'author': review['user']['login'],
                        'state': review['state']
                    })
        
        return review_comments, pr_comments, review_approval_comments
        
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error parsing comments: {e}", file=sys.stderr)
        return [], [], []

def create_weblog_entry(frontmatter, archive_content, review_comments, pr_comments, review_approval_comments, archive_filename):
    """Create weblog entry with quoted paragraphs and comments."""
    
    # Create weblog frontmatter - carry over ALL fields from archive
    weblog_frontmatter = frontmatter.copy()  # Start with all archive fields
    
    # Add weblog-specific fields
    weblog_frontmatter['date'] = datetime.now().strftime('%Y-%m-%d')
    weblog_frontmatter['link'] = f"/archive/{Path(archive_filename).name}"
    weblog_frontmatter['tags'] = frontmatter.get('tags', []) + ['weblog']
    weblog_frontmatter['type'] = 'weblog'
    
    # Start building the weblog content
    weblog_content = []
    
    # Add review approval comments (from "Approve" button)
    if review_approval_comments:
        for approval_comment in review_approval_comments:
            weblog_content.append(f"{approval_comment['body']}\n")
    
    # Add small divider before line-specific review comments
    if review_comments:
        weblog_content.append("---\n")
    
    # Process ALL line-specific comments with quoted paragraphs
    # Use the full file content including frontmatter since line numbers reference the entire file
    with open(archive_filename, 'r', encoding='utf-8') as f:
        full_file_content = f.read()
    archive_lines = full_file_content.split('\n')
    
    if review_comments:
        # Sort comments by line number to maintain logical order
        sorted_comments = sorted(review_comments, key=lambda x: x.get('line', 0))
        for i, comment in enumerate(sorted_comments):
            # Include ALL comments, with or without line numbers
            if comment.get('line'):
                # Extract the paragraph for this line
                line_number = comment['line']
                paragraph = extract_paragraph_for_line(archive_lines, line_number)
                
                if paragraph:
                    weblog_content.append(f"> {paragraph}\n")
                else:
                    # If paragraph extraction fails, include the line itself
                    if line_number <= len(archive_lines):
                        line_content = archive_lines[line_number - 1].strip()
                        if line_content:
                            weblog_content.append(f"> {line_content}\n")
                weblog_content.append(f"{comment['body']}\n")
            else:
                # Comments without line numbers (shouldn't happen but include them anyway)
                weblog_content.append(f"{comment['body']}\n")
            
            # Add delimiter between quote-comment pairs (except after the last one)
            if i < len(sorted_comments) - 1:
                weblog_content.append("---\n")
    
    return weblog_frontmatter, '\n'.join(weblog_content)

def create_weblog_file(frontmatter, content, archive_filename, output_dir="weblog"):
    """Create the weblog markdown file."""
    
    # Reuse the archive filename
    filename = Path(archive_filename).name
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
        review_comments, pr_comments, review_approval_comments = parse_pr_comments(comments_json)
        
        # Create weblog entry
        weblog_frontmatter, weblog_content = create_weblog_entry(
            frontmatter, archive_content, review_comments, pr_comments, review_approval_comments, archive_file
        )
        
        # Create the weblog file
        weblog_file = create_weblog_file(weblog_frontmatter, weblog_content, archive_file)
        
        # Output for GitHub Actions
        print(f"weblog_file:{weblog_file}")
        print(f"title:{weblog_frontmatter['title']}")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
