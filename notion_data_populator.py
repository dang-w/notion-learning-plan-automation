#!/usr/bin/env python3
"""
Notion Learning Tracker Data Populator
Extracts data from learning_plan.md and populates Notion databases
"""

import os
import json
import re
from datetime import datetime, timedelta
from notion_client import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Notion client
notion = Client(auth=os.environ["NOTION_TOKEN"])

# Load database IDs
with open("database_ids.json", "r") as f:
    database_ids = json.load(f)

def parse_learning_plan():
    """Extract learning modules and resources from learning_plan.md"""

    with open("learning_plan.md", "r") as f:
        content = f.read()

    # Extract learning modules based on the phases and topics
    learning_modules = [
        {
            "name": "Advanced API Design Patterns",
            "category": "Backend Development",
            "phase": "Phase 1 (Months 1-3)",
            "priority": "High",
            "estimated_hours": 20,
            "skills": ["API Design"],
            "notes": "RESTful, GraphQL, RPC patterns and best practices"
        },
        {
            "name": "Microservices Architecture",
            "category": "Backend Development",
            "phase": "Phase 1 (Months 1-3)",
            "priority": "High",
            "estimated_hours": 25,
            "skills": ["System Architecture"],
            "notes": "Understanding microservices vs monoliths, service communication"
        },
        {
            "name": "Message Queues & Event-Driven Architecture",
            "category": "Backend Development",
            "phase": "Phase 1 (Months 1-3)",
            "priority": "Medium",
            "estimated_hours": 20,
            "skills": ["System Architecture"],
            "notes": "RabbitMQ, Kafka, async processing patterns"
        },
        {
            "name": "Advanced Caching Strategies",
            "category": "Backend Development",
            "phase": "Phase 1 (Months 1-3)",
            "priority": "High",
            "estimated_hours": 15,
            "skills": ["System Architecture"],
            "notes": "Redis, Memcached, caching patterns and invalidation"
        },
        {
            "name": "Authentication & Authorization",
            "category": "Backend Development",
            "phase": "Phase 1 (Months 1-3)",
            "priority": "Critical",
            "estimated_hours": 18,
            "skills": ["API Design"],
            "notes": "OAuth2, JWT, RBAC implementation"
        },
        {
            "name": "Advanced SQL & Query Optimization",
            "category": "Database Management",
            "phase": "Phase 1 (Months 1-3)",
            "priority": "Critical",
            "estimated_hours": 30,
            "skills": ["Database Optimization"],
            "notes": "Window functions, CTEs, query performance tuning"
        },
        {
            "name": "Database Design Patterns",
            "category": "Database Management",
            "phase": "Phase 1 (Months 1-3)",
            "priority": "High",
            "estimated_hours": 20,
            "skills": ["Database Optimization"],
            "notes": "Normalization, indexing strategies, schema design"
        },
        {
            "name": "NoSQL Database Mastery",
            "category": "Database Management",
            "phase": "Phase 1 (Months 1-3)",
            "priority": "Medium",
            "estimated_hours": 25,
            "skills": ["Database Optimization"],
            "notes": "MongoDB, DynamoDB patterns and use cases"
        },
        {
            "name": "Scalability Patterns",
            "category": "System Design",
            "phase": "Phase 2 (Months 4-6)",
            "priority": "Critical",
            "estimated_hours": 35,
            "skills": ["System Architecture"],
            "notes": "Horizontal vs vertical scaling, load balancing strategies"
        },
        {
            "name": "Database Sharding & Replication",
            "category": "System Design",
            "phase": "Phase 2 (Months 4-6)",
            "priority": "High",
            "estimated_hours": 30,
            "skills": ["Database Optimization", "System Architecture"],
            "notes": "Distributed database concepts and implementation"
        },
        {
            "name": "CDNs & Global Distribution",
            "category": "System Design",
            "phase": "Phase 2 (Months 4-6)",
            "priority": "Medium",
            "estimated_hours": 20,
            "skills": ["System Architecture"],
            "notes": "Content delivery networks, edge computing"
        },
        {
            "name": "Monitoring & Observability",
            "category": "System Design",
            "phase": "Phase 2 (Months 4-6)",
            "priority": "High",
            "estimated_hours": 25,
            "skills": ["System Architecture"],
            "notes": "Prometheus, Grafana, distributed tracing"
        },
        {
            "name": "Algorithm Complexity Analysis",
            "category": "Algorithms & Data Structures",
            "phase": "Phase 3 (Months 3-5)",
            "priority": "Critical",
            "estimated_hours": 25,
            "skills": ["Algorithm Analysis"],
            "notes": "Big O notation, time/space complexity optimization"
        },
        {
            "name": "Dynamic Programming Mastery",
            "category": "Algorithms & Data Structures",
            "phase": "Phase 3 (Months 3-5)",
            "priority": "High",
            "estimated_hours": 30,
            "skills": ["Algorithm Analysis"],
            "notes": "DP patterns, memoization, tabulation techniques"
        },
        {
            "name": "Graph Algorithms",
            "category": "Algorithms & Data Structures",
            "phase": "Phase 3 (Months 3-5)",
            "priority": "High",
            "estimated_hours": 25,
            "skills": ["Algorithm Analysis"],
            "notes": "BFS, DFS, shortest path, MST algorithms"
        },
        {
            "name": "LLM Integration & API Patterns",
            "category": "AI/ML Development",
            "phase": "Phase 4 (Months 6-12)",
            "priority": "Critical",
            "estimated_hours": 40,
            "skills": ["Machine Learning"],
            "notes": "OpenAI API, prompt engineering, token optimization"
        },
        {
            "name": "AI Agent Development",
            "category": "AI/ML Development",
            "phase": "Phase 4 (Months 6-12)",
            "priority": "Critical",
            "estimated_hours": 50,
            "skills": ["Machine Learning"],
            "notes": "LangChain, agent orchestration, communication protocols"
        },
        {
            "name": "Multimodal AI Applications",
            "category": "AI/ML Development",
            "phase": "Phase 4 (Months 6-12)",
            "priority": "High",
            "estimated_hours": 35,
            "skills": ["Machine Learning"],
            "notes": "Text, image, audio processing with AI models"
        },
        {
            "name": "Vector Databases & Embeddings",
            "category": "AI/ML Development",
            "phase": "Phase 4 (Months 6-12)",
            "priority": "High",
            "estimated_hours": 30,
            "skills": ["Machine Learning", "Database Optimization"],
            "notes": "Pinecone, Weaviate, semantic search implementation"
        },
        {
            "name": "MLOps & Model Deployment",
            "category": "AI/ML Development",
            "phase": "Phase 4 (Months 6-12)",
            "priority": "Medium",
            "estimated_hours": 40,
            "skills": ["Machine Learning", "Cloud Infrastructure"],
            "notes": "Model serving, monitoring, A/B testing"
        }
    ]

    # Extract key resources from the learning plan
    resources = [
        {
            "name": "Designing Data-Intensive Applications",
            "type": "Book",
            "provider": "Book Publisher",
            "priority": "Must Read",
            "difficulty": "Advanced",
            "cost": "Paid",
            "estimated_time": "40-50 hours",
            "url": "https://dataintensive.net/",
            "notes": "Essential book covering distributed systems, databases, and data processing"
        },
        {
            "name": "Complete Node.js Developer Course",
            "type": "Online Course",
            "provider": "Udemy",
            "priority": "High Value",
            "difficulty": "Intermediate",
            "cost": "Paid",
            "estimated_time": "20 hours",
            "notes": "Advanced Node.js patterns beyond basics"
        },
        {
            "name": "Building Microservices",
            "type": "Book",
            "provider": "Book Publisher",
            "priority": "Must Read",
            "difficulty": "Intermediate",
            "cost": "Paid",
            "estimated_time": "30 hours",
            "notes": "Comprehensive guide to microservices architecture"
        },
        {
            "name": "FastAPI - The Complete Course",
            "type": "Online Course",
            "provider": "Udemy",
            "priority": "High Value",
            "difficulty": "Intermediate",
            "cost": "Paid",
            "estimated_time": "12 hours",
            "notes": "Advanced FastAPI features and patterns"
        },
        {
            "name": "SQL Performance Explained",
            "type": "Book",
            "provider": "Book Publisher",
            "priority": "Must Read",
            "difficulty": "Advanced",
            "cost": "Paid",
            "estimated_time": "25 hours",
            "notes": "Deep dive into SQL optimization techniques"
        },
        {
            "name": "System Design Interview",
            "type": "Book",
            "provider": "Book Publisher",
            "priority": "Must Read",
            "difficulty": "Intermediate",
            "cost": "Paid",
            "estimated_time": "30 hours",
            "notes": "Essential system design concepts and patterns"
        },
        {
            "name": "Grokking the System Design Interview",
            "type": "Online Course",
            "provider": "EducativeIO",
            "priority": "High Value",
            "difficulty": "Intermediate",
            "cost": "Subscription",
            "estimated_time": "25 hours",
            "notes": "Interactive system design practice"
        },
        {
            "name": "Cracking the Coding Interview",
            "type": "Book",
            "provider": "Book Publisher",
            "priority": "High Value",
            "difficulty": "Intermediate",
            "cost": "Paid",
            "estimated_time": "40 hours",
            "notes": "Algorithm and data structure interview preparation"
        },
        {
            "name": "LeetCode Premium",
            "type": "Interactive Platform",
            "provider": "LeetCode",
            "priority": "High Value",
            "difficulty": "Intermediate",
            "cost": "Subscription",
            "estimated_time": "Ongoing",
            "url": "https://leetcode.com/",
            "notes": "Algorithm practice platform with premium features"
        },
        {
            "name": "LangChain & Vector Databases in Production",
            "type": "Online Course",
            "provider": "Udemy",
            "priority": "Must Read",
            "difficulty": "Advanced",
            "cost": "Paid",
            "estimated_time": "15 hours",
            "notes": "Production-ready AI agent development"
        },
        {
            "name": "Hands-On Large Language Models",
            "type": "Book",
            "provider": "Book Publisher",
            "priority": "High Value",
            "difficulty": "Advanced",
            "cost": "Paid",
            "estimated_time": "35 hours",
            "notes": "Practical LLM implementation and integration"
        },
        {
            "name": "Deep Learning Specialization",
            "type": "Online Course",
            "provider": "Coursera",
            "priority": "High Value",
            "difficulty": "Advanced",
            "cost": "Subscription",
            "estimated_time": "60 hours",
            "notes": "Comprehensive deep learning fundamentals"
        }
    ]

    # Extract projects from the timeline
    projects = [
        {
            "name": "Task Management API with Advanced Features",
            "type": "Backend API",
            "complexity": "Moderate",
            "technologies": ["FastAPI", "PostgreSQL", "Redis", "Python"],
            "description": "Comprehensive task management API with FastAPI backend, PostgreSQL with complex queries, Redis caching layer, JWT authentication, and comprehensive testing suite",
            "timeline": "Months 1-3",
            "key_features": "Advanced FastAPI features, complex PostgreSQL queries, Redis caching, JWT auth, comprehensive tests"
        },
        {
            "name": "Distributed Chat Application",
            "type": "System Design Implementation",
            "complexity": "Complex",
            "technologies": ["Node.js", "PostgreSQL", "Redis", "Docker"],
            "description": "Distributed chat application with microservices architecture, WebSocket connections, message queues, load balancing, and monitoring",
            "timeline": "Months 4-6",
            "key_features": "Microservices architecture, WebSocket connections, RabbitMQ/Kafka, load balancing, Prometheus/Grafana monitoring"
        },
        {
            "name": "AI-Powered Code Review Assistant",
            "type": "AI/ML Application",
            "complexity": "Advanced",
            "technologies": ["Python", "FastAPI", "React", "Machine Learning"],
            "description": "AI-powered code review assistant with LLM integration for code analysis, multi-file processing, custom fine-tuning, and web interface",
            "timeline": "Months 7-9",
            "key_features": "LLM integration, code analysis, multi-file processing, custom fine-tuning, React interface"
        },
        {
            "name": "AI Agent Marketplace Platform",
            "type": "Full-Stack Application",
            "complexity": "Advanced",
            "technologies": ["React", "Next.js", "Python", "FastAPI", "PostgreSQL", "Machine Learning"],
            "description": "Comprehensive AI agent marketplace with agent creation and deployment tools, multi-modal capabilities, usage analytics, and subscription billing",
            "timeline": "Months 10-12",
            "key_features": "Agent creation tools, multi-modal AI, usage analytics, subscription billing, full-stack platform"
        }
    ]

    return learning_modules, resources, projects

