#!/usr/bin/env python3
"""
Script to fix archive file dates based on their corresponding weblog dates.
For weblog files that are not from 2025-07-21/20, updates the corresponding
archive file's date in both frontmatter and filename.
"""

import re
import shutil
from pathlib import Path
import sys

def extract_date_from_filename(filename):
    """Extract date from filename format: YYYY-MM-DD-title.md"""
    match = re.match(r'^(\d{4}-\d{2}-\d{2})-', filename)
    if match:
        return match.group(1)
    return None

def extract_archive_filename_from_weblog(weblog_path):
    """Extract archive filename from weblog file link."""
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
                    return f"{link_match.group(1)}.md"
    except Exception as e:
        print(f"Error reading {weblog_path}: {e}")
    
    return None

def update_archive_date(archive_path, new_date, dry_run=False):
    """Update the date in archive file frontmatter and rename file."""
    try:
        with open(archive_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.startswith('---'):
            print(f"No frontmatter found in {archive_path}")
            return False
        
        parts = content.split('---', 2)
        if len(parts) < 3:
            print(f"Invalid frontmatter in {archive_path}")
            return False
        
        frontmatter = parts[1]
        body_content = parts[2]
        
        # Generate new filename
        old_path = Path(archive_path)
        filename = old_path.name
        
        # Extract title part from current filename (everything after the date)
        filename_match = re.match(r'^\d{4}-\d{2}-\d{2}-(.+)$', filename)
        if filename_match:
            title_part = filename_match.group(1)
            new_filename = f"{new_date}-{title_part}"
            new_path = old_path.parent / new_filename
            
            if dry_run:
                if old_path != new_path:
                    print(f"[DRY RUN] Would update {filename} -> {new_filename}")
                else:
                    print(f"[DRY RUN] Would update frontmatter in {filename} (no rename needed)")
                return True
            
            # Update date in frontmatter
            updated_frontmatter = re.sub(
                r'^date:\s*.*$', 
                f'date: {new_date}', 
                frontmatter, 
                flags=re.MULTILINE
            )
            
            # Reconstruct content
            updated_content = f"---{updated_frontmatter}---{body_content}"
            
            # Write updated content
            with open(archive_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            # Rename file
            if old_path != new_path:
                shutil.move(str(old_path), str(new_path))
                print(f"✓ Updated {filename} -> {new_filename}")
                return str(new_path)
            else:
                print(f"✓ Updated frontmatter in {filename} (no rename needed)")
                return str(old_path)
        else:
            print(f"Could not parse filename format: {filename}")
            return False
            
    except Exception as e:
        print(f"Error updating {archive_path}: {e}")
        return False

def main():
    """Main function to fix archive dates from weblog dates."""
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
    
    # Filter weblog files that are NOT from 2025-07-21 or 2025-07-20
    files_to_process = []
    for weblog_file in weblog_files:
        filename = weblog_file.name
        if not (filename.startswith('2025-07-21-') or filename.startswith('2025-07-20-')):
            files_to_process.append(weblog_file)
    
    print(f"Found {len(files_to_process)} weblog files that need archive date fixes")
    
    # Process each weblog file
    updated_count = 0
    for weblog_path in files_to_process:
        weblog_filename = weblog_path.name
        print(f"\nProcessing weblog: {weblog_filename}")
        
        # Extract date from weblog filename
        weblog_date = extract_date_from_filename(weblog_filename)
        if not weblog_date:
            print(f"Could not extract date from {weblog_filename}")
            continue
        
        print(f"Weblog date: {weblog_date}")
        
        # Find corresponding archive file
        archive_filename = extract_archive_filename_from_weblog(weblog_path)
        if not archive_filename:
            print(f"Could not find archive filename from {weblog_filename}")
            continue
        
        archive_path = archive_dir / archive_filename
        if not archive_path.exists():
            print(f"Archive file not found: {archive_path}")
            continue
        
        print(f"Archive file: {archive_filename}")
        
        # Check if archive already has the correct date
        current_archive_date = extract_date_from_filename(archive_filename)
        if current_archive_date == weblog_date:
            print(f"Archive already has correct date: {current_archive_date}")
            continue
        
        print(f"Archive current date: {current_archive_date} -> updating to: {weblog_date}")
        
        # Update archive file
        result = update_archive_date(archive_path, weblog_date, dry_run)
        if result:
            updated_count += 1
        else:
            print(f"Failed to update {archive_filename}")
    
    action = "would update" if dry_run else "updated"
    print(f"\n✓ Successfully {action} {updated_count}/{len(files_to_process)} archive files")

if __name__ == '__main__':
    main()
