#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""
Create Weblog Review PR for Existing Archives

This script creates a PR for an existing archive file to enable the weblog creation workflow.
It allows you to review archive content, add line comments, and trigger weblog generation
through the normal PR approval process.

Usage:
    uv run --script tools/create-weblog-pr.py <archive-filename>

Example:
    uv run --script tools/create-weblog-pr.py 2025-05-03-ai-agents-are-here-so-are-the-threats.md

What it does:
1. Creates a new branch for the weblog review
2. Makes a minimal change to the archive file (adds a comment)
3. Creates a PR with the "ready-to-comment" label
4. You can then review the PR, add line comments on specific content
5. When you approve the PR, the weblog creation workflow triggers automatically

Requirements:
- GitHub CLI (`gh`) must be installed and authenticated
- Must be run from the repository root
- Archive file must exist in the archive/ directory

The created PR will:
- Show the archive content for review
- Accept your line-by-line comments via GitHub's review interface
- Automatically create a weblog entry when approved
- Merge both the archive and weblog together
"""

import sys
import subprocess
import os
from datetime import datetime
from pathlib import Path

def run_command(cmd, check=True):
    """Run a shell command and return the result."""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if check and result.returncode != 0:
        print(f"Error: {result.stderr}")
        sys.exit(1)
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

def main():
    if len(sys.argv) != 2:
        print("Usage: uv run --script tools/create-weblog-pr.py <archive-filename>")
        print("Example: uv run --script tools/create-weblog-pr.py 2025-05-03-ai-agents-are-here-so-are-the-threats.md")
        sys.exit(1)
    
    archive_filename = sys.argv[1]
    archive_path = f"archive/{archive_filename}"
    
    # Check prerequisites
    check_prerequisites()
    
    # Check if archive file exists
    if not Path(archive_path).exists():
        print(f"Error: Archive file {archive_path} does not exist")
        sys.exit(1)
    
    # Generate branch name
    timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
    branch_name = f"weblog-review-{timestamp}"
    
    print(f"Creating weblog review PR for: {archive_filename}")
    print(f"Branch name: {branch_name}")
    
    # Create and switch to new branch
    run_command(f"git checkout -b {branch_name}")
    
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
        run_command(f"git add {archive_path}")
        run_command(f'git commit -m "Create weblog review PR for {archive_filename}"')
        
        # Push the branch
        run_command(f"git push origin {branch_name}")
        
        # Create PR with GitHub CLI
        pr_title = f"Weblog Review: {archive_filename}"
        pr_body = f"""This PR enables weblog creation for an existing archive.

**Archive:** `{archive_filename}`

**Instructions:**
1. Review the archive content below
2. Add line comments on specific quotes/paragraphs you want to reference in your weblog
3. Add general comments for overall thoughts  
4. Approve this PR to automatically generate the weblog entry

**What happens on approval:**
- A weblog entry will be created in `weblog/` with your comments
- Line comments become quoted paragraphs with "My take:" responses
- General comments appear at the top after the archive link
- Both archive and weblog will be committed together

This is part of the automated weblog creation workflow."""

        # Create the PR
        pr_url = run_command(f'gh pr create --title "{pr_title}" --body "{pr_body}"')
        
        # Add the ready-to-comment label
        run_command(f'gh pr edit --add-label "ready-to-comment"')
        
        print(f"\n✅ Successfully created weblog review PR!")
        print(f"PR URL: {pr_url}")
        print(f"\n📝 Next steps:")
        print(f"1. Open the PR and review the archive content")
        print(f"2. Add line comments on specific quotes you want to reference")
        print(f"3. Add general PR comments for overall thoughts")  
        print(f"4. Approve the PR to trigger weblog creation")
        print(f"\n🤖 The weblog will be automatically generated and merged when you approve.")
        
    except Exception as e:
        print(f"Error occurred: {e}")
        print("Cleaning up...")
        # Switch back to main and delete the branch
        run_command("git checkout main")
        run_command(f"git branch -D {branch_name}", check=False)
        run_command(f"git push origin --delete {branch_name}", check=False)
        sys.exit(1)
    
    # Switch back to main
    run_command("git checkout main")

if __name__ == "__main__":
    main()