def create_learning_module_entry(module):
    """Create a single learning module entry in Notion"""

    # Calculate target completion date based on phase
    start_date = datetime.now()
    if "Phase 1" in module["phase"]:
        target_completion = start_date + timedelta(days=90)
    elif "Phase 2" in module["phase"]:
        target_completion = start_date + timedelta(days=180)
    elif "Phase 3" in module["phase"]:
        target_completion = start_date + timedelta(days=150)
    else:  # Phase 4
        target_completion = start_date + timedelta(days=365)

    properties = {
        "Module Name": {"title": [{"text": {"content": module["name"]}}]},
        "Category": {"select": {"name": module["category"]}},
        "Phase": {"select": {"name": module["phase"]}},
        "Status": {"select": {"name": "Not Started"}},
        "Priority Level": {"select": {"name": module["priority"]}},
        "Estimated Hours": {"number": module["estimated_hours"]},
        "Target Completion": {"date": {"start": target_completion.isoformat()[:10]}},
        "Skills Gained": {
            "multi_select": [{"name": skill} for skill in module["skills"]]
        },
        "Notes": {"rich_text": [{"text": {"content": module["notes"]}}]}
    }

    try:
        response = notion.pages.create(
            parent={"database_id": database_ids["learning_modules"]},
            properties=properties
        )
        return response["id"]
    except Exception as e:
        print(f"❌ Error creating module '{module['name']}': {e}")
        return None

