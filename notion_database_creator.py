#!/usr/bin/env python3
"""
Notion Learning Tracker Database Creator
Automatically creates all databases for the learning management system
"""

import os
from notion_client import Client
from dotenv import load_dotenv
import json

# Load environment variables
load_dotenv()

# Initialize Notion client
notion = Client(auth=os.environ["NOTION_TOKEN"])
PARENT_PAGE_ID = os.environ["NOTION_PARENT_PAGE_ID"]

def create_learning_modules_database():
    """Create the Learning Modules database with all properties"""

    properties = {
        "Module Name": {"title": {}},
        "Category": {
            "select": {
                "options": [
                    {"name": "Backend Development", "color": "blue"},
                    {"name": "Database Management", "color": "green"},
                    {"name": "System Design", "color": "purple"},
                    {"name": "Algorithms & Data Structures", "color": "orange"},
                    {"name": "AI/ML Development", "color": "red"},
                    {"name": "DevOps & Infrastructure", "color": "yellow"},
                    {"name": "Design Patterns", "color": "gray"}
                ]
            }
        },
        "Phase": {
            "select": {
                "options": [
                    {"name": "Phase 1 (Months 1-3)", "color": "blue"},
                    {"name": "Phase 2 (Months 4-6)", "color": "green"},
                    {"name": "Phase 3 (Months 3-5)", "color": "orange"},
                    {"name": "Phase 4 (Months 6-12)", "color": "red"}
                ]
            }
        },
        "Status": {
            "select": {
                "options": [
                    {"name": "Not Started", "color": "gray"},
                    {"name": "In Progress", "color": "yellow"},
                    {"name": "Completed", "color": "green"},
                    {"name": "On Hold", "color": "orange"},
                    {"name": "Archived", "color": "red"}
                ]
            }
        },
        "Priority Level": {
            "select": {
                "options": [
                    {"name": "Critical", "color": "red"},
                    {"name": "High", "color": "orange"},
                    {"name": "Medium", "color": "yellow"},
                    {"name": "Low", "color": "gray"}
                ]
            }
        },
        "Estimated Hours": {"number": {"format": "number"}},
        "Actual Hours": {"number": {"format": "number"}},
        "Progress %": {
            "formula": {
                "expression": "if(prop(\"Estimated Hours\") > 0, round(prop(\"Actual Hours\") / prop(\"Estimated Hours\") * 100), 0)"
            }
        },
        "Start Date": {"date": {}},
        "Target Completion": {"date": {}},
        "Actual Completion": {"date": {}},
        "Skills Gained": {
            "multi_select": {
                "options": [
                    {"name": "API Design", "color": "blue"},
                    {"name": "Database Optimization", "color": "green"},
                    {"name": "System Architecture", "color": "purple"},
                    {"name": "Algorithm Analysis", "color": "orange"},
                    {"name": "Machine Learning", "color": "red"},
                    {"name": "Cloud Infrastructure", "color": "yellow"},
                    {"name": "Code Quality", "color": "gray"}
                ]
            }
        },
        "Notes": {"rich_text": {}}
    }

    try:
        response = notion.databases.create(
            parent={"type": "page_id", "page_id": PARENT_PAGE_ID},
            title=[{"type": "text", "text": {"content": "Learning Modules"}}],
            properties=properties
        )
        print("✅ Learning Modules database created successfully!")
        return response["id"]
    except Exception as e:
        print(f"❌ Error creating Learning Modules database: {e}")
        return None

