# Personal Link Archive

Github-based system to archive web links you find valuable with a single tap.
Combat [link rot](https://en.wikipedia.org/wiki/Link_rot) by creating permanent, searchable archives.
Inspired by [Simon Willison's weblog](https://simonwillison.net/2024/Dec/22/link-blog/).

## Quick Start

**Mobile/Desktop shortcuts:**
- [iPhone shortcut](triggers/iphone/) - Archive from iOS
- [Mac shortcut](triggers/mac/) - Archive from macOS

**Manual:** Run the "Process URL" GitHub workflow with any URL

The system automatically fetches content, processes it with AI, and creates a pull request with structured markdown.

## Setup

1. Fork this repository
2. Add repository secrets:
   - `OPENAI_API_KEY` - For content processing
   - `FIRECRAWL_API_KEY` - For web scraping