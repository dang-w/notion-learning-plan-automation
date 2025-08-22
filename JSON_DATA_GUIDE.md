# JSON Data Structure Guide

This guide explains how to use and customize the JSON-based data structure for the Notion Learning Tracker.

## Overview

The system now uses JSON files to store all learning data, making it easier to:
- Add new modules, resources, and projects
- Modify existing data without editing Python code
- Share and version control your learning plan
- Validate data before importing to Notion

## Directory Structure

```
notion-setup/
├── data/
│   ├── learning_modules.json    # Learning modules and topics
│   ├── resources.json           # Books, courses, and materials
│   ├── projects.json            # Hands-on projects
│   └── schemas/                 # JSON validation schemas
│       ├── learning_module.schema.json
│       ├── resource.schema.json
│       └── project.schema.json
```

## Data Files

### 1. Learning Modules (`data/learning_modules.json`)

Defines the learning topics and modules you want to track.

**Structure:**
```json
{
  "modules": [
    {
      "id": "unique-module-id",
      "name": "Module Display Name",
      "category": "Backend Development",
      "phase": "Phase 1 (Months 1-3)",
      "priority": "High",
      "estimated_hours": 20,
      "skills": ["API Design", "System Architecture"],
      "notes": "Additional details about the module",
      "status": "Not Started"
    }
  ]
}
```

**Field Descriptions:**
- `id`: Unique identifier (required, use kebab-case)
- `name`: Display name for the module (required)
- `category`: One of: "Backend Development", "Database Management", "System Design", "Algorithms & Data Structures", "AI/ML Development", "Cloud Infrastructure", "DevOps"
- `phase`: Learning phase timeline (e.g., "Phase 1 (Months 1-3)")
- `priority`: One of: "Critical", "High", "Medium", "Low"
- `estimated_hours`: Estimated time to complete (number)
- `skills`: Array of skills covered
- `notes`: Additional information
- `status`: One of: "Not Started", "In Progress", "Completed", "On Hold"

### 2. Resources (`data/resources.json`)

Contains books, courses, and other learning materials.

**Structure:**
```json
{
  "resources": [
    {
      "id": "unique-resource-id",
      "name": "Resource Name",
      "type": "Book",
      "provider": "Publisher Name",
      "priority": "Must Read",
      "difficulty": "Intermediate",
      "cost": "Paid",
      "estimated_time": "30 hours",
      "url": "https://example.com",
      "notes": "Why this resource is valuable",
      "module_ids": ["module-id-1", "module-id-2"],
      "status": "Not Started",
      "rating": null
    }
  ]
}
```

**Field Descriptions:**
- `id`: Unique identifier (required)
- `name`: Resource name (required)
- `type`: One of: "Book", "Online Course", "Video Series", "Interactive Platform", "Documentation", "Tutorial", "Workshop", "Conference"
- `provider`: Publisher or platform name
- `priority`: One of: "Must Read", "Must Take", "Must Have", "High Value", "Good to Have", "Good Practice", "Reference", "Optional"
- `difficulty`: One of: "Beginner", "Intermediate", "Advanced", "Varied"
- `cost`: One of: "Free", "Paid", "Subscription", "Freemium"
- `estimated_time`: Time to complete (string)
- `url`: Link to resource (optional)
- `notes`: Additional information
- `module_ids`: Array of related module IDs
- `status`: One of: "Not Started", "In Progress", "Completed", "Reference"
- `rating`: Personal rating 1-5 (optional)

### 3. Projects (`data/projects.json`)

Defines hands-on projects to apply your learning.

**Structure:**
```json
{
  "projects": [
    {
      "id": "unique-project-id",
      "name": "Project Name",
      "description": "Project description",
      "phase": "Phase 1 (Months 1-3)",
      "timeline": "Months 1-3",
      "status": "Not Started",
      "technologies": ["FastAPI", "PostgreSQL"],
      "skills_applied": ["API Design", "Database Optimization"],
      "features": ["Key feature 1", "Key feature 2"],
      "github_link": null,
      "demo_link": null,
      "lessons_learned": [],
      "next_steps": []
    }
  ]
}
```

