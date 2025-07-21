#!/usr/bin/env python3
"""
Script to trigger GitHub workflow for all URLs in the pickle file.
"""

import pickle
import subprocess
import sys
import time
from pathlib import Path

def load_urls_from_pickle(pickle_path):
    """Load URLs from the pickle file."""
    try:
        with open(pickle_path, 'rb') as f:
            records = pickle.load(f)
        
        urls = [record['link'] for record in records if 'link' in record]
        return urls
    except Exception as e:
        print(f"Error loading pickle file: {e}")
        return []

def trigger_github_workflow(url):
    """Trigger GitHub workflow by creating an issue with the URL."""
    try:
        # Create issue with URL in the body
        cmd = [
            'gh', 'issue', 'create',
            '--title', f'Process URL: {url}',
            '--body', f'URL: {url}'
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✓ Created issue for: {url}")
            return True
        else:
            print(f"✗ Failed to create issue for: {url}")
            print(f"Error: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"✗ Error creating issue for {url}: {e}")
        return False

def main():
    """Main function to process all URLs."""
    pickle_path = Path('../../mbgsec/linklogs.pkl')
    
    if not pickle_path.exists():
        print(f"Pickle file not found: {pickle_path}")
        sys.exit(1)
    
    print("Loading URLs from pickle file...")
    urls = load_urls_from_pickle(pickle_path)
    
    if not urls:
        print("No URLs found in pickle file")
        sys.exit(1)
    
    print(f"Found {len(urls)} URLs to process")
    
    # Auto-confirm for batch processing
    print(f"Creating {len(urls)} GitHub issues to trigger workflows...")
    
    # Process URLs
    success_count = 0
    for i, url in enumerate(urls, 1):
        print(f"\n[{i}/{len(urls)}] Processing: {url}")
        
        if trigger_github_workflow(url):
            success_count += 1
        
        # Add delay to avoid rate limiting
        if i < len(urls):
            time.sleep(30)
    
    print(f"\n✓ Successfully created {success_count}/{len(urls)} issues")

if __name__ == '__main__':
    main()
