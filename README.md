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

## Workflow Chain

The system has multiple entry points that all funnel through the same core workflow:

### Entry Points

1. **External Webhooks** → External systems (Slack, etc.) send webhook to `message-webhook.yml`
2. **Mobile/Desktop Shortcuts** → iOS/macOS shortcuts trigger `receive-url.yml` directly

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
                                                │ validate-and-review│
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
                                                │  create-linklog    │
                                                │ Creates Linklog +  │
                                                │   Merges Both      │
                                                └────────────────────┘
```

### Trigger Details

- **`message-webhook.yml`** - Triggered by `repository_dispatch` events with type `message_received`
- **`receive-url.yml`** - Triggered by `workflow_dispatch` (manual) or called from message webhook
- **`process-url-to-pr.yml`** - Triggered by `workflow_dispatch` or called from receive-url
- **`validate-and-review.yml`** - Triggered by `workflow_dispatch`, called from process-url-to-pr (closes PR on validation errors)
- **`create-linklog.yml`** - Triggered by `pull_request_review` when approved with `archive-review` label

### Commentary System

1. Archive PR created with content for review
2. You comment on specific lines to quote full paragraphs in linklog
3. General PR comments become "Additional Thoughts" 
4. On approval: linklog auto-generated with quoted content + your commentary
5. Both archive and linklog validated before merge

## Setup

1. Fork this repository
2. Add repository secrets:
   - `OPENAI_API_KEY` - For content processing
   - `FIRECRAWL_API_KEY` - For web scraping