def create_resources_library_database():
    """Create the Resources Library database with all properties"""

    properties = {
        "Resource Name": {"title": {}},
        "Type": {
            "select": {
                "options": [
                    {"name": "Book", "color": "blue"},
                    {"name": "Online Course", "color": "green"},
                    {"name": "Video Tutorial", "color": "orange"},
                    {"name": "Article/Blog", "color": "yellow"},
                    {"name": "Documentation", "color": "gray"},
                    {"name": "Interactive Platform", "color": "purple"},
                    {"name": "Podcast", "color": "red"}
                ]
            }
        },
        "Provider": {
            "select": {
                "options": [
                    {"name": "Udemy", "color": "purple"},
                    {"name": "Coursera", "color": "blue"},
                    {"name": "Pluralsight", "color": "orange"},
                    {"name": "YouTube", "color": "red"},
                    {"name": "Book Publisher", "color": "gray"},
                    {"name": "Official Documentation", "color": "green"},
                    {"name": "Blog/Medium", "color": "yellow"}
                ]
            }
        },
        "Status": {
            "select": {
                "options": [
                    {"name": "To Read/Watch", "color": "gray"},
                    {"name": "In Progress", "color": "yellow"},
                    {"name": "Completed", "color": "green"},
                    {"name": "Reference Only", "color": "blue"},
                    {"name": "Abandoned", "color": "red"}
                ]
            }
        },
        "Priority": {
            "select": {
                "options": [
                    {"name": "Must Read", "color": "red"},
                    {"name": "High Value", "color": "orange"},
                    {"name": "Useful", "color": "yellow"},
                    {"name": "Nice to Have", "color": "gray"}
                ]
            }
        },
        "Difficulty Level": {
            "select": {
                "options": [
                    {"name": "Beginner", "color": "green"},
                    {"name": "Intermediate", "color": "yellow"},
                    {"name": "Advanced", "color": "orange"},
                    {"name": "Expert", "color": "red"}
                ]
            }
        },
        "Rating": {
            "select": {
                "options": [
                    {"name": "⭐⭐⭐⭐⭐", "color": "green"},
                    {"name": "⭐⭐⭐⭐", "color": "yellow"},
                    {"name": "⭐⭐⭐", "color": "orange"},
                    {"name": "⭐⭐", "color": "red"},
                    {"name": "⭐", "color": "gray"}
                ]
            }
        },
        "URL": {"url": {}},
        "Cost": {
            "select": {
                "options": [
                    {"name": "Free", "color": "green"},
                    {"name": "Paid", "color": "orange"},
                    {"name": "Subscription", "color": "red"}
                ]
            }
        },
        "Estimated Time": {"rich_text": {}},
        "Key Takeaways": {"rich_text": {}},
        "Practical Applications": {"rich_text": {}},
        "Review Notes": {"rich_text": {}},
        "Date Added": {"created_time": {}},
        "Last Updated": {"last_edited_time": {}}
    }

    try:
        response = notion.databases.create(
            parent={"type": "page_id", "page_id": PARENT_PAGE_ID},
            title=[{"type": "text", "text": {"content": "Resources Library"}}],
            properties=properties
        )
        print("✅ Resources Library database created successfully!")
        return response["id"]
    except Exception as e:
        print(f"❌ Error creating Resources Library database: {e}")
        return None

