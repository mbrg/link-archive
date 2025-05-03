# Personal Link Archive

GitHub-based system for archiving and preserving web links that you find valuable. It helps combat [link rot](https://en.wikipedia.org/wiki/Link_rot) by creating permanent, searchable archives of web content you want to remember.

## How It Works

1. Run the "Process URL" workflow with the URL you want to archive
2. The system automatically:
   - Fetches the content
   - Processes it using AI
   - Creates a structured markdown file
   - Opens a pull request with the archived content
   - Review and merge the PR to add the content to your archive

## Setup

1. Fork this repository
2. Set up the following secrets in your repository:
   - `OPENAI_API_KEY`: Your OpenAI API key for content processing
   - `FIRECRAWL_API_KEY`: Your Firecrawl API key for web scraping