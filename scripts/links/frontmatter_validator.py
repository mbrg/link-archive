#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pyyaml>=6.0.1",
#     "requests>=2.31.0"
# ]
# ///

import os
import sys
import re
import yaml
import requests
from typing import Tuple

def validate_url(url: str) -> Tuple[bool, str]:
    """Validate if a URL is accessible."""
    try:
        response = requests.head(url, timeout=5, allow_redirects=True)
        return response.status_code < 400, f"Status code: {response.status_code}"
    except requests.RequestException as e:
        return False, str(e)

def validate_files(toread_dir):
    """Validate newly added files."""
    # Check if any files were added outside toreaddir
    added_files = os.popen('git diff --name-only HEAD~1').read().splitlines()
    for file in added_files:
        if not file.startswith(toread_dir):
            print(f"❌ Files were added outside {toread_dir} directory")
            sys.exit(1)
        
        # Validate filename format
        if not re.match(f'^{toread_dir}/[0-9]{{4}}-[0-9]{{2}}-[0-9]{{2}}-[a-z0-9-]+\\.md$', file):
            print(f"❌ Invalid filename format: {file}")
            sys.exit(1)
        
        # Validate YAML front matter and URL
        try:
            with open(file) as f:
                content = f.read()
                front_matter = yaml.safe_load(content.split('---')[1])
                
                if 'link' not in front_matter:
                    print(f"❌ No link found in front matter of: {file}")
                    sys.exit(1)
                
                url = front_matter['link']
                is_valid, reason = validate_url(url)
                if not is_valid:
                    print(f"❌ Invalid URL in {file}: {url}")
                    print(f"  Reason: {reason}")
                    sys.exit(1)
                
        except Exception as e:
            print(f"❌ Error processing {file}: {str(e)}")
            sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python validate_files.py <toread_dir>")
        sys.exit(1)
    
    toread_dir = sys.argv[1]
    validate_files(toread_dir) 