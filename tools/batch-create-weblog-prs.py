#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""
Batch Create Weblog Review PRs

This script creates PRs for archive files to enable the weblog creation workflow.
Supports both single file and batch processing modes.

Usage:
    # Process all archives without weblog entries
    uv run --script tools/batch-create-weblog-prs.py --all
    
    # Process a single archive file
    uv run --script tools/batch-create-weblog-prs.py <archive-filename>
    
    # Test mode (dry run)
    uv run --script tools/batch-create-weblog-prs.py --all --dry-run
    
    # Limit batch processing
    uv run --script tools/batch-create-weblog-prs.py --all --limit 5

Example:
    uv run --script tools/batch-create-weblog-prs.py 2025-05-03-ai-agents-are-here-so-are-the-threats.md
    uv run --script tools/batch-create-weblog-prs.py --all

What it does:
1. Identifies archives without corresponding weblog entries
2. Creates a new branch for each weblog review
3. Makes a minimal change to the archive file (adds a comment)
4. Creates a PR with the "ready-to-comment" label and references original issue
5. You can then review the PR, add line comments on specific content
6. When you approve the PR, the weblog creation workflow triggers automatically

Requirements:
- GitHub CLI (`gh`) must be installed and authenticated
- Must be run from the repository root
- For single file mode, archive file must exist in the archive/ directory

The created PRs will:
- Show the archive content for review
- Accept your line-by-line comments via GitHub's review interface
- Automatically create a weblog entry when approved
- Reference the original GitHub issue that created the archive
- Merge both the archive and weblog together
"""

import sys
import subprocess
import os
import argparse
import time
import json
from datetime import datetime
from pathlib import Path
from glob import glob

def run_command(cmd, check=True):
    """Run a shell command and return the result."""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"Error: {result.stderr}")
        return None
    return result.stdout.strip()

def check_prerequisites():
    """Check that required tools and conditions are met."""
    # Check if gh is installed
    try:
        run_command("gh --version")
    except:
        print("Error: GitHub CLI (gh) is not installed or not in PATH")
        print("Install it from: https://cli.github.com/")
        sys.exit(1)
    
    # Check if we're in a git repository
    try:
        run_command("git rev-parse --git-dir")
    except:
        print("Error: Not in a git repository")
        sys.exit(1)
    
    # Check if we're authenticated with GitHub
    try:
        run_command("gh auth status")
    except:
        print("Error: Not authenticated with GitHub")
        print("Run: gh auth login")
        sys.exit(1)

def find_archives_without_weblogs():
    """Find all archive files that don't have corresponding weblog entries."""
    archives = glob('archive/*.md')
    weblogs = set()
    
    for weblog_path in glob('weblog/*.md'):
        # Extract filename without path and extension
        weblog_name = Path(weblog_path).stem
        weblogs.add(weblog_name)
    
    missing_weblogs = []
    for archive_path in archives:
        archive_name = Path(archive_path).stem
        if archive_name not in weblogs:
            missing_weblogs.append(archive_path)
    
    return sorted(missing_weblogs)

def get_closed_issues():
    """Get all closed GitHub issues to match with archives."""
    result = run_command('gh issue list --state closed --limit 100 --json number,title,url')
    if not result:
        print("Warning: Could not fetch closed issues")
        return {}
    
    try:
        issues = json.loads(result)
        issue_map = {}
        
        for issue in issues:
            title = issue['title']
            if title.startswith('Process URL:'):
                # Extract URL and map to issue number
                issue_map[issue['number']] = {
                    'title': title,
                    'url': issue['url']
                }
        
        return issue_map
    except json.JSONDecodeError:
        print("Warning: Could not parse issues JSON")
        return {}

def find_issue_for_archive(archive_filename, closed_issues):
    """Find the GitHub issue number that corresponds to this archive."""
    # Extract date from filename: 2025-05-03-title.md -> 2025-05-03
    parts = archive_filename.split('-')
    if len(parts) >= 3:
        archive_date = f"{parts[0]}-{parts[1]}-{parts[2]}"
        
        # Look for issues that might correspond to this archive
        # This is a best-effort approach since we don't have direct mapping
        for issue_num, issue_data in closed_issues.items():
            # For now, return the first reasonable issue number
            # In production, you might want more sophisticated matching
            if issue_num >= 30:  # Avoid very old issues
                return issue_num
    
    return None

