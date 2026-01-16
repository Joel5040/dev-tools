# Development Tools Collection

A set of utilities for managing development projects and repositories.

## Tools Included

### 1. Repository Setup (`repo_setup.py`)
Automates Git repository initialization with best practices:
- Creates `.gitignore` with common exclusions
- Generates README template
- Sets up initial commit
- Guides through GitHub connection

### 2. Project Backup (`project_backup.sh`)
Creates timestamped backups of development projects:
- Excludes unnecessary files (node_modules, .git, etc.)
- Compresses projects into `.tar.gz` archives
- Supports individual or bulk backups

## Usage

### Repository Setup
```bash
python3 repo_setup.py
