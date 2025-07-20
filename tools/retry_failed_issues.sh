#!/bin/bash

# Script to retry failed URL processing on open issues
# Uses gh CLI to trigger the Process URL workflow one by one

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if gh CLI is installed and authenticated
if ! command -v gh &> /dev/null; then
    print_error "gh CLI is not installed. Please install it first: https://cli.github.com/"
    exit 1
fi

# Check if authenticated
if ! gh auth status &> /dev/null; then
    print_error "gh CLI is not authenticated. Please run: gh auth login"
    exit 1
fi

print_status "Fetching open issues..."

# Get all open issues with URLs in the body
# Filter out PDFs and only process issues that contain "URL:" lines
ISSUES=$(gh issue list --state open --limit 1000 --json number,body --jq '.[] | select(.body | test("URL:.*"; "i")) | select(.body | test("\\.pdf"; "i") | not) | .number')

if [ -z "$ISSUES" ]; then
    print_warning "No open issues found with URLs (excluding PDFs)"
    exit 0
fi

# Count total issues
TOTAL_ISSUES=$(echo "$ISSUES" | wc -l | tr -d ' ')
print_status "Found $TOTAL_ISSUES open issues with URLs to process"

# Process each issue one by one
COUNTER=1
for ISSUE_NUMBER in $ISSUES; do
    print_status "Processing issue #$ISSUE_NUMBER ($COUNTER/$TOTAL_ISSUES)..."
    
    # Get the issue body to extract URL for logging
    ISSUE_BODY=$(gh issue view "$ISSUE_NUMBER" --json body --jq '.body')
    URL=$(echo "$ISSUE_BODY" | grep -m 1 '^URL:' | sed 's/^URL: //' | tr -d '\r' || echo "Unknown URL")
    
    print_status "  URL: $URL"
    
    # Trigger the workflow
    if gh workflow run "process-url-to-pr.yml" --field issue_number="$ISSUE_NUMBER"; then
        print_status "  ✓ Workflow triggered successfully for issue #$ISSUE_NUMBER"
    else
        print_error "  ✗ Failed to trigger workflow for issue #$ISSUE_NUMBER"
    fi
    
    # Wait 30 seconds between triggers to avoid overloading
    if [ $COUNTER -lt $TOTAL_ISSUES ]; then
        print_status "  Waiting 30 seconds before next trigger..."
        sleep 30
    fi
    
    COUNTER=$((COUNTER + 1))
done

print_status "Completed processing all $TOTAL_ISSUES issues"
print_warning "Monitor the Actions tab to see workflow progress: https://github.com/$(gh repo view --json owner,name --jq '.owner.login + "/" + .name')/actions"