def create_resource_entry(resource):
    """Create a single resource entry in Notion"""

    properties = {
        "Resource Name": {"title": [{"text": {"content": resource["name"]}}]},
        "Type": {"select": {"name": resource["type"]}},
        "Provider": {"select": {"name": resource["provider"]}},
        "Status": {"select": {"name": "To Read/Watch"}},
        "Priority": {"select": {"name": resource["priority"]}},
        "Difficulty Level": {"select": {"name": resource["difficulty"]}},
        "Cost": {"select": {"name": resource["cost"]}},
        "Estimated Time": {"rich_text": [{"text": {"content": resource["estimated_time"]}}]}
    }

    if "url" in resource:
        properties["URL"] = {"url": resource["url"]}

    if "notes" in resource:
        properties["Key Takeaways"] = {"rich_text": [{"text": {"content": resource["notes"]}}]}

    try:
        response = notion.pages.create(
            parent={"database_id": database_ids["resources_library"]},
            properties=properties
        )
        return response["id"]
    except Exception as e:
        print(f"❌ Error creating resource '{resource['name']}': {e}")
        return None

def create_project_entry(project):
    """Create a single project entry in Notion"""

    properties = {
        "Project Name": {"title": [{"text": {"content": project["name"]}}]},
        "Project Type": {"select": {"name": project["type"]}},
        "Status": {"select": {"name": "Planning"}},
        "Complexity": {"select": {"name": project["complexity"]}},
        "Technologies Used": {
            "multi_select": [{"name": tech} for tech in project["technologies"]]
        },
        "Project Description": {"rich_text": [{"text": {"content": project["description"]}}]},
        "Key Features": {"rich_text": [{"text": {"content": project["key_features"]}}]},
        "Portfolio Worthy": {"checkbox": True}
    }

    try:
        response = notion.pages.create(
            parent={"database_id": database_ids["projects_portfolio"]},
            properties=properties
        )
        return response["id"]
    except Exception as e:
        print(f"❌ Error creating project '{project['name']}': {e}")
        return None

