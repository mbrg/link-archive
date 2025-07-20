# Link Archive Agent Guide

## Commands
- **Test scripts**: `uv run --script scripts/archive/url_processor.py <url> <dir> <model>` - Process a URL and create archive
- **Validate**: `uv run --script scripts/archive/frontmatter_validator.py <dir>` - Validate archive file frontmatter
- **Trigger workflow**: Use GitHub "Process URL" workflow with issue number containing `URL: <url>`

## Architecture
- **Main workflow**: `.github/workflows/process-url-to-pr.yml` - Automated URL processing and PR creation
- **Archive storage**: `archive/` - Markdown files with YAML frontmatter, dated filenames
- **Processing scripts**: `scripts/archive/` - Python scripts using uv for dependency management
- **External APIs**: Firecrawl (scraping), OpenAI (summarization), requires API keys in secrets
- **Triggers**: iOS/macOS shortcuts in `triggers/` for mobile/desktop URL submission

## Code Style
- **Python**: Use uv script headers for dependencies, Python 3.12+, type hints
- **Filenames**: `YYYY-MM-DD-slugified-title.md` format for archive files
- **YAML frontmatter**: title, tags (array), link, date, summary fields required
- **Environment**: Load from .env file, fallback to environment variables
- **Error handling**: Validate URLs, check API keys, graceful failures with GitHub comments
- **Git workflow**: Feature branches, automated PRs, validation before merge
