#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pyyaml>=6.0.1",
#     "python-dotenv>=1.0.0"
# ]
# ///

import yaml
import sys
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

def validate_linklog_file(filepath):
    """Validate a linklog markdown file."""
    errors = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        errors.append(f"Could not read file {filepath}: {e}")
        return errors
    
    # Check for frontmatter
    if not content.startswith('---\n'):
        errors.append(f"File {filepath} must start with YAML frontmatter")
        return errors
    
    try:
        parts = content.split('---\n', 2)
        if len(parts) < 3:
            errors.append(f"Invalid frontmatter format in {filepath}")
            return errors
        
        frontmatter = yaml.safe_load(parts[1])
        markdown_content = parts[2].strip()
        
    except yaml.YAMLError as e:
        errors.append(f"Invalid YAML frontmatter in {filepath}: {e}")
        return errors
    
    # Validate required frontmatter fields
    required_fields = ['title', 'date', 'original_link', 'archive_link', 'type']
    for field in required_fields:
        if field not in frontmatter:
            errors.append(f"Missing required field '{field}' in {filepath}")
        elif not frontmatter[field]:
            errors.append(f"Empty required field '{field}' in {filepath}")
    
    # Validate type is 'linklog'
    if frontmatter.get('type') != 'linklog':
        errors.append(f"Type must be 'linklog' in {filepath}, got '{frontmatter.get('type')}'")
    
    # Validate date format (YYYY-MM-DD)
    date_val = frontmatter.get('date')
    if date_val:
        try:
            from datetime import datetime
            datetime.strptime(str(date_val), '%Y-%m-%d')
        except ValueError:
            errors.append(f"Invalid date format in {filepath}. Expected YYYY-MM-DD, got '{date_val}'")
    
    # Validate URLs
    for url_field in ['original_link', 'archive_link']:
        url_val = frontmatter.get(url_field)
        if url_val and not (url_val.startswith('http') or url_val.startswith('archive/')):
            errors.append(f"Invalid {url_field} in {filepath}: '{url_val}'")
    
    # Validate tags is a list
    if 'tags' in frontmatter and not isinstance(frontmatter['tags'], list):
        errors.append(f"Tags must be a list in {filepath}")
    
    # Validate minimum content length
    if len(markdown_content.strip()) < 50:
        errors.append(f"Linklog content too short in {filepath} (minimum 50 characters)")
    
    # Check for required sections in content
    if 'original_link' in frontmatter and frontmatter['original_link']:
        if not any(link in markdown_content for link in [frontmatter['original_link'], 'Original:']):
            errors.append(f"Linklog should reference original link in content: {filepath}")
    
    return errors

def validate_directory(directory):
    """Validate all linklog files in a directory."""
    directory_path = Path(directory)
    
    if not directory_path.exists():
        print(f"Directory {directory} does not exist")
        return False
    
    if not directory_path.is_dir():
        print(f"{directory} is not a directory")
        return False
    
    all_errors = []
    linklog_files = list(directory_path.glob('*.md'))
    
    if not linklog_files:
        print(f"No markdown files found in {directory}")
        return True
    
    for filepath in linklog_files:
        if filepath.name == '.gitkeep':
            continue
            
        errors = validate_linklog_file(filepath)
        if errors:
            all_errors.extend([f"{filepath.name}: {error}" for error in errors])
    
    if all_errors:
        print("Validation errors found:")
        for error in all_errors:
            print(f"  - {error}")
        return False
    
    print(f"All {len(linklog_files)} linklog files are valid")
    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python linklog_validator.py <directory>")
        sys.exit(1)
    
    directory = sys.argv[1]
    
    if validate_directory(directory):
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()
