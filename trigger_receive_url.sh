#!/bin/bash

# Script to trigger the Receive URL workflow for all URLs from the pickle file

URLS_FILE="urls.txt"
total_count=0
success_count=0

echo "Triggering Receive URL workflow for URLs from $URLS_FILE..."

# Count total URLs
total_count=$(wc -l < "$URLS_FILE")
echo "Found $total_count URLs to process"

# Process each URL
current=0
while IFS= read -r url; do
    current=$((current + 1))
    echo ""
    echo "[$current/$total_count] Triggering workflow for: $url"
    
    # Trigger the Receive URL workflow
    if gh workflow run receive-url.yml --field url="$url" --field source="mbgsec-linklog"; then
        echo "✓ Triggered Receive URL workflow for: $url"
        success_count=$((success_count + 1))
    else
        echo "✗ Failed to trigger workflow for: $url"
    fi
    
    # Wait 30 seconds between iterations (except for the last one)
    if [ $current -lt $total_count ]; then
        echo "Waiting 30 seconds before next URL..."
        sleep 30
    fi
    
done < "$URLS_FILE"

echo ""
echo "✓ Successfully triggered $success_count/$total_count workflows"
