#!/usr/bin/env python3
"""
Script to create approval reviews for open PRs using content from the pickle file.
"""

import pickle
import subprocess
import json
import re
import sys
from pathlib import Path

def load_pickle_data(pickle_path):
    """Load URL to content mapping from pickle file."""
    try:
        with open(pickle_path, 'rb') as f:
            records = pickle.load(f)
        
        # Create URL -> content mapping
        url_to_content = {}
        for record in records:
            if 'link' in record and 'content' in record:
                url_to_content[record['link']] = record['content']
        
        return url_to_content
    except Exception as e:
        print(f"Error loading pickle file: {e}")
        return {}

def get_open_prs():
    """Get list of open PRs with their numbers and associated URLs."""
    try:
        cmd = ['gh', 'pr', 'list', '--state', 'open', '--limit', '50', '--json', 'number,title,body']
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Error getting PRs: {result.stderr}")
            return []
        
        prs = json.loads(result.stdout)
        
        # Extract URLs from PR bodies (look for archive files)
        pr_urls = []
        for pr in prs:
            pr_number = pr['number']
            title = pr['title']
            
            # Skip if not an archive PR
            if 'Add new link:' not in title:
                continue
            
            # Get the archive file from the PR to extract URL
            try:
                cmd = ['gh', 'pr', 'view', str(pr_number), '--json', 'files']
                result = subprocess.run(cmd, capture_output=True, text=True)
                
                if result.returncode == 0:
                    files_data = json.loads(result.stdout)
                    
                    # Look for archive file
                    for file_info in files_data['files']:
                        if file_info['path'].startswith('archive/') and file_info['path'].endswith('.md'):
                            # Read the archive file to get the URL
                            try:
                                cmd = ['gh', 'pr', 'view', str(pr_number), '--json', 'additions']
                                diff_result = subprocess.run(cmd, capture_output=True, text=True)
                                
                                # Get file content using gh pr diff
                                cmd = ['gh', 'pr', 'diff', str(pr_number), '--name-only']
                                diff_result = subprocess.run(cmd, capture_output=True, text=True)
                                
                                if diff_result.returncode == 0:
                                    # Get the actual file content
                                    cmd = ['gh', 'pr', 'diff', str(pr_number)]
                                    full_diff = subprocess.run(cmd, capture_output=True, text=True)
                                    
                                    if full_diff.returncode == 0:
                                        diff_content = full_diff.stdout
                                        
                                        # Extract URL from diff content (look for +link: lines)
                                        url_match = re.search(r'^\+link:\s*(.+)$', diff_content, re.MULTILINE)
                                        if url_match:
                                            url = url_match.group(1).strip()
                                            pr_urls.append({
                                                'number': pr_number,
                                                'title': title,
                                                'url': url,
                                                'archive_file': file_info['path']
                                            })
                                            print(f"Found PR #{pr_number}: {url}")
                                            break
                            except Exception as e:
                                print(f"Error reading archive file for PR #{pr_number}: {e}")
                                continue
            except Exception as e:
                print(f"Error processing PR #{pr_number}: {e}")
                continue
        
        return pr_urls
    except Exception as e:
        print(f"Error getting open PRs: {e}")
        return []

def create_approval_review(pr_number, comment, dry_run=False):
    """Create an approval review on the PR with the given comment."""
    if dry_run:
        print(f"[DRY RUN] Would create approval review for PR #{pr_number}")
        print(f"[DRY RUN] Comment preview: {comment[:100]}...")
        return True
    
    try:
        cmd = [
            'gh', 'pr', 'review', str(pr_number),
            '--approve',
            '--body', comment
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✓ Created approval review for PR #{pr_number}")
            return True
        else:
            print(f"✗ Failed to create approval review for PR #{pr_number}")
            print(f"Error: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"✗ Error creating approval review for PR #{pr_number}: {e}")
        return False

def main():
    """Main function to process PRs and create approval reviews."""
    # Check for dry run flag
    dry_run = '--dry-run' in sys.argv
    if dry_run:
        print("=== DRY RUN MODE ===")
    
    pickle_path = Path('../mbgsec/linklogs.pkl')
    
    if not pickle_path.exists():
        print(f"Pickle file not found: {pickle_path}")
        sys.exit(1)
    
    print("Loading content from pickle file...")
    url_to_content = load_pickle_data(pickle_path)
    
    if not url_to_content:
        print("No content found in pickle file")
        sys.exit(1)
    
    print(f"Loaded {len(url_to_content)} URL-content mappings")
    
    print("\nGetting open PRs...")
    open_prs = get_open_prs()
    
    if not open_prs:
        print("No open PRs found")
        sys.exit(0)
    
    print(f"Found {len(open_prs)} open archive PRs")
    
    # Process each PR
    success_count = 0
    for pr_info in open_prs:
        pr_number = pr_info['number']
        url = pr_info['url']
        title = pr_info['title']
        
        print(f"\nProcessing PR #{pr_number}: {title}")
        print(f"URL: {url}")
        
        # Find matching content
        if url in url_to_content:
            content = url_to_content[url]
            print(f"Found matching content ({len(content)} chars)")
            
            # Create approval review
            if create_approval_review(pr_number, content, dry_run):
                success_count += 1
        else:
            print(f"No matching content found for URL: {url}")
    
    action = "would create" if dry_run else "created"
    print(f"\n✓ Successfully {action} {success_count}/{len(open_prs)} approval reviews")

if __name__ == '__main__':
    main()