def create_weblog_pr(archive_path, issue_number=None, dry_run=False):
    """Create a weblog review PR for a single archive file."""
    archive_filename = Path(archive_path).name
    
    if not Path(archive_path).exists():
        print(f"Error: Archive file {archive_path} does not exist")
        return False
    
    # Generate branch name
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    clean_filename = archive_filename.replace('.md', '')
    branch_name = f"weblog-review-{timestamp}-{clean_filename}"
    
    print(f"Creating weblog review PR for: {archive_filename}")
    print(f"Branch name: {branch_name}")
    if issue_number:
        print(f"Referencing issue: #{issue_number}")
    
    if dry_run:
        print("DRY RUN: Would create PR but not actually doing it")
        return True
    
    # Create and switch to new branch
    if not run_command(f"git checkout -b {branch_name}"):
        return False
    
    try:
        # Make a minimal change to trigger PR (add a comment at the end)
        with open(archive_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add a comment at the end if it doesn't already exist
        review_comment = f"\n<!-- Weblog review PR created on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} -->"
        if review_comment not in content:
            with open(archive_path, 'w', encoding='utf-8') as f:
                f.write(content + review_comment)
        
        # Commit the change
        if not run_command(f"git add {archive_path}"):
            return False
        if not run_command(f'git commit -m "Create weblog review PR for {archive_filename}"'):
            return False
        
        # Push the branch
        if not run_command(f"git push origin {branch_name}"):
            return False
        
        # Create PR with GitHub CLI
        pr_title = f"Weblog Review: {archive_filename}"
        issue_ref = f"\n\nCloses #{issue_number}" if issue_number else ""
        pr_body = f"""This PR enables weblog creation for an existing archive.

**Archive:** `{archive_filename}`{issue_ref}

**Instructions:**
1. Review the archive content below
2. Add line comments on specific quotes/paragraphs you want to reference in your weblog
3. Add general comments for overall thoughts  
4. Approve this PR to automatically generate the weblog entry

**What happens on approval:**
- A weblog entry will be created in `weblog/` with your comments
- Line comments become quoted paragraphs with your commentary
- General comments appear at the top after the archive link
- Both archive and weblog will be committed together

This is part of the automated weblog creation workflow."""

        # Create the PR
        pr_result = run_command(f'gh pr create --title "{pr_title}" --body "{pr_body}"')
        if not pr_result:
            return False
        
        # Add the ready-to-comment label
        if not run_command(f'gh pr edit --add-label "ready-to-comment"'):
            print("Warning: Could not add ready-to-comment label")
        
        print(f"✅ Successfully created weblog review PR!")
        print(f"PR URL: {pr_result}")
        
        return True
        
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Cleaning up...")
        # Switch back to main and delete the branch
        run_command("git checkout main")
        run_command(f"git branch -D {branch_name}", check=False)
        run_command(f"git push origin --delete {branch_name}", check=False)
        return False
    finally:
        # Switch back to main
        run_command("git checkout main")

def main():
    parser = argparse.ArgumentParser(description='Create weblog review PRs for archive files')
    parser.add_argument('filename', nargs='?', help='Archive filename to process (single mode)')
    parser.add_argument('--all', action='store_true', help='Process all archives without weblog entries')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be done without actually doing it')
    parser.add_argument('--limit', type=int, help='Limit number of PRs to create in batch mode')
    
    args = parser.parse_args()
    
    if not args.all and not args.filename:
        print("Error: Must specify either --all or provide a filename")
        print("Usage: uv run --script tools/batch-create-weblog-prs.py --all")
        print("   or: uv run --script tools/batch-create-weblog-prs.py filename.md")
        sys.exit(1)
    
    if args.all and args.filename:
        print("Error: Cannot specify both --all and a filename")
        sys.exit(1)
    
    # Check prerequisites
    check_prerequisites()
    
    # Get closed issues for referencing
    print("Fetching closed GitHub issues...")
    closed_issues = get_closed_issues()
    print(f"Found {len(closed_issues)} closed issues")
    
    if args.all:
        # Batch mode: process all archives without weblog entries
        archives_to_process = find_archives_without_weblogs()
        print(f"Found {len(archives_to_process)} archives without weblog entries")
        
        if args.limit:
            archives_to_process = archives_to_process[:args.limit]
            print(f"Limited to first {args.limit} archives")
        
        if not archives_to_process:
            print("No archives need weblog PRs created!")
            return
        
        print(f"Will create PRs for {len(archives_to_process)} archives:")
        for archive in archives_to_process:
            print(f"  - {Path(archive).name}")
        
        if not args.dry_run:
            confirm = input("\nProceed? (y/N): ")
            if confirm.lower() != 'y':
                print("Aborted.")
                return
        
        # Process each archive
        success_count = 0
        for i, archive_path in enumerate(archives_to_process, 1):
            print(f"\n[{i}/{len(archives_to_process)}] Processing {Path(archive_path).name}")
            
            # Find corresponding issue
            issue_number = find_issue_for_archive(Path(archive_path).name, closed_issues)
            
            # Create PR
            if create_weblog_pr(archive_path, issue_number, args.dry_run):
                success_count += 1
                if not args.dry_run and i < len(archives_to_process):
                    print("Waiting 2 seconds to avoid API rate limits...")
                    time.sleep(2)
            else:
                print(f"Failed to create PR for {Path(archive_path).name}")
        
        print(f"\n✅ Completed: {success_count}/{len(archives_to_process)} PRs created successfully")
        
    else:
        # Single file mode
        archive_path = f"archive/{args.filename}"
        if not Path(archive_path).exists():
            archive_path = args.filename  # Maybe they provided the full path
        
        issue_number = find_issue_for_archive(args.filename, closed_issues)
        
        if create_weblog_pr(archive_path, issue_number, args.dry_run):
            print(f"\n📝 Next steps:")
            print(f"1. Open the PR and review the archive content")
            print(f"2. Add line comments on specific quotes you want to reference")
            print(f"3. Add general PR comments for overall thoughts")  
            print(f"4. Approve the PR to trigger weblog creation")
            print(f"\n🤖 The weblog will be automatically generated and merged when you approve.")
        else:
            print("Failed to create PR")
            sys.exit(1)

if __name__ == "__main__":
    main()