def create_projects_portfolio_database():
    """Create the Projects Portfolio database with all properties"""

    properties = {
        "Project Name": {"title": {}},
        "Project Type": {
            "select": {
                "options": [
                    {"name": "Backend API", "color": "blue"},
                    {"name": "Full-Stack Application", "color": "green"},
                    {"name": "System Design Implementation", "color": "purple"},
                    {"name": "AI/ML Application", "color": "red"},
                    {"name": "Algorithm Implementation", "color": "orange"},
                    {"name": "DevOps/Infrastructure", "color": "yellow"},
                    {"name": "Learning Exercise", "color": "gray"}
                ]
            }
        },
        "Status": {
            "select": {
                "options": [
                    {"name": "Planning", "color": "gray"},
                    {"name": "In Development", "color": "yellow"},
                    {"name": "Testing", "color": "orange"},
                    {"name": "Completed", "color": "green"},
                    {"name": "Deployed", "color": "blue"},
                    {"name": "Archived", "color": "red"}
                ]
            }
        },
        "Complexity": {
            "select": {
                "options": [
                    {"name": "Simple", "color": "green"},
                    {"name": "Moderate", "color": "yellow"},
                    {"name": "Complex", "color": "orange"},
                    {"name": "Advanced", "color": "red"}
                ]
            }
        },
        "Technologies Used": {
            "multi_select": {
                "options": [
                    {"name": "React", "color": "blue"},
                    {"name": "Next.js", "color": "gray"},
                    {"name": "TypeScript", "color": "blue"},
                    {"name": "Node.js", "color": "green"},
                    {"name": "Python", "color": "yellow"},
                    {"name": "FastAPI", "color": "green"},
                    {"name": "PostgreSQL", "color": "blue"},
                    {"name": "Redis", "color": "red"},
                    {"name": "Docker", "color": "blue"},
                    {"name": "AWS", "color": "orange"},
                    {"name": "GraphQL", "color": "purple"},
                    {"name": "Machine Learning", "color": "red"}
                ]
            }
        },
        "GitHub Repository": {"url": {}},
        "Live Demo": {"url": {}},
        "Start Date": {"date": {}},
        "Completion Date": {"date": {}},
        "Time Invested": {"number": {"format": "number"}},
        "Project Description": {"rich_text": {}},
        "Key Features": {"rich_text": {}},
        "Technical Challenges": {"rich_text": {}},
        "Lessons Learned": {"rich_text": {}},
        "Next Steps/Improvements": {"rich_text": {}},
        "Portfolio Worthy": {"checkbox": {}}
    }

    try:
        response = notion.databases.create(
            parent={"type": "page_id", "page_id": PARENT_PAGE_ID},
            title=[{"type": "text", "text": {"content": "Projects Portfolio"}}],
            properties=properties
        )
        print("✅ Projects Portfolio database created successfully!")
        return response["id"]
    except Exception as e:
        print(f"❌ Error creating Projects Portfolio database: {e}")
        return None

def create_weekly_reflections_database():
    """Create the Weekly Reflections database with all properties"""

    properties = {
        "Week Of": {"title": {}},
        "Week Start Date": {"date": {}},
        "Total Study Hours": {"number": {"format": "number"}},
        "Study Goal Hours": {"number": {"format": "number"}},
        "Goal Achievement": {
            "formula": {
                "expression": "if(prop(\"Study Goal Hours\") > 0, round(prop(\"Total Study Hours\") / prop(\"Study Goal Hours\") * 100), 0)"
            }
        },
        "Focus Areas": {
            "multi_select": {
                "options": [
                    {"name": "Backend Development", "color": "blue"},
                    {"name": "Database Skills", "color": "green"},
                    {"name": "System Design", "color": "purple"},
                    {"name": "Algorithms", "color": "orange"},
                    {"name": "AI/ML", "color": "red"},
                    {"name": "Project Work", "color": "yellow"},
                    {"name": "Reading", "color": "gray"}
                ]
            }
        },
        "Concepts Learned": {"rich_text": {}},
        "Challenges Faced": {"rich_text": {}},
        "Breakthrough Moments": {"rich_text": {}},
        "Overall Confidence": {
            "select": {
                "options": [
                    {"name": "Very Confident", "color": "green"},
                    {"name": "Confident", "color": "yellow"},
                    {"name": "Neutral", "color": "gray"},
                    {"name": "Need Improvement", "color": "orange"},
                    {"name": "Struggling", "color": "red"}
                ]
            }
        },
        "Backend Confidence": {
            "select": {
                "options": [
                    {"name": "5 - Expert", "color": "green"},
                    {"name": "4 - Advanced", "color": "yellow"},
                    {"name": "3 - Intermediate", "color": "gray"},
                    {"name": "2 - Beginner", "color": "orange"},
                    {"name": "1 - Learning", "color": "red"}
                ]
            }
        },
        "Database Confidence": {
            "select": {
                "options": [
                    {"name": "5 - Expert", "color": "green"},
                    {"name": "4 - Advanced", "color": "yellow"},
                    {"name": "3 - Intermediate", "color": "gray"},
                    {"name": "2 - Beginner", "color": "orange"},
                    {"name": "1 - Learning", "color": "red"}
                ]
            }
        },
        "System Design Confidence": {
            "select": {
                "options": [
                    {"name": "5 - Expert", "color": "green"},
                    {"name": "4 - Advanced", "color": "yellow"},
                    {"name": "3 - Intermediate", "color": "gray"},
                    {"name": "2 - Beginner", "color": "orange"},
                    {"name": "1 - Learning", "color": "red"}
                ]
            }
        },
        "AI/ML Confidence": {
            "select": {
                "options": [
                    {"name": "5 - Expert", "color": "green"},
                    {"name": "4 - Advanced", "color": "yellow"},
                    {"name": "3 - Intermediate", "color": "gray"},
                    {"name": "2 - Beginner", "color": "orange"},
                    {"name": "1 - Learning", "color": "red"}
                ]
            }
        },
        "Goals for Next Week": {"rich_text": {}},
        "Action Items": {"rich_text": {}}
    }

    try:
        response = notion.databases.create(
            parent={"type": "page_id", "page_id": PARENT_PAGE_ID},
            title=[{"type": "text", "text": {"content": "Weekly Reflections"}}],
            properties=properties
        )
        print("✅ Weekly Reflections database created successfully!")
        return response["id"]
    except Exception as e:
        print(f"❌ Error creating Weekly Reflections database: {e}")
        return None

