#!/bin/bash

# Get URL from clipboard
url=$(pbpaste)

# Retrieve token from Keychain
token=$(security find-generic-password -a "github-token" -s "github-api" -w)

# Configuration
GITHUB_OWNER = "mbrg"            # Replace with your GitHub username
GITHUB_REPO  = "link-archive"    # Replace with your repository name
WORKFLOW     = "receive-url.yml" # Replace with your workflow file name

# Make the API call to trigger workflow
curl -X POST \
  -H "Authorization: Bearer $token" \
  -H "Accept: application/vnd.github.v3+json" \
  -H "Content-Type: application/json" \
  -d "{
    \"ref\": \"main\",
    \"inputs\": {
      \"url\": \"$url\",
      \"source\": \"mac-shortcut\"
    }
  }" \
  "https://api.github.com/repos/$GITHUB_OWNER/$GITHUB_REPO/actions/workflows/$WORKFLOW/dispatches"

echo "URL sent to GitHub: $url"