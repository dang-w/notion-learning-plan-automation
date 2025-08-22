#!/usr/bin/env python3
"""
Notion Learning Tracker Dashboard Creator
Creates dashboard pages with embedded database views
"""

import os
import json
from notion_client import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Notion client
notion = Client(auth=os.environ["NOTION_TOKEN"])
PARENT_PAGE_ID = os.environ["NOTION_PARENT_PAGE_ID"]

# Load database IDs
with open("database_ids.json", "r") as f:
    database_ids = json.load(f)

def create_learning_dashboard():
    """Create the main learning dashboard page"""

    # Create the dashboard page
    dashboard_content = [
        {
            "object": "block",
            "type": "heading_1",
            "heading_1": {
                "rich_text": [{"type": "text", "text": {"content": "📚 Learning Progress Overview"}}]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": "Your comprehensive learning management dashboard - track progress, manage resources, and monitor your skill development journey."}}]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "🎯 Current Focus"}}]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": "Active learning modules and immediate priorities:"}}]
            }
        },
        {
            "object": "block",
            "type": "child_database",
            "child_database": {
                "title": "Current Phase Modules",
                "database_id": database_ids["learning_modules"]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "📖 Priority Resources"}}]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": "Must-read resources and high-value learning materials:"}}]
            }
        },
        {
            "object": "block",
            "type": "child_database",
            "child_database": {
                "title": "To Read/Watch",
                "database_id": database_ids["resources_library"]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "🚀 Active Projects"}}]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": "Current development projects and hands-on learning:"}}]
            }
        },
        {
            "object": "block",
            "type": "child_database",
            "child_database": {
                "title": "Current Projects",
                "database_id": database_ids["projects_portfolio"]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "📊 Quick Stats"}}]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {"type": "text", "text": {"content": "• Total Learning Modules: "}, "annotations": {"bold": True}},
                    {"type": "text", "text": {"content": "20 planned modules across 4 phases\n"}},
                    {"type": "text", "text": {"content": "• Resource Library: "}, "annotations": {"bold": True}},
                    {"type": "text", "text": {"content": "12 curated high-value resources\n"}},
                    {"type": "text", "text": {"content": "• Project Pipeline: "}, "annotations": {"bold": True}},
                    {"type": "text", "text": {"content": "4 progressive hands-on projects\n"}},
                    {"type": "text", "text": {"content": "• Study Goal: "}, "annotations": {"bold": True}},
                    {"type": "text", "text": {"content": "8 hours per week focused learning"}}
                ]
            }
        }
    ]

    try:
        response = notion.pages.create(
            parent={"type": "page_id", "page_id": PARENT_PAGE_ID},
            properties={
                "title": [{"type": "text", "text": {"content": "📚 Learning Dashboard"}}]
            },
            children=dashboard_content
        )
        print("✅ Learning Dashboard created successfully!")
        return response["id"]
    except Exception as e:
        print(f"❌ Error creating Learning Dashboard: {e}")
        return None

def create_progress_analytics():
    """Create the progress analytics dashboard"""

    analytics_content = [
        {
            "object": "block",
            "type": "heading_1",
            "heading_1": {
                "rich_text": [{"type": "text", "text": {"content": "📊 Progress Analytics"}}]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": "Track your learning progress, confidence levels, and study patterns over time."}}]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "📈 Weekly Reflections & Confidence Tracking"}}]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": "Monitor your confidence levels across different skill areas and track weekly progress:"}}]
            }
        },
        {
            "object": "block",
            "type": "child_database",
            "child_database": {
                "title": "Weekly Progress",
                "database_id": database_ids["weekly_reflections"]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "🎯 Module Progress by Category"}}]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": "See completion status across different learning categories:"}}]
            }
        },
        {
            "object": "block",
            "type": "child_database",
            "child_database": {
                "title": "Progress Tracker",
                "database_id": database_ids["learning_modules"]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "📚 Resource Utilization"}}]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": "Track your resource consumption and identify high-value materials:"}}]
            }
        },
        {
            "object": "block",
            "type": "child_database",
            "child_database": {
                "title": "Resource Status",
                "database_id": database_ids["resources_library"]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "💡 Learning Insights"}}]
            }
        },
        {
            "object": "block",
            "type": "callout",
            "callout": {
                "rich_text": [
                    {"type": "text", "text": {"content": "Analytics Tips:\n"}},
                    {"type": "text", "text": {"content": "• Update weekly reflections consistently for accurate trends\n"}},
                    {"type": "text", "text": {"content": "• Use confidence ratings to identify areas needing focus\n"}},
                    {"type": "text", "text": {"content": "• Track actual vs. estimated hours to improve planning\n"}},
                    {"type": "text", "text": {"content": "• Review breakthrough moments to reinforce learning patterns"}}
                ],
                "icon": {"emoji": "💡"}
            }
        }
    ]

    try:
        response = notion.pages.create(
            parent={"type": "page_id", "page_id": PARENT_PAGE_ID},
            properties={
                "title": [{"type": "text", "text": {"content": "📊 Progress Analytics"}}]
            },
            children=analytics_content
        )
        print("✅ Progress Analytics dashboard created successfully!")
        return response["id"]
    except Exception as e:
        print(f"❌ Error creating Progress Analytics dashboard: {e}")
        return None

