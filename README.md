# Personal Link Archive

Github-based system to archive web links you find valuable with a single tap.
Combat [link rot](https://en.wikipedia.org/wiki/Link_rot) by creating permanent, searchable archives.
Inspired by [Simon Willison's weblog](https://simonwillison.net/2024/Dec/22/link-blog/).

## Quick Start

**Mobile/Desktop shortcuts:**
- [iPhone shortcut](triggers/iphone/) - Archive from iOS
- [Mac shortcut](triggers/mac/) - Archive from macOS

**Manual:** Use repository dispatch webhook or run workflows directly (for debugging)

The system automatically fetches content, processes it with AI, and creates a pull request with structured markdown.

### Setup

1. Fork this repository
2. Add repository secrets:
   - `OPENAI_API_KEY` - For content processing
   - `FIRECRAWL_API_KEY` - For web scraping

### Commentary System

1. Archive PR created with content for review
2. You comment on specific lines to quote full paragraphs in weblog
3. General PR comments become "Additional Thoughts" 
4. On approval: weblog auto-generated with quoted content + your commentary
5. Both archive and weblog validated before merge

## Workflow Chain

The system has multiple entry points that all funnel through the same core workflow:

### Complete Workflow Chain

```
┌─────────────────┐    ┌──────────────────┐    ┌────────────────────┐
│ External System │───▶│ message-webhook  │───▶│    receive-url     │
│ (Webhook)       │    │      .yml        │    │       .yml         │
└─────────────────┘    └──────────────────┘    └────────────────────┘
                                                          │
┌─────────────────┐                                       │
│ iPhone Shortcut │──────────────────────────────────────▶│
└─────────────────┘                                       │
                                                          │
┌─────────────────┐                                       │
│  Mac Shortcut   │──────────────────────────────────────▶│
└─────────────────┘                                       ▼
                              🤖 AUTOMATED FLOW           
                                                ┌────────────────────┐
                                                │   Creates Issue    │
                                                │   + Triggers       │
                                                │ process-url-to-pr  │
                                                └────────────────────┘
                                                           │
                                                           ▼
                                                ┌────────────────────┐
                                                │ process-url-to-pr  │
                                                │    Creates         │
                                                │   Archive PR       │
                                                └────────────────────┘
                                                           │
                                                           ▼
                                                ┌────────────────────┐
                                                │  archive-review    │
                                                │ Validates + Adds   │
                                                │   You as Reviewer  │
                                                └────────────────────┘
                                                         │        │
                                                      ✅ │        │ ❌
                               👤 MANUAL STEP           ▼        ▼
                                        ┌────────────────────┐ ┌─────────────────┐
                                        │   YOU REVIEW &     │ │ Closes PR on    │
                                        │ COMMENT ON ARCHIVE │ │ Validation Error│
                                        │     CONTENT        │ └─────────────────┘
                                        └────────────────────┘
                                                   │
                               🤖 AUTOMATED ON APPROVAL
                                                   ▼
                                                ┌────────────────────┐
                                                │  create-weblog     │
                                                │ Creates Weblog +   │
                                                │   Merges Both      │
                                                └────────────────────┘
```