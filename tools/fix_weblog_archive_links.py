#!/usr/bin/env python3
"""
Script to fix archive links in weblog files.
Updates the archive links in weblog frontmatter to point to the correctly named archive files.
"""

import re
import os
from pathlib import Path
import sys

def extract_archive_link_from_weblog(weblog_path):
    """Extract archive link from weblog file frontmatter."""
    try:
        with open(weblog_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract frontmatter from weblog file
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter = parts[1]
                
                # Extract the archive link reference
                link_match = re.search(r'^link:\s*/archive/(.+)$', frontmatter, re.MULTILINE)
                if link_match:
                    return link_match.group(1)
    except Exception as e:
        print(f"Error reading {weblog_path}: {e}")
    
    return None

def find_actual_archive_file(archive_dir, old_archive_name):
    """Find the actual archive file that corresponds to the old name."""
    # Extract title part from old name (remove date prefix)
    title_match = re.match(r'^\d{4}-\d{2}-\d{2}-(.+)$', old_archive_name)
    if not title_match:
        return None
    
    title_part = title_match.group(1)
    
    # Look for archive file with same title but different date
    for archive_file in archive_dir.glob('*.md'):
        filename = archive_file.name
        # Check if filename ends with the same title part
        if filename.endswith(f'-{title_part}.md'):
            return filename[:-3]  # Remove .md extension
    
    return None

def update_weblog_archive_link(weblog_path, new_archive_name, dry_run=False):
    """Update the archive link in weblog file frontmatter."""
    try:
        with open(weblog_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.startswith('---'):
            print(f"No frontmatter found in {weblog_path}")
            return False
        
        parts = content.split('---', 2)
        if len(parts) < 3:
            print(f"Invalid frontmatter in {weblog_path}")
            return False
        
        frontmatter = parts[1]
        body_content = parts[2]
        
        if dry_run:
            print(f"[DRY RUN] Would update archive link to: /archive/{new_archive_name}")
            return True
        
        # Update archive link in frontmatter
        updated_frontmatter = re.sub(
            r'^link:\s*/archive/.+$', 
            f'link: /archive/{new_archive_name}', 
            frontmatter, 
            flags=re.MULTILINE
        )
        
        # Reconstruct content
        updated_content = f"---{updated_frontmatter}---{body_content}"
        
        # Write updated content
        with open(weblog_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"✓ Updated archive link to: /archive/{new_archive_name}")
        return True
            
    except Exception as e:
        print(f"Error updating {weblog_path}: {e}")
        return False

def main():
    """Main function to fix weblog archive links."""
    # Check for dry run flag
    dry_run = '--dry-run' in sys.argv
    if dry_run:
        print("=== DRY RUN MODE ===")
    
    weblog_dir = Path('weblog')
    archive_dir = Path('archive')
    
    if not weblog_dir.exists():
        print(f"Weblog directory not found: {weblog_dir}")
        return
    
    if not archive_dir.exists():
        print(f"Archive directory not found: {archive_dir}")
        return
    
    # Find all weblog files
    weblog_files = list(weblog_dir.glob('*.md'))
    print(f"Found {len(weblog_files)} weblog files")
    
    # Process each weblog file
    updated_count = 0
    for weblog_path in weblog_files:
        weblog_filename = weblog_path.name
        print(f"\nProcessing weblog: {weblog_filename}")
        
        # Extract current archive link
        current_archive_name = extract_archive_link_from_weblog(weblog_path)
        if not current_archive_name:
            print(f"Could not extract archive link from {weblog_filename}")
            continue
        
        print(f"Current archive link: /archive/{current_archive_name}")
        
        # Check if the referenced archive file exists
        expected_archive_path = archive_dir / f"{current_archive_name}.md"
        if expected_archive_path.exists():
            print(f"Archive file exists, no update needed")
            continue
        
        # Find the actual archive file
        actual_archive_name = find_actual_archive_file(archive_dir, current_archive_name)
        if not actual_archive_name:
            print(f"Could not find actual archive file for {current_archive_name}")
            continue
        
        print(f"Found actual archive: {actual_archive_name}")
        
        # Update weblog archive link
        if update_weblog_archive_link(weblog_path, actual_archive_name, dry_run):
            updated_count += 1
        else:
            print(f"Failed to update {weblog_filename}")
    
    action = "would update" if dry_run else "updated"
    print(f"\n✓ Successfully {action} {updated_count}/{len(weblog_files)} weblog files")

if __name__ == '__main__':
    main()