def create_project_showcase():
    """Create the project portfolio showcase"""

    showcase_content = [
        {
            "object": "block",
            "type": "heading_1",
            "heading_1": {
                "rich_text": [{"type": "text", "text": {"content": "🚀 Project Portfolio"}}]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": "Showcase your hands-on projects and track practical application of your learning."}}]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "⭐ Portfolio-Worthy Projects"}}]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": "Your best projects ready for professional showcase:"}}]
            }
        },
        {
            "object": "block",
            "type": "child_database",
            "child_database": {
                "title": "Showcase Projects",
                "database_id": database_ids["projects_portfolio"]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "🔧 Current Development"}}]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": "Projects currently in development or testing phases:"}}]
            }
        },
        {
            "object": "block",
            "type": "child_database",
            "child_database": {
                "title": "Active Development",
                "database_id": database_ids["projects_portfolio"]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "🛠️ Technology Stack Overview"}}]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {"type": "text", "text": {"content": "Technologies you're building expertise in:\n\n"}},
                    {"type": "text", "text": {"content": "Backend: "}, "annotations": {"bold": True}},
                    {"type": "text", "text": {"content": "FastAPI, Node.js, Python, PostgreSQL, Redis\n"}},
                    {"type": "text", "text": {"content": "Frontend: "}, "annotations": {"bold": True}},
                    {"type": "text", "text": {"content": "React, Next.js, TypeScript, Tailwind CSS\n"}},
                    {"type": "text", "text": {"content": "AI/ML: "}, "annotations": {"bold": True}},
                    {"type": "text", "text": {"content": "LangChain, OpenAI API, Vector Databases\n"}},
                    {"type": "text", "text": {"content": "Infrastructure: "}, "annotations": {"bold": True}},
                    {"type": "text", "text": {"content": "Docker, AWS, Kubernetes, Monitoring Tools"}}
                ]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "📅 Project Timeline"}}]
            }
        },
        {
            "object": "block",
            "type": "callout",
            "callout": {
                "rich_text": [
                    {"type": "text", "text": {"content": "Months 1-3: "}, "annotations": {"bold": True}},
                    {"type": "text", "text": {"content": "Task Management API (Backend Mastery)\n"}},
                    {"type": "text", "text": {"content": "Months 4-6: "}, "annotations": {"bold": True}},
                    {"type": "text", "text": {"content": "Distributed Chat App (System Design)\n"}},
                    {"type": "text", "text": {"content": "Months 7-9: "}, "annotations": {"bold": True}},
                    {"type": "text", "text": {"content": "AI Code Review Assistant (AI Integration)\n"}},
                    {"type": "text", "text": {"content": "Months 10-12: "}, "annotations": {"bold": True}},
                    {"type": "text", "text": {"content": "AI Agent Marketplace (Full-Stack AI Platform)"}}
                ],
                "icon": {"emoji": "📅"}
            }
        }
    ]

    try:
        response = notion.pages.create(
            parent={"type": "page_id", "page_id": PARENT_PAGE_ID},
            properties={
                "title": [{"type": "text", "text": {"content": "🚀 Project Portfolio"}}]
            },
            children=showcase_content
        )
        print("✅ Project Portfolio showcase created successfully!")
        return response["id"]
    except Exception as e:
        print(f"❌ Error creating Project Portfolio showcase: {e}")
        return None

