# Link Archive State Machine Documentation

## Overview

The link archive system implements a GitHub Actions-based state machine that processes URLs into archive entries and then generates weblog posts based on PR review comments.

## State Machine Flow

```mermaid
stateDiagram-v2
    [*] --> URL_Submitted: GitHub Issue with URL
    URL_Submitted --> Processing: Workflow triggered
    Processing --> Archive_Created: Success
    Processing --> Failed: Error
    
    Archive_Created --> PR_Created: Create PR
    PR_Created --> Validation: validate-and-review.yml
    
    Validation --> Ready_For_Review: Validation passes
    Validation --> PR_Closed: Validation fails
    
    Ready_For_Review --> Reviewing: Owner reviews
    Reviewing --> Approved: PR approved
    Reviewing --> Changes_Requested: Changes requested
    
    Approved --> Weblog_Generation: create-weblog.yml
    Weblog_Generation --> Weblog_Created: Success
    Weblog_Generation --> Failed: Error
    
    Weblog_Created --> Merged: PR auto-merged
    
    Failed --> [*]: Manual intervention
    PR_Closed --> [*]: End
    Changes_Requested --> Ready_For_Review: After fixes
    Merged --> [*]: Complete
```

## States and Transitions

### 1. URL Submission
- **Entry**: GitHub issue created with `URL: <url>` format
- **Trigger**: `process-url-to-pr.yml` workflow
- **Outputs**: 
  - Success → Archive file created
  - Failure → Error comment on issue

### 2. Archive Processing (`archive_processor.py`)
- **Validates**: URL format and accessibility
- **Checks**: Existing archive entries (6-month window)
- **Creates**: `YYYY-MM-DD-slugified-title.md` file
- **Required fields**: title, tags, link, date, description
- **Error handling**:
  - Missing API keys → Clear error message
  - Invalid URL → Validation error
  - Existing entry → Reports existing file

### 3. PR Creation and Validation
- **Creates**: Feature branch with archive file
- **Triggers**: `validate-and-review.yml`
- **Validation** (`archive_validator.py`):
  - File location (must be in `archive/`)
  - Filename format (`YYYY-MM-DD-*.md`)
  - YAML frontmatter structure
  - Required `link` field with valid URL
- **State markers**:
  - Success → `ready-to-comment` label added
  - Failure → PR closed with comment

### 4. Review State
- **Label**: `ready-to-comment`
- **Actions**: Owner can add line-specific comments
- **Transitions**:
  - Approved → Triggers weblog creation
  - Changes requested → Back to review after fixes

### 5. Weblog Generation (`weblog_processor.py`)
- **Trigger**: PR approval with `ready-to-comment` label
- **Processes**:
  - Extracts review comments (line-specific and general)
  - Quotes full paragraphs for line comments
  - Filters out generic approvals (LGTM, etc.)
- **Creates**: Weblog entry with:
  - All archive frontmatter fields
  - `type: weblog` marker
  - Link back to archive entry
  - Quoted content with commentary
- **Error handling**:
  - Invalid frontmatter → ValueError
  - JSON parsing errors → Logged to stderr

### 6. Final Validation and Merge
- **Validation** (`weblog_validator.py`):
  - Required fields: title, date, link, type
  - Date format: YYYY-MM-DD
  - Link format: `archive/*`
  - Content requirements: 50+ chars, "Archive:" reference
- **Success**: Auto-merge with squash commit
- **Failure**: Process stops, manual intervention needed

## Failure States and Recovery

### Clear Failure Indicators
1. **Processing failures**: Error comment on original issue with workflow logs link
2. **Validation failures**: PR closed with specific error message
3. **Weblog generation failures**: stderr output, exit code 1
4. **All Python scripts**: Exit code 1 on any error

### Retry Mechanisms
1. **URL Processing**: 
   - Can re-trigger workflow from issue
   - Cleanup handled automatically on failure
   
2. **Archive Validation**:
   - Fix issues and push to branch
   - Validation re-runs on push
   
3. **Weblog Creation**:
   - Can re-approve PR after fixing issues
   - Comments preserved for retry

### Manual Intervention Points
1. **Missing API keys**: Set in GitHub secrets or .env file
2. **Validation errors**: Fix file format/content
3. **Review required**: Owner must review and approve
4. **Merge conflicts**: Resolve manually