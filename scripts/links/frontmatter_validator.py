#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pyyaml>=6.0.1"
# ]
# ///

import os
import sys
import re
import yaml

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
        
        # Validate YAML front matter
        try:
            with open(file) as f:
                yaml.safe_load(f.read().split('---')[1])
        except:
            print(f"❌ Invalid YAML front matter in: {file}")
            sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python validate_files.py <toread_dir>")
        sys.exit(1)
    
    toread_dir = sys.argv[1]
    validate_files(toread_dir) 