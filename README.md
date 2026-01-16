# Development Tools Collection

A set of utilities developed to streamline DevOps workflows and automate development processes.

## Tools Included

### 1. Repository Setup (`repo_setup.py`)
Automates Git repository initialization with DevOps best practices:
- Creates `.gitignore` with infrastructure-as-code exclusions
- Generates standardized README templates
- Sets up initial CI/CD-ready commits

### 2. Project Backup (`project_backup.sh`)
Creates timestamped backups of development projects with:
- Infrastructure state preservation
- Container image management
- Configuration versioning

## Purpose
These tools were developed as part of my DevOps transition journey, applying Quality Control principles of standardization and reproducibility to development workflows.

## Skills Demonstrated
- Infrastructure as Code principles
- Automation scripting (Python/Bash)
- Git operations and version control
- Process optimization from QC background

## DevOps Application
- **Standardization**: Applying QC batch consistency to deployment processes
- **Reproducibility**: Ensuring environment consistency across deployments
- **Documentation**: Maintaining precise records akin to QC compliance tracking

## Usage
\`\`\`bash
# Repository setup with DevOps standards
python3 repo_setup.py

# Infrastructure backup
chmod +x project_backup.sh
./project_backup.sh
\`\`\`

## License
MIT License
