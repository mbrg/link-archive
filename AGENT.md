# Link Archive Agent Guide

## Commands
- **Test scripts**: `uv run --script src/processors/url_processor.py <url> <dir> <model>` - Process a URL and create archive
- **Validate archive**: `uv run --script src/processors/frontmatter_validator.py <dir>` - Validate archive file frontmatter
- **Validate weblog**: `uv run --script src/processors/weblog_validator.py <dir>` - Validate weblog entries
- **Create weblog**: `uv run --script src/processors/weblog_processor.py <archive_file> <comments_json>` - Generate weblog from archive + PR comments
- **Trigger workflow**: Use GitHub "Process URL" workflow with issue number containing `URL: <url>`

## Architecture
- **Main workflow**: `.github/workflows/process-url-to-pr.yml` - Automated URL processing and PR creation
- **Archive storage**: `archive/` - Markdown files with YAML frontmatter, dated filenames

- **Weblog entries**: `weblog/` - Final published entries with your commentary
- **Core processors**: `src/processors/` - Python scripts using uv for dependency management
  - `url_processor.py` - Process URLs into archive entries
  - `weblog_processor.py` - Convert archive files + PR comments into weblog entries
  - `frontmatter_validator.py` - Validate archive file structure
  - `weblog_validator.py` - Validate weblog entry structure
- **Commentary workflow**: Review archive PRs directly with line comments
- **Maintenance tools**: `tools/` - Administrative scripts for repo maintenance
- **External APIs**: Firecrawl (scraping), OpenAI (summarization), requires API keys in secrets
- **Triggers**: iOS/macOS shortcuts in `triggers/` for mobile/desktop URL submission

## Code Style
- **Python**: Use uv script headers for dependencies, Python 3.12+, type hints
- **Filenames**: `YYYY-MM-DD-slugified-title.md` format for archive files
- **YAML frontmatter**: title, tags (array), link, date, summary fields required
- **Environment**: Load from .env file, fallback to environment variables
- **Error handling**: Validate URLs, check API keys, graceful failures with GitHub comments
- **Git workflow**: Feature branches, automated PRs, validation before merge