**Field Descriptions:**
- `id`: Unique identifier (required)
- `name`: Project name (required)
- `description`: Project description (required)
- `phase`: Learning phase this project belongs to
- `timeline`: Expected completion timeline
- `status`: One of: "Not Started", "Planning", "In Development", "Testing", "Completed", "Deployed", "Archived"
- `technologies`: Array of technologies used
- `skills_applied`: Array of skills practiced
- `features`: Array of key features
- `github_link`: GitHub repository URL (optional)
- `demo_link`: Live demo URL (optional)
- `lessons_learned`: Array of key learnings
- `next_steps`: Array of planned improvements

## Adding New Data

### Adding a New Module

1. Open `data/learning_modules.json`
2. Add a new object to the `modules` array:
```json
{
  "id": "my-new-module",
  "name": "My New Learning Module",
  "category": "Backend Development",
  "phase": "Phase 1 (Months 1-3)",
  "priority": "High",
  "estimated_hours": 25,
  "skills": ["New Skill"],
  "notes": "Description of what this module covers",
  "status": "Not Started"
}
```

### Adding a New Resource

1. Open `data/resources.json`
2. Add a new object to the `resources` array:
```json
{
  "id": "my-new-book",
  "name": "Amazing Tech Book",
  "type": "Book",
  "provider": "Tech Publisher",
  "priority": "Must Read",
  "difficulty": "Intermediate",
  "cost": "Paid",
  "estimated_time": "20 hours",
  "url": "https://book-website.com",
  "notes": "Great book for learning X",
  "module_ids": ["my-new-module"],
  "status": "Not Started",
  "rating": null
}
```

### Adding a New Project

1. Open `data/projects.json`
2. Add a new object to the `projects` array:
```json
{
  "id": "my-project",
  "name": "My Awesome Project",
  "description": "A project to practice new skills",
  "phase": "Phase 1 (Months 1-3)",
  "timeline": "Month 2",
  "status": "Planning",
  "technologies": ["Python", "Docker"],
  "skills_applied": ["Backend Development"],
  "features": ["REST API", "Database integration"],
  "github_link": null,
  "demo_link": null,
  "lessons_learned": [],
  "next_steps": ["Add authentication", "Deploy to cloud"]
}
```

## Validating Your Data

Before populating Notion, validate your JSON files:

```bash
python validate_data.py
```

This will:
- Check JSON syntax
- Validate against schemas
- Check for duplicate IDs
- Verify cross-references between modules and resources
- Test backward compatibility
- Provide warnings for data quality issues

## Populating Notion

After validation passes, populate your Notion databases:

```bash
python notion_data_populator.py
```

The script will:
- Read data from JSON files (or fall back to legacy if JSON not found)
- Create entries in your Notion databases
- Map relationships between modules, resources, and projects
- Set up proper formatting and colors

## Backward Compatibility

The system maintains backward compatibility:
- If JSON files are not found, it falls back to legacy hardcoded data
- Existing Notion dashboards continue to work without modification
- You can gradually migrate from the old system to JSON-based data

## Tips and Best Practices

1. **Use meaningful IDs**: Use kebab-case IDs that describe the content (e.g., `advanced-sql-optimization`)

2. **Maintain relationships**: When adding resources, link them to relevant modules using `module_ids`

3. **Regular validation**: Run `validate_data.py` after making changes to catch issues early

4. **Version control**: Commit your JSON files to track changes over time

5. **Incremental updates**: You can add new items without affecting existing data

6. **Custom categories**: To add new categories, update both the JSON files and the schema files

## Troubleshooting

### Validation Errors
- **Duplicate IDs**: Ensure all IDs within each file are unique
- **Invalid enum values**: Check that category, priority, and status values match the allowed options
- **Schema validation failures**: Ensure required fields are present and have correct types

### Import Errors
- **Missing environment variables**: Ensure `.env` file has `NOTION_TOKEN` and `NOTION_PARENT_PAGE_ID`
- **Database ID issues**: Run `notion_database_creator.py` first if databases don't exist
- **Permission errors**: Verify your Notion integration has access to the workspace

## Schema Customization

To add new fields or categories:

1. Update the relevant schema file in `data/schemas/`
2. Update the corresponding JSON data file
3. Modify `notion_data_populator.py` to handle the new fields
4. Run validation to ensure everything works

## Support

For issues or questions:
1. Check validation output for specific errors
2. Review this guide for proper data structure
3. Ensure all dependencies are installed: `pip install -r requirements.txt`
4. Verify Notion API credentials are correct