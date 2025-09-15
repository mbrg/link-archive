#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "feedparser",
# ]
# ///
"""Check RSS feeds and output URLs for processing."""

import json
import sys
from pathlib import Path

import feedparser


def main():
    # Load feeds from file
    feeds_file = Path(__file__).parent / "feeds.txt"
    if not feeds_file.exists():
        print("Error: feeds.txt not found", file=sys.stderr)
        sys.exit(1)

    feeds = []
    for line in feeds_file.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            # Remove inline comments
            url = line.split('#')[0].strip()
            if url:
                feeds.append(url)

    if not feeds:
        print("No feeds found in feeds.txt", file=sys.stderr)
        sys.exit(0)

    print(f"Checking {len(feeds)} RSS feeds...", file=sys.stderr)

    # Collect items from all feeds
    items = []
    for feed_url in feeds:
        try:
            feed = feedparser.parse(feed_url)
            feed_title = feed.feed.get('title', feed_url.split('/')[2] if '/' in feed_url else 'Unknown')

            # Get top 3 items from each feed
            for entry in feed.entries[:3]:
                if entry.get('link'):
                    items.append({
                        'url': entry.get('link'),
                        'title': entry.get('title', 'Untitled'),
                        'source': feed_title
                    })
        except Exception as e:
            print(f"Error processing {feed_url}: {e}", file=sys.stderr)

    # Output as JSON for the workflow
    print(json.dumps(items))


if __name__ == "__main__":
    main()