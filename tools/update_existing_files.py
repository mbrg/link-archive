#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pyyaml>=6.0.1",
# ]
# ///

import yaml
import os
import re
from pathlib import Path

def update_archive_files():
    """Update archive files to replace pipe characters with diamonds in titles."""
    archive_dir = Path("archive")
    if not archive_dir.exists():
        print("Archive directory not found")
        return
    
    updated_count = 0
    for file_path in archive_dir.glob("*.md"):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace pipe characters with diamond symbols in titles
        # Pattern to match title lines with pipes (quoted, escaped, or unquoted)
        title_with_pipes_pattern = r'title: ([^"\n]*\|[^\n]*|"[^"]*\\?\|[^"]*")'
        
        def replace_pipes_in_title(match):
            title_content = match.group(1)
            # Handle quoted titles
            if title_content.startswith('"') and title_content.endswith('"'):
                inner_content = title_content[1:-1]
                # Replace both escaped and unescaped pipes
                cleaned = inner_content.replace('\\|', '◆').replace('|', '◆')
                return f'title: "{cleaned}"'
            else:
                # Unquoted title
                cleaned = title_content.replace('|', '◆')
                return f'title: "{cleaned}"'
        
        if re.search(title_with_pipes_pattern, content):
            new_content = re.sub(title_with_pipes_pattern, replace_pipes_in_title, content)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"Updated archive: {file_path.name}")
            updated_count += 1
    
    print(f"Updated {updated_count} archive files")

def update_weblog_files():
    """Update weblog files to remove H1 titles and fix links."""
    weblog_dir = Path("weblog")
    if not weblog_dir.exists():
        print("Weblog directory not found")
        return
    
    updated_count = 0
    for file_path in weblog_dir.glob("*.md"):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Split frontmatter and content
        if content.startswith('---\n'):
            parts = content.split('---\n', 2)
            if len(parts) >= 3:
                frontmatter = yaml.safe_load(parts[1])
                markdown_content = parts[2].strip()
                
                needs_update = False
                
                # Replace pipes with diamonds in title
                if 'title' in frontmatter and '|' in frontmatter['title']:
                    frontmatter['title'] = frontmatter['title'].replace('|', '◆')
                    needs_update = True
                
                # Fix frontmatter link to start with /archive/
                if 'link' in frontmatter and frontmatter['link'].startswith('archive/'):
                    frontmatter['link'] = '/' + frontmatter['link']
                    needs_update = True
                
                # Remove H1 title (any H1 at the start of content)
                h1_pattern = r'^# [^\n]+\n'
                if re.match(h1_pattern, markdown_content):
                    markdown_content = re.sub(h1_pattern, '', markdown_content, count=1)
                    needs_update = True
                
                # Remove "Original:" and "Archive:" links
                original_pattern = r'\*\*Original:\*\* \[Link\]\([^)]+\)\s*\n'
                archive_pattern = r'\*\*Archive:\*\* \[Link\]\([^)]+\)\s*\n'
                
                if re.search(original_pattern, markdown_content):
                    markdown_content = re.sub(original_pattern, '', markdown_content)
                    needs_update = True
                
                if re.search(archive_pattern, markdown_content):
                    markdown_content = re.sub(archive_pattern, '', markdown_content)
                    needs_update = True
                
                # Clean up extra newlines at the beginning
                markdown_content = markdown_content.lstrip('\n')
                
                if needs_update:
                    # Recreate the file
                    new_content = f"""---
{yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)}---

{markdown_content}
"""
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    print(f"Updated weblog: {file_path.name}")
                    updated_count += 1
    
    print(f"Updated {updated_count} weblog files")

def main():
    print("Updating existing archive files...")
    update_archive_files()
    
    print("\nUpdating existing weblog files...")
    update_weblog_files()
    
    print("\nDone!")

if __name__ == "__main__":
    main()