def create_main_navigation():
    """Update the main parent page with navigation to all dashboards"""

    navigation_content = [
        {
            "object": "block",
            "type": "heading_1",
            "heading_1": {
                "rich_text": [{"type": "text", "text": {"content": "🎓 Learning Management System"}}]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [{"type": "text", "text": {"content": "Welcome to your comprehensive learning tracker! This system helps you manage your journey from frontend expertise to full-stack senior engineer with backend, database, system design, and AI specialization."}}]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "🗺️ Navigation"}}]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {"type": "text", "text": {"content": "📚 "}, "annotations": {"bold": True}},
                    {"type": "text", "text": {"content": "Learning Dashboard"}, "annotations": {"bold": True}},
                    {"type": "text", "text": {"content": " - Your main hub for tracking current modules, priority resources, and active projects\n"}},
                    {"type": "text", "text": {"content": "📊 "}, "annotations": {"bold": True}},
                    {"type": "text", "text": {"content": "Progress Analytics"}, "annotations": {"bold": True}},
                    {"type": "text", "text": {"content": " - Analyze your learning trends, confidence levels, and study patterns\n"}},
                    {"type": "text", "text": {"content": "🚀 "}, "annotations": {"bold": True}},
                    {"type": "text", "text": {"content": "Project Portfolio"}, "annotations": {"bold": True}},
                    {"type": "text", "text": {"content": " - Showcase your hands-on projects and track practical skill application"}}
                ]
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "🎯 Learning Path Overview"}}]
            }
        },
        {
            "object": "block",
            "type": "callout",
            "callout": {
                "rich_text": [
                    {"type": "text", "text": {"content": "Phase 1 (Months 1-3): "}, "annotations": {"bold": True}},
                    {"type": "text", "text": {"content": "Backend & Database Fundamentals\n"}},
                    {"type": "text", "text": {"content": "Phase 2 (Months 4-6): "}, "annotations": {"bold": True}},
                    {"type": "text", "text": {"content": "System Design & Architecture\n"}},
                    {"type": "text", "text": {"content": "Phase 3 (Months 3-5): "}, "annotations": {"bold": True}},
                    {"type": "text", "text": {"content": "Algorithms & Data Structures\n"}},
                    {"type": "text", "text": {"content": "Phase 4 (Months 6-12): "}, "annotations": {"bold": True}},
                    {"type": "text", "text": {"content": "AI/ML & Emerging Technologies"}}
                ],
                "icon": {"emoji": "🎯"}
            }
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": "📋 Quick Actions"}}]
            }
        },
        {
            "object": "block",
            "type": "to_do",
            "to_do": {
                "rich_text": [{"type": "text", "text": {"content": "Complete weekly reflection"}}],
                "checked": False
            }
        },
        {
            "object": "block",
            "type": "to_do",
            "to_do": {
                "rich_text": [{"type": "text", "text": {"content": "Update current module progress"}}],
                "checked": False
            }
        },
        {
            "object": "block",
            "type": "to_do",
            "to_do": {
                "rich_text": [{"type": "text", "text": {"content": "Log today's study hours"}}],
                "checked": False
            }
        },
        {
            "object": "block",
            "type": "to_do",
            "to_do": {
                "rich_text": [{"type": "text", "text": {"content": "Review and rate completed resources"}}],
                "checked": False
            }
        }
    ]

    try:
        # Get the existing page to preserve any existing content
        page = notion.pages.retrieve(page_id=PARENT_PAGE_ID)

        # Append new content blocks
        for block in navigation_content:
            notion.blocks.children.append(
                block_id=PARENT_PAGE_ID,
                children=[block]
            )

        print("✅ Main navigation page updated successfully!")
        return True
    except Exception as e:
        print(f"❌ Error updating main navigation: {e}")
        return False

def main():
    """Main function to create all dashboard pages"""
    print("🎨 Starting Notion Dashboard Creation...")
    print("=" * 60)

    # Create dashboard pages
    dashboards_created = []

    # Create Learning Dashboard
    print("\n📚 Creating Learning Dashboard...")
    if create_learning_dashboard():
        dashboards_created.append("Learning Dashboard")

    # Create Progress Analytics
    print("\n📊 Creating Progress Analytics...")
    if create_progress_analytics():
        dashboards_created.append("Progress Analytics")

    # Create Project Showcase
    print("\n🚀 Creating Project Portfolio...")
    if create_project_showcase():
        dashboards_created.append("Project Portfolio")

    # Update main navigation
    print("\n🗺️ Updating main navigation...")
    if create_main_navigation():
        dashboards_created.append("Main Navigation")

    # Summary
    print(f"\n🎉 Dashboard creation completed!")
    print(f"📋 Created: {', '.join(dashboards_created)}")

    if len(dashboards_created) == 4:
        print("\n✅ All components successfully created!")
        print("\n🚀 Your Notion Learning Management System is ready!")
        print("\nNext steps:")
        print("1. Visit your main Learning Management System page in Notion")
        print("2. Explore the three dashboard pages")
        print("3. Start logging your first weekly reflection")
        print("4. Begin tracking your learning progress!")
    else:
        print(f"\n⚠️ Some components failed to create. Please check the errors above.")

if __name__ == "__main__":
    main()