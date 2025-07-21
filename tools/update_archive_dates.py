#!/usr/bin/env python3
"""
Script to update archive file dates from pickle data.
Updates both filename and frontmatter date to match original dates.
"""

import pickle
import re
import os
import shutil
from pathlib import Path
import yaml

def load_pickle_dates(pickle_path):
    """Load URL to date mapping from pickle file."""
    try:
        with open(pickle_path, 'rb') as f:
            records = pickle.load(f)
        
        # Create URL -> date mapping
        url_to_date = {}
        for record in records:
            if 'link' in record and 'date' in record:
                url_to_date[record['link']] = record['date']
        
        return url_to_date
    except Exception as e:
        print(f"Error loading pickle file: {e}")
        return {}

def extract_url_from_archive_file(file_path):
    """Extract URL from archive file frontmatter."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract frontmatter
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter = parts[1]
                # Extract link from frontmatter
                link_match = re.search(r'^link:\s*(.+)$', frontmatter, re.MULTILINE)
                if link_match:
                    return link_match.group(1).strip()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    
    return None

def update_file_date(file_path, new_date, dry_run=False):
    """Update the date in archive file frontmatter and rename file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.startswith('---'):
            print(f"No frontmatter found in {file_path}")
            return False
        
        parts = content.split('---', 2)
        if len(parts) < 3:
            print(f"Invalid frontmatter in {file_path}")
            return False
        
        frontmatter = parts[1]
        body_content = parts[2]
        
        # Generate new filename
        old_path = Path(file_path)
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
            with open(file_path, 'w', encoding='utf-8') as f:
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
        print(f"Error updating {file_path}: {e}")
        return False

def main():
    """Main function to update archive dates."""
    import sys
    
    # Check for dry run flag
    dry_run = '--dry-run' in sys.argv
    if dry_run:
        print("=== DRY RUN MODE ===")
    
    pickle_path = Path('../mbgsec/linklogs.pkl')
    archive_dir = Path('archive')
    
    if not pickle_path.exists():
        print(f"Pickle file not found: {pickle_path}")
        return
    
    if not archive_dir.exists():
        print(f"Archive directory not found: {archive_dir}")
        return
    
    print("Loading dates from pickle file...")
    url_to_date = load_pickle_dates(pickle_path)
    
    if not url_to_date:
        print("No date mappings found in pickle file")
        return
    
    print(f"Loaded {len(url_to_date)} URL-date mappings")
    
    # Find all archive files
    archive_files = list(archive_dir.glob('*.md'))
    print(f"Found {len(archive_files)} archive files")
    
    # Process each file
    updated_count = 0
    for file_path in archive_files:
        print(f"\nProcessing: {file_path.name}")
        
        # Extract URL from file
        url = extract_url_from_archive_file(file_path)
        if not url:
            print(f"Could not extract URL from {file_path.name}")
            continue
        
        print(f"URL: {url}")
        
        # Find matching date
        if url in url_to_date:
            original_date = url_to_date[url]
            print(f"Original date: {original_date}")
            
            # Update file
            result = update_file_date(file_path, original_date, dry_run)
            if result:
                updated_count += 1
            else:
                print(f"Failed to update {file_path.name}")
        else:
            print(f"No date found for URL: {url}")
    
    action = "would update" if dry_run else "updated"
    print(f"\n✓ Successfully {action} {updated_count}/{len(archive_files)} files")

if __name__ == '__main__':
    main()