def setup_database_relations(learning_modules_id, resources_library_id, projects_portfolio_id, weekly_reflections_id):
    """Add relation properties between databases"""

    # Add relations to Learning Modules
    try:
        notion.databases.update(
            database_id=learning_modules_id,
            properties={
                "Related Resources": {
                    "relation": {"database_id": resources_library_id}
                },
                "Related Projects": {
                    "relation": {"database_id": projects_portfolio_id}
                }
            }
        )
        print("✅ Learning Modules relations added!")
    except Exception as e:
        print(f"❌ Error adding Learning Modules relations: {e}")

    # Add relations to Resources Library
    try:
        notion.databases.update(
            database_id=resources_library_id,
            properties={
                "Module Links": {
                    "relation": {"database_id": learning_modules_id}
                }
            }
        )
        print("✅ Resources Library relations added!")
    except Exception as e:
        print(f"❌ Error adding Resources Library relations: {e}")

    # Add relations to Projects Portfolio
    try:
        notion.databases.update(
            database_id=projects_portfolio_id,
            properties={
                "Skills Applied": {
                    "relation": {"database_id": learning_modules_id}
                }
            }
        )
        print("✅ Projects Portfolio relations added!")
    except Exception as e:
        print(f"❌ Error adding Projects Portfolio relations: {e}")

    # Add relations to Weekly Reflections
    try:
        notion.databases.update(
            database_id=weekly_reflections_id,
            properties={
                "Resources Used": {
                    "relation": {"database_id": resources_library_id}
                },
                "Projects Worked On": {
                    "relation": {"database_id": projects_portfolio_id}
                }
            }
        )
        print("✅ Weekly Reflections relations added!")
    except Exception as e:
        print(f"❌ Error adding Weekly Reflections relations: {e}")

def main():
    """Main function to create all databases and relations"""
    print("🚀 Starting Notion Learning Tracker Database Creation...")
    print("=" * 60)

    # Create databases
    learning_modules_id = create_learning_modules_database()
    resources_library_id = create_resources_library_database()
    projects_portfolio_id = create_projects_portfolio_database()
    weekly_reflections_id = create_weekly_reflections_database()

    # Check if all databases were created successfully
    if all([learning_modules_id, resources_library_id, projects_portfolio_id, weekly_reflections_id]):
        print("\n🔗 Setting up database relations...")
        setup_database_relations(learning_modules_id, resources_library_id, projects_portfolio_id, weekly_reflections_id)

        # Save database IDs for future scripts
        database_ids = {
            "learning_modules": learning_modules_id,
            "resources_library": resources_library_id,
            "projects_portfolio": projects_portfolio_id,
            "weekly_reflections": weekly_reflections_id
        }

        with open("database_ids.json", "w") as f:
            json.dump(database_ids, f, indent=2)

        print("\n🎉 All databases created successfully!")
        print("📋 Database IDs saved to 'database_ids.json'")
        print("\nNext steps:")
        print("1. Run 'python notion_data_populator.py' to add sample data")
        print("2. Run 'python notion_dashboard_creator.py' to create dashboard pages")
    else:
        print("\n❌ Some databases failed to create. Please check the errors above.")

if __name__ == "__main__":
    main()