#!/usr/bin/env python3
"""
Development Repository Setup Utility
Helps initialize and configure Git repositories with best practices
"""

import os
import subprocess
import sys
from datetime import datetime

def create_gitignore():
    """Create a comprehensive .gitignore file"""
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*.pyo
*.pyd
.Python
env/
venv/
.env

# Node.js
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# IDE
.vscode/
.idea/
*.swp
*.swo

# System
.DS_Store
Thumbs.db

# Logs
*.log
"""
    
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content)
    print("✓ Created .gitignore")

def create_readme_template(project_name):
    """Create a README template"""
    readme_content = f"""# {project_name}

## Description
Brief description of the project.

## Features
- Feature 1
- Feature 2
- Feature 3

## Installation
```bash
git clone https://github.com/yourusername/{project_name}.git
cd {project_name}
# Installation steps