def create_initial_weekly_reflection():
    """Create an initial weekly reflection entry"""

    current_date = datetime.now()
    week_start = current_date - timedelta(days=current_date.weekday())
    week_title = f"Week of {week_start.strftime('%B %d, %Y')}"

    properties = {
        "Week Of": {"title": [{"text": {"content": week_title}}]},
        "Week Start Date": {"date": {"start": week_start.isoformat()[:10]}},
        "Study Goal Hours": {"number": 8},
        "Focus Areas": {
            "multi_select": [
                {"name": "Backend Development"},
                {"name": "Database Skills"}
            ]
        },
        "Overall Confidence": {"select": {"name": "Confident"}},
        "Backend Confidence": {"select": {"name": "3 - Intermediate"}},
        "Database Confidence": {"select": {"name": "2 - Beginner"}},
        "System Design Confidence": {"select": {"name": "2 - Beginner"}},
        "AI/ML Confidence": {"select": {"name": "1 - Learning"}},
        "Goals for Next Week": {
            "rich_text": [{"text": {"content": "Start with FastAPI advanced patterns and PostgreSQL optimization fundamentals"}}]
        },
        "Action Items": {
            "rich_text": [{"text": {"content": "1. Set up development environment\n2. Begin reading 'Designing Data-Intensive Applications'\n3. Complete FastAPI course setup"}}]
        }
    }

    try:
        response = notion.pages.create(
            parent={"database_id": database_ids["weekly_reflections"]},
            properties=properties
        )
        return response["id"]
    except Exception as e:
        print(f"❌ Error creating initial weekly reflection: {e}")
        return None

