#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "feedparser",
#     "python-dateutil",
# ]
# ///
"""Check RSS feeds and output URLs for processing."""

import json
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import feedparser
from dateutil import parser as date_parser


def parse_entry_date(entry):
    """Parse date from RSS entry."""
    # Try structured date fields first
    for field in ['published_parsed', 'updated_parsed', 'created_parsed']:
        if hasattr(entry, field) and getattr(entry, field):
            try:
                return datetime.fromtimestamp(time.mktime(getattr(entry, field)), tz=timezone.utc)
            except (ValueError, TypeError, OverflowError):
                continue

    # Try string date fields
    for field in ['published', 'updated', 'created']:
        if hasattr(entry, field) and getattr(entry, field):
            try:
                parsed = date_parser.parse(getattr(entry, field))
                if parsed.tzinfo is None:
                    parsed = parsed.replace(tzinfo=timezone.utc)
                return parsed
            except (ValueError, TypeError):
                continue

    return None


def main():
    # Parse command line args
    hours_back = 7  # Default to 7 hours
    if len(sys.argv) > 1:
        try:
            hours_back = int(sys.argv[1])
        except ValueError:
            pass

    # Calculate cutoff time
    cutoff = datetime.now(timezone.utc) - timedelta(hours=hours_back)

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

    print(f"Checking {len(feeds)} RSS feeds for items from last {hours_back} hours...", file=sys.stderr)

    # Collect items from all feeds
    items = []
    for feed_url in feeds:
        try:
            feed = feedparser.parse(feed_url)
            feed_title = feed.feed.get('title', feed_url.split('/')[2] if '/' in feed_url else 'Unknown')

            # Process entries
            for entry in feed.entries[:10]:  # Check more entries to find recent ones
                if entry.get('link'):
                    # Check if entry is recent
                    entry_date = parse_entry_date(entry)
                    if entry_date and entry_date > cutoff:
                        items.append({
                            'url': entry.get('link'),
                            'title': entry.get('title', 'Untitled'),
                            'source': feed_title
                        })
                        print(f"  ✓ {feed_title}: {entry.get('title', 'Untitled')[:60]}", file=sys.stderr)
        except Exception as e:
            print(f"Error processing {feed_url}: {e}", file=sys.stderr)

    # Output as JSON for the workflow
    print(json.dumps(items))


if __name__ == "__main__":
    main()