# Archive URLs Shortcut for iPhone

This repository contains the [Archive URLs.shortcut](/triggers/iphone/Archive%20URLs.shortcut) file, an iOS Shortcut designed to help you quickly archive web URLs to your GitHub repository using the GitHub app.

## Features
- Accepts input from Safari web pages and URLs via the Share Sheet or Quick Actions.
- If no input is provided, it will use the clipboard contents.
- Extracts URLs from the input or clipboard text.
- For each URL found, it triggers a GitHub Actions workflow (`receive-url.yml`) in the `link-archive` repository.
    - Make sure you change the details to point to your repo!
- The workflow receives a dictionary with the URL and a source identifier (`iphone-shortcut`).

## Requirements
- **GitHub app for iOS**: [Download from the App Store](https://apps.apple.com/il/app/github/id1477376905)
- A GitHub account with access to the `link-archive` repository and permissions to dispatch workflows.

## How to Use
1. Install the GitHub app from the link above and sign in.
2. Add the `Archive URLs.shortcut` to your Shortcuts app.
3. Share a web page or URL from Safari (or copy a URL to your clipboard) and run the shortcut.
4. The shortcut will extract URLs and send them to your GitHub repository for archiving.