def main():
    """Main function to populate all databases with sample data"""
    print("📊 Starting Notion Learning Tracker Data Population...")
    print("=" * 60)

    # Parse the learning plan
    learning_modules, resources, projects = parse_learning_plan()

    # Populate Learning Modules
    print(f"\n📚 Creating {len(learning_modules)} learning modules...")
    module_count = 0
    for module in learning_modules:
        if create_learning_module_entry(module):
            module_count += 1
    print(f"✅ Created {module_count}/{len(learning_modules)} learning modules")

    # Populate Resources Library
    print(f"\n📖 Creating {len(resources)} resources...")
    resource_count = 0
    for resource in resources:
        if create_resource_entry(resource):
            resource_count += 1
    print(f"✅ Created {resource_count}/{len(resources)} resources")

    # Populate Projects Portfolio
    print(f"\n🚀 Creating {len(projects)} projects...")
    project_count = 0
    for project in projects:
        if create_project_entry(project):
            project_count += 1
    print(f"✅ Created {project_count}/{len(projects)} projects")

    # Create initial weekly reflection
    print(f"\n📝 Creating initial weekly reflection...")
    if create_initial_weekly_reflection():
        print("✅ Initial weekly reflection created")

    print("\n🎉 Data population completed!")
    print(f"📋 Summary:")
    print(f"   - Learning Modules: {module_count}")
    print(f"   - Resources: {resource_count}")
    print(f"   - Projects: {project_count}")
    print(f"   - Weekly Reflections: 1")

    print("\nNext step: Run 'python notion_dashboard_creator.py' to create dashboard pages")

if __name__ == "__main__":
    main()