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

## Usage

### Adding a New Link

1. Go to the Actions tab in your repository
2. Select "Process URL" workflow
3. Click "Run workflow"
4. Enter the URL you want to archive in the `issue_number` field (this will be used to generate a unique identifier)
5. Optionally customize:
   - `toreaddir`: Directory where articles are stored (default: `links`)
   - `model`: OpenAI model to use for summarization (default: `gpt-4o-mini`)
6. Click "Run workflow"
7. The system will create a PR with the archived content
8. Review and merge the PR to add the content to your archive

## Project Structure

- `links/`: Directory containing archived content
- `scripts/links/`: Processing scripts
  - `url_processor.py`: Main script for processing URLs
  - `frontmatter_validator.py`: Validates the structure of archived content

## Contributing

Feel free to open issues or pull requests to improve the system. Some potential areas for contribution:
- Adding support for different content types
- Improving the AI processing
- Enhancing the validation system

## License

This project is open source and available under the MIT License. 