---
date: '2025-08-09'
description: Vercel's `markdown-to-markdown-sanitizer` is a new tool for sanitizing
  Markdown content, focused on preventing unexpected URLs in images and links. It
  processes input Markdown through a structured pipeline—parsing with `remark`, sanitizing
  HTML using `DOMPurify`, and converting back to Markdown with `turndown`. Key security
  features include strict URL allow-lists, XSS prevention via entity encoding, and
  configurable input length limits for DoS protection. While users can configure origins
  and prefixes, the output sacrifices some readability for enhanced security, making
  it ideal for rendering rather than direct human consumption.
link: https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer
tags:
- security
- sanitization
- html
- typescript
- markdown
title: markdown-sanitizers/markdown-to-markdown-sanitizer at main · vercel/markdown-sanitizers
  · GitHub
---

[Skip to content](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer#start-of-content)

[vercel](https://github.com/vercel)/ **[markdown-sanitizers](https://github.com/vercel/markdown-sanitizers)** Public

- [Notifications](https://github.com/login?return_to=%2Fvercel%2Fmarkdown-sanitizers) You must be signed in to change notification settings
- [Fork\\
0](https://github.com/login?return_to=%2Fvercel%2Fmarkdown-sanitizers)
- [Star\\
38](https://github.com/login?return_to=%2Fvercel%2Fmarkdown-sanitizers)


## Collapse file tree

## Files

main

Search this repository

/

# markdown-to-markdown-sanitizer

/

Copy path

## Directory actions

## More options

More options

## Directory actions

## More options

More options

## Latest commit

[![cramforce](https://avatars.githubusercontent.com/u/89679?v=4&size=40)](https://github.com/cramforce)[cramforce](https://github.com/vercel/markdown-sanitizers/commits?author=cramforce)

[Update README.md](https://github.com/vercel/markdown-sanitizers/commit/875e5c7a601799416d5316ae89ca67957742adfd)

Aug 5, 2025

[875e5c7](https://github.com/vercel/markdown-sanitizers/commit/875e5c7a601799416d5316ae89ca67957742adfd) · Aug 5, 2025

## History

[History](https://github.com/vercel/markdown-sanitizers/commits/main/markdown-to-markdown-sanitizer)

Open commit details

[View commit history for this file.](https://github.com/vercel/markdown-sanitizers/commits/main/markdown-to-markdown-sanitizer)

/

# markdown-to-markdown-sanitizer

/

Top

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| ### parent directory<br> [..](https://github.com/vercel/markdown-sanitizers/tree/main) |
| [src](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer/src "src") | [src](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer/src "src") | [types](https://github.com/vercel/markdown-sanitizers/commit/807ddd7ffbb7c9b0870be2d35c523cb4bc93dd1f "types") | Aug 5, 2025 |
| [tests](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer/tests "tests") | [tests](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer/tests "tests") | [Remove features](https://github.com/vercel/markdown-sanitizers/commit/013524d168f1adcc69f475fd05c683f5b70ac4d0 "Remove features") | Aug 5, 2025 |
| [.eslintrc.js](https://github.com/vercel/markdown-sanitizers/blob/main/markdown-to-markdown-sanitizer/.eslintrc.js ".eslintrc.js") | [.eslintrc.js](https://github.com/vercel/markdown-sanitizers/blob/main/markdown-to-markdown-sanitizer/.eslintrc.js ".eslintrc.js") | [Markdown to markdown added](https://github.com/vercel/markdown-sanitizers/commit/99a33cc32a54dc3efe9784e662e7f9499f68471f "Markdown to markdown added") | Aug 2, 2025 |
| [.gitignore](https://github.com/vercel/markdown-sanitizers/blob/main/markdown-to-markdown-sanitizer/.gitignore ".gitignore") | [.gitignore](https://github.com/vercel/markdown-sanitizers/blob/main/markdown-to-markdown-sanitizer/.gitignore ".gitignore") | [Markdown to markdown added](https://github.com/vercel/markdown-sanitizers/commit/99a33cc32a54dc3efe9784e662e7f9499f68471f "Markdown to markdown added") | Aug 2, 2025 |
| [.npmignore](https://github.com/vercel/markdown-sanitizers/blob/main/markdown-to-markdown-sanitizer/.npmignore ".npmignore") | [.npmignore](https://github.com/vercel/markdown-sanitizers/blob/main/markdown-to-markdown-sanitizer/.npmignore ".npmignore") | [Markdown to markdown added](https://github.com/vercel/markdown-sanitizers/commit/99a33cc32a54dc3efe9784e662e7f9499f68471f "Markdown to markdown added") | Aug 2, 2025 |
| [CLAUDE.md](https://github.com/vercel/markdown-sanitizers/blob/main/markdown-to-markdown-sanitizer/CLAUDE.md "CLAUDE.md") | [CLAUDE.md](https://github.com/vercel/markdown-sanitizers/blob/main/markdown-to-markdown-sanitizer/CLAUDE.md "CLAUDE.md") | [Remove features](https://github.com/vercel/markdown-sanitizers/commit/013524d168f1adcc69f475fd05c683f5b70ac4d0 "Remove features") | Aug 5, 2025 |
| [LICENSE](https://github.com/vercel/markdown-sanitizers/blob/main/markdown-to-markdown-sanitizer/LICENSE "LICENSE") | [LICENSE](https://github.com/vercel/markdown-sanitizers/blob/main/markdown-to-markdown-sanitizer/LICENSE "LICENSE") | [docs](https://github.com/vercel/markdown-sanitizers/commit/e555d680ed18e6d143e6eef2af73f678a0a127fc "docs") | Aug 5, 2025 |
| [README.md](https://github.com/vercel/markdown-sanitizers/blob/main/markdown-to-markdown-sanitizer/README.md "README.md") | [README.md](https://github.com/vercel/markdown-sanitizers/blob/main/markdown-to-markdown-sanitizer/README.md "README.md") | [Update README.md](https://github.com/vercel/markdown-sanitizers/commit/875e5c7a601799416d5316ae89ca67957742adfd "Update README.md") | Aug 5, 2025 |
| [TESTING.md](https://github.com/vercel/markdown-sanitizers/blob/main/markdown-to-markdown-sanitizer/TESTING.md "TESTING.md") | [TESTING.md](https://github.com/vercel/markdown-sanitizers/blob/main/markdown-to-markdown-sanitizer/TESTING.md "TESTING.md") | [Markdown to markdown added](https://github.com/vercel/markdown-sanitizers/commit/99a33cc32a54dc3efe9784e662e7f9499f68471f "Markdown to markdown added") | Aug 2, 2025 |
| [package.json](https://github.com/vercel/markdown-sanitizers/blob/main/markdown-to-markdown-sanitizer/package.json "package.json") | [package.json](https://github.com/vercel/markdown-sanitizers/blob/main/markdown-to-markdown-sanitizer/package.json "package.json") | [version](https://github.com/vercel/markdown-sanitizers/commit/0878fc962141bebfbece786ae69bb77d6c33d128 "version") | Aug 5, 2025 |
| [pnpm-lock.yaml](https://github.com/vercel/markdown-sanitizers/blob/main/markdown-to-markdown-sanitizer/pnpm-lock.yaml "pnpm-lock.yaml") | [pnpm-lock.yaml](https://github.com/vercel/markdown-sanitizers/blob/main/markdown-to-markdown-sanitizer/pnpm-lock.yaml "pnpm-lock.yaml") | [working](https://github.com/vercel/markdown-sanitizers/commit/4983ec8b829203719556871255de9a6d09fbf4f9 "working") | Aug 4, 2025 |
| [tsconfig.json](https://github.com/vercel/markdown-sanitizers/blob/main/markdown-to-markdown-sanitizer/tsconfig.json "tsconfig.json") | [tsconfig.json](https://github.com/vercel/markdown-sanitizers/blob/main/markdown-to-markdown-sanitizer/tsconfig.json "tsconfig.json") | [Markdown to markdown added](https://github.com/vercel/markdown-sanitizers/commit/99a33cc32a54dc3efe9784e662e7f9499f68471f "Markdown to markdown added") | Aug 2, 2025 |
| [tsconfig.test.json](https://github.com/vercel/markdown-sanitizers/blob/main/markdown-to-markdown-sanitizer/tsconfig.test.json "tsconfig.test.json") | [tsconfig.test.json](https://github.com/vercel/markdown-sanitizers/blob/main/markdown-to-markdown-sanitizer/tsconfig.test.json "tsconfig.test.json") | [Markdown to markdown added](https://github.com/vercel/markdown-sanitizers/commit/99a33cc32a54dc3efe9784e662e7f9499f68471f "Markdown to markdown added") | Aug 2, 2025 |
| [vitest.config.ts](https://github.com/vercel/markdown-sanitizers/blob/main/markdown-to-markdown-sanitizer/vitest.config.ts "vitest.config.ts") | [vitest.config.ts](https://github.com/vercel/markdown-sanitizers/blob/main/markdown-to-markdown-sanitizer/vitest.config.ts "vitest.config.ts") | [Markdown to markdown added](https://github.com/vercel/markdown-sanitizers/commit/99a33cc32a54dc3efe9784e662e7f9499f68471f "Markdown to markdown added") | Aug 2, 2025 |
| View all files |

## [README.md](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer\#readme)

Outline

# Markdown to Markdown Sanitizer

[Permalink: Markdown to Markdown Sanitizer](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer#markdown-to-markdown-sanitizer)

A robust markdown sanitizer focused on avoiding unexpected image and link URLs in markdown.

Note: This is brand new software and comes without security guarantees. Do your own testing for
your own use case.

The sanitizer consumes markdown and produces markdown output. Generally speaking, this is
less secure than sanitizing the final rendered output such as the generated HTML. Hence, this
package should only be used when the markdown is rendered by a third-party such as GitHub
or GitLab.

The primary use-case for this package is to [sanitize AI-generated markdown which may have\\
been subject to prompt-injection with the goal of exfiltrating data](https://vercel.com/blog/building-secure-ai-agents).

Note: The output of the sanitizer is designed to be unambiguous in terms of markdown parsing.
This comes at the trade-off of reduced human readability of the generated markdown. Hence,
it is only recommended to use this package when the markdown is meant to be rendered to an
output format such as HTML, rather than being directly consumed by humans.

## Why is markdown-to-markdown sanitization hard?

[Permalink: Why is markdown-to-markdown sanitization hard?](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer#why-is-markdown-to-markdown-sanitization-hard)

Markdown parsing substantially differs between implementations. Hence the parsed representation
that may appear valid with one parser, may not be valid with another.

The way this package tests whether it is doing a good job is:

- Tests in `tests/bypass-attempts/*.md`
- Sanitize with this package
- Use a range of markdown renderers to turn the sanitized markdown to HTML
  - `remark`
  - `marked`
  - `markdown-it`
  - `showdown`
  - `commonmark`
- Render the HTML output and check if it is secure

## How it works

[Permalink: How it works](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer#how-it-works)

The current implementation is quite involved. Simpler implementations may be possible, but the interleaved
markdown and HTML nature makes this quite hard.

Current steps:

- Parse input markdown with `remark`
- Render to HTML
- Use `DOMPurify` to sanitize the HTML according to the input rules
- Use `turndown` to re-create the markdown
- Escape all characters in text that are markdown control characters as HTML-entities

The last step is causing the reduced readability of the output (see trade-off documented above)
but it robustly avoids parsing ambiguities Backslash-based escaping has proven to lead to parsing
ambiguities between implementations.

## Features

[Permalink: Features](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer#features)

- **URL Sanitization**: Filters `href` and `src` attributes against configurable prefix allow-lists
- **HTML Sanitization**: DOMPurify-based HTML sanitization with GitHub-compatible allow-lists
- **Entity Encoding**: Aggressive HTML entity encoding for dangerous characters to prevent XSS
- **Length Limits**: Configurable maximum markdown length for DoS protection
- **TypeScript Support**: Full TypeScript definitions included

## Installation

[Permalink: Installation](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer#installation)

```
npm install markdown-to-markdown-sanitizer
```

## Basic Usage

[Permalink: Basic Usage](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer#basic-usage)

```
import { sanitizeMarkdown } from "markdown-to-markdown-sanitizer";

const options = {
  defaultOrigin: "https://example.com",
  allowedLinkPrefixes: ["https://example.com", "https://trusted-site.org"],
  allowedImagePrefixes: ["https://example.com/images"],
};

const input = `
# My Document

Check out this [safe link](https://example.com/page) and this [unsafe link](https://malicious.com/page).

![Safe image](https://example.com/images/photo.png)
![Unsafe image](https://malicious.com/image.png)
`;

const sanitized = sanitizeMarkdown(input, options);
console.log(sanitized);
// Output:
// # My Document
//
// Check out this [safe link](https://example.com/page) and this [unsafe link](#).
//
// ![Safe image](https://example.com/images/photo.png)
// ![Unsafe image]()
```

## Configuration Options

[Permalink: Configuration Options](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer#configuration-options)

### SanitizeOptions

[Permalink: SanitizeOptions](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer#sanitizeoptions)

```
interface SanitizeOptions {
  /**
   * Default origin for relative URLs (e.g., "https://github.com")
   * Required if your content contains relative URLs that should be allowed.
   */
  defaultOrigin: string;

  /** Allowed URL prefixes for links (href attributes) */
  allowedLinkPrefixes?: string[];

  /** Allowed URL prefixes for images (src attributes) */
  allowedImagePrefixes?: string[];

  /**
   * Default origin specifically for relative links
   * (overrides defaultOrigin if set)
   */
  defaultLinkOrigin?: string;

  /**
   * Default origin specifically for relative images
   * (overrides defaultOrigin if set)
   */
  defaultImageOrigin?: string;

  /**
   * Maximum length of URLs to be sanitized.
   * Default is 200 characters. 0 means no limit.
   */
  urlMaxLength?: number;

  /**
   * Maximum length of markdown content to process.
   * Default is 100000 characters. 0 means no limit.
   */
  maxMarkdownLength?: number;
}
```

## HTML Sanitization

[Permalink: HTML Sanitization](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer#html-sanitization)

The sanitizer uses DOMPurify with GitHub-compatible allow-lists for HTML elements and attributes:

### Allowed HTML Elements

[Permalink: Allowed HTML Elements](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer#allowed-html-elements)

**Text Formatting:**

- `strong`, `b`, `em`, `i`, `code`, `pre`, `tt`
- `s`, `strike`, `del`, `ins`, `mark`
- `sub`, `sup` (subscript and superscript)

**Structure:**

- `h1`, `h2`, `h3`, `h4`, `h5`, `h6` (headers)
- `p`, `blockquote`, `q` (paragraphs and quotes)
- `br`, `hr` (line breaks and horizontal rules)

**Lists:**

- `ul`, `ol`, `li` (with `start`, `reversed`, `value` attributes)
- `dl`, `dt`, `dd` (definition lists)

**Links and Media:**

- `a` (with `href`, `name`, `id`, `title`, `target` attributes)
- `img` (with `src`, `alt`, `title`, `width`, `height`, `align` attributes)

**Code and Technical:**

- `pre`, `code`, `samp`, `kbd`, `var`

**Tables:**

- `table`, `thead`, `tbody`, `tfoot`, `tr`, `td`, `th`
- Table attributes: `colspan`, `rowspan`, `align`, `valign`

**GitHub-Specific:**

- `details`, `summary` (with `open` attribute)
- `div`, `span` (with `class`, `id`, `dir` attributes)
- `ruby`, `rt`, `rp` (East Asian typography)

### Security Features

[Permalink: Security Features](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer#security-features)

- **URL Validation**: All URLs in `href` and `src` are validated against allow-lists
- **ID Prefixing**: User-generated `id` and `name` attributes are prefixed with `user-content-`
- **Entity Encoding**: Dangerous characters are encoded as HTML entities
- **XSS Prevention**: Scripts, event handlers, and dangerous elements are removed

## Advanced Usage

[Permalink: Advanced Usage](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer#advanced-usage)

### URL Prefix Configuration

[Permalink: URL Prefix Configuration](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer#url-prefix-configuration)

The sanitizer supports flexible URL prefix matching:

```
// Protocol-only prefixes
const options1 = {
  defaultOrigin: "https://example.com",
  allowedLinkPrefixes: ["https:", "http:"], // Allow any HTTPS or HTTP URL
};

// Domain prefixes
const options2 = {
  defaultOrigin: "https://example.com",
  allowedLinkPrefixes: ["https://example.com", "https://api.example.com"],
};

// Path prefixes
const options3 = {
  defaultOrigin: "https://example.com",
  allowedLinkPrefixes: ["https://example.com/docs", "https://example.com/api"],
};
```

### Length Limits

[Permalink: Length Limits](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer#length-limits)

Configure maximum markdown length to prevent DoS attacks:

```
const options = {
  defaultOrigin: "https://example.com",
  allowedLinkPrefixes: ["https://example.com"],
  maxMarkdownLength: 50000, // Limit to 50k characters
  urlMaxLength: 500, // Limit URL length to 500 characters
};

// Content over the limit will be truncated before processing
const longContent = "a".repeat(60000);
const result = sanitizeMarkdown(longContent, options);
// Result will be based on truncated content (first 50k chars)
```

## Processing Pipeline

[Permalink: Processing Pipeline](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer#processing-pipeline)

The sanitizer follows a multi-step pipeline to ensure security:

1. **Autolink Normalization**: Converts `<url>` syntax to `[url](url)` and rejects URLs with HTML entities
2. **Markdown → HTML**: Uses unified/remark to parse markdown and convert to HTML
3. **HTML Sanitization**: Uses DOMPurify with GitHub-compatible allow-lists
4. **HTML → Markdown**: Uses Turndown with GFM plugin to convert back to markdown
5. **Entity Encoding**: Encodes dangerous characters as HTML entities

## Security Considerations

[Permalink: Security Considerations](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer#security-considerations)

### Best Practices

[Permalink: Best Practices](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer#best-practices)

1. **Always specify `defaultOrigin`** \- Required for relative URL handling
2. **Use HTTPS prefixes** in your allow-lists when possible
3. **Be specific with prefixes** \- Avoid overly broad matches
4. **Set appropriate length limits** for your use case
5. **Test with untrusted input** to ensure your configuration is secure

### Entity Encoding

[Permalink: Entity Encoding](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer#entity-encoding)

The sanitizer aggressively encodes dangerous characters to prevent XSS:

- Characters encoded: `<>&"'[]:()/!\`
- Encoding format: `&{hex};` (e.g., `<` becomes `&3c;`)
- Applied to all text containing dangerous characters

## Performance

[Permalink: Performance](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer#performance)

- **Configurable length limits** to prevent DoS attacks
- **Efficient HTML processing** using DOMPurify
- **Optimized markdown parsing** using unified ecosystem

## Testing

[Permalink: Testing](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer#testing)

The package includes comprehensive test coverage:

- 800+ total tests including:
  - Core sanitization functionality
  - HTML sanitization with DOMPurify
  - Security attack prevention
  - Edge cases and malformed input
  - Length limit configuration
  - 555 bypass attempt tests

Run tests:

```
# Run all tests
pnpm test

# Run specific test file
pnpm test -- tests/basic-sanitization.test.ts

```

## Dependencies

[Permalink: Dependencies](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer#dependencies)

- **unified ecosystem**: Markdown parsing and processing
- **DOMPurify**: HTML sanitization
- **Turndown**: HTML to Markdown conversion
- **JSDOM**: DOM implementation for Node.js

## License

[Permalink: License](https://github.com/vercel/markdown-sanitizers/tree/main/markdown-to-markdown-sanitizer#license)

MIT
