#!/usr/bin/env python3
"""
Notion Learning Tracker Data Populator
Reads data from JSON files and populates Notion databases
"""

import os
import json
from datetime import datetime, timedelta
from notion_client import Client
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()

# Initialize Notion client
notion = Client(auth=os.environ["NOTION_TOKEN"])

# Load database IDs
with open("database_ids.json", "r") as f:
    database_ids = json.load(f)

def load_json_data(filename):
    """Load data from a JSON file in the data directory"""
    data_path = Path("data") / filename
    
    # Fallback to legacy extraction if JSON files don't exist
    if not data_path.exists():
        print(f"⚠️ {filename} not found. Using legacy data extraction...")
        return None
    
    with open(data_path, "r") as f:
        return json.load(f)

def get_legacy_modules():
    """Legacy function to extract modules from learning_plan.md"""
    return [
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

def get_legacy_resources():
    """Legacy function to extract resources"""
    return [
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
            "priority": "Must Have",
            "difficulty": "Varied",
            "cost": "Subscription",
            "estimated_time": "Ongoing",
            "url": "https://leetcode.com",
            "notes": "Algorithm practice platform with company-specific questions"
        },
        {
            "name": "LangChain & Vector Databases in Production",
            "type": "Online Course",
            "provider": "Udemy",
            "priority": "Must Take",
            "difficulty": "Intermediate",
            "cost": "Paid",
            "estimated_time": "15 hours",
            "notes": "Production-ready LLM application development"
        },
        {
            "name": "Deep Learning Specialization",
            "type": "Online Course",
            "provider": "Coursera",
            "priority": "High Value",
            "difficulty": "Intermediate",
            "cost": "Subscription",
            "estimated_time": "60 hours",
            "notes": "Comprehensive deep learning fundamentals by Andrew Ng"
        },
        {
            "name": "Practical Deep Learning for Coders",
            "type": "Online Course",
            "provider": "Fast.ai",
            "priority": "High Value",
            "difficulty": "Intermediate",
            "cost": "Free",
            "estimated_time": "30 hours",
            "url": "https://course.fast.ai",
            "notes": "Practical approach to deep learning"
        }
    ]

def get_legacy_projects():
    """Legacy function to extract projects"""
    return [
        {
            "name": "Task Management API",
            "description": "Comprehensive task management API with advanced backend features",
            "timeline": "Months 1-3",
            "technologies": ["FastAPI", "PostgreSQL", "Redis", "JWT"],
            "skills_applied": ["API Design", "Database Optimization", "Authentication"],
            "github_link": "",
            "demo_link": "",
            "status": "Planning"
        },
        {
            "name": "Distributed Chat Application",
            "description": "Real-time chat system with microservices architecture",
            "timeline": "Months 4-6",
            "technologies": ["Node.js", "WebSocket", "RabbitMQ", "Kubernetes"],
            "skills_applied": ["System Architecture", "Real-time Communication", "Microservices"],
            "github_link": "",
            "demo_link": "",
            "status": "Not Started"
        },
        {
            "name": "AI-Powered Code Review Assistant",
            "description": "Intelligent code review tool using LLM integration",
            "timeline": "Months 7-9",
            "technologies": ["Python", "LangChain", "OpenAI API", "React"],
            "skills_applied": ["Machine Learning", "Full-Stack Development", "API Integration"],
            "github_link": "",
            "demo_link": "",
            "status": "Not Started"
        },
        {
            "name": "AI Agent Marketplace",
            "description": "Full-stack platform for AI agent creation and deployment",
            "timeline": "Months 10-12",
            "technologies": ["Next.js", "FastAPI", "LangGraph", "PostgreSQL", "Stripe"],
            "skills_applied": ["Full-Stack Development", "AI Development", "Payment Integration"],
            "github_link": "",
            "demo_link": "",
            "status": "Not Started"
        }
    ]

def parse_learning_plan():
    """Extract learning modules and resources from JSON files or fall back to legacy"""
    
    # Try to load from JSON files first
    modules_data = load_json_data("learning_modules.json")
    resources_data = load_json_data("resources.json")
    projects_data = load_json_data("projects.json")
    
    # Extract modules
    if modules_data:
        learning_modules = modules_data.get("modules", [])
    else:
        learning_modules = get_legacy_modules()
    
    # Extract resources
    if resources_data:
        resources = resources_data.get("resources", [])
    else:
        resources = get_legacy_resources()
    
    # Extract projects
    if projects_data:
        projects = projects_data.get("projects", [])
    else:
        projects = get_legacy_projects()
    
    return learning_modules, resources, projects

def populate_learning_modules(learning_modules):
    """Populate the Learning Modules database"""
    print(f"\n📚 Populating {len(learning_modules)} learning modules...")
    
    for module in learning_modules:
        # Convert skills list to multi-select format
        skills_options = []
        for skill in module.get("skills", []):
            skills_options.append({"name": skill})
        
        # Priority color mapping
        priority_colors = {
            "Critical": "red",
            "High": "orange",
            "Medium": "yellow",
            "Low": "gray"
        }
        
        # Status color mapping
        status_colors = {
            "Not Started": "gray",
            "In Progress": "blue",
            "Completed": "green",
            "On Hold": "yellow"
        }
        
        try:
            response = notion.pages.create(
                parent={"database_id": database_ids["learning_modules"]},
                properties={
                    "Module Name": {
                        "title": [{"text": {"content": module["name"]}}]
                    },
                    "Category": {
                        "select": {"name": module["category"]}
                    },
                    "Phase": {
                        "select": {"name": module.get("phase", "Phase 1 (Months 1-3)")}
                    },
                    "Status": {
                        "select": {
                            "name": module.get("status", "Not Started"),
                            "color": status_colors.get(module.get("status", "Not Started"), "gray")
                        }
                    },
                    "Priority Level": {
                        "select": {
                            "name": module["priority"],
                            "color": priority_colors.get(module["priority"], "gray")
                        }
                    },
                    "Estimated Hours": {
                        "number": module["estimated_hours"]
                    },
                    "Skills": {
                        "multi_select": skills_options
                    },
                    "Notes": {
                        "rich_text": [{"text": {"content": module.get("notes", "")}}]
                    }
                }
            )
            print(f"  ✅ Added: {module['name']}")
        except Exception as e:
            print(f"  ❌ Failed to add {module['name']}: {e}")

def populate_resources(resources):
    """Populate the Resources Library database"""
    print(f"\n📖 Populating {len(resources)} resources...")
    
    for resource in resources:
        # Priority color mapping
        priority_colors = {
            "Must Read": "red",
            "Must Take": "red",
            "Must Have": "red",
            "High Value": "orange",
            "Good to Have": "yellow",
            "Good Practice": "yellow",
            "Reference": "blue",
            "Optional": "gray"
        }
        
        # Status color mapping
        status_colors = {
            "Not Started": "gray",
            "In Progress": "blue",
            "Completed": "green",
            "Reference": "purple"
        }
        
        # Type color mapping
        type_colors = {
            "Book": "blue",
            "Online Course": "green",
            "Video Series": "purple",
            "Interactive Platform": "orange",
            "Documentation": "gray",
            "Tutorial": "yellow",
            "Workshop": "pink",
            "Conference": "red"
        }
        
        # Cost color mapping
        cost_colors = {
            "Free": "green",
            "Paid": "red",
            "Subscription": "orange",
            "Freemium": "yellow"
        }
        
        try:
            properties = {
                "Resource Name": {
                    "title": [{"text": {"content": resource["name"]}}]
                },
                "Type": {
                    "select": {
                        "name": resource["type"],
                        "color": type_colors.get(resource["type"], "gray")
                    }
                },
                "Provider": {
                    "rich_text": [{"text": {"content": resource.get("provider", "")}}]
                },
                "Status": {
                    "select": {
                        "name": resource.get("status", "Not Started"),
                        "color": status_colors.get(resource.get("status", "Not Started"), "gray")
                    }
                },
                "Priority": {
                    "select": {
                        "name": resource["priority"],
                        "color": priority_colors.get(resource["priority"], "gray")
                    }
                },
                "Difficulty": {
                    "select": {"name": resource.get("difficulty", "Intermediate")}
                },
                "Cost": {
                    "select": {
                        "name": resource.get("cost", "Paid"),
                        "color": cost_colors.get(resource.get("cost", "Paid"), "gray")
                    }
                },
                "Estimated Time": {
                    "rich_text": [{"text": {"content": resource.get("estimated_time", "")}}]
                },
                "Notes": {
                    "rich_text": [{"text": {"content": resource.get("notes", "")}}]
                }
            }
            
            # Add URL if available
            if resource.get("url"):
                properties["URL"] = {"url": resource["url"]}
            
            # Add rating if available
            if resource.get("rating"):
                properties["Rating"] = {"number": resource["rating"]}
            
            response = notion.pages.create(
                parent={"database_id": database_ids["resources_library"]},
                properties=properties
            )
            print(f"  ✅ Added: {resource['name']}")
        except Exception as e:
            print(f"  ❌ Failed to add {resource['name']}: {e}")

def populate_projects(projects):
    """Populate the Projects Portfolio database"""
    print(f"\n🚀 Populating {len(projects)} projects...")
    
    for project in projects:
        # Convert lists to multi-select format
        tech_options = []
        for tech in project.get("technologies", []):
            tech_options.append({"name": tech})
        
        skills_options = []
        for skill in project.get("skills_applied", []):
            skills_options.append({"name": skill})
        
        # Status color mapping
        status_colors = {
            "Not Started": "gray",
            "Planning": "yellow",
            "In Development": "blue",
            "Testing": "orange",
            "Completed": "green",
            "Deployed": "purple",
            "Archived": "brown"
        }
        
        try:
            properties = {
                "Project Name": {
                    "title": [{"text": {"content": project["name"]}}]
                },
                "Description": {
                    "rich_text": [{"text": {"content": project.get("description", "")}}]
                },
                "Status": {
                    "select": {
                        "name": project.get("status", "Not Started"),
                        "color": status_colors.get(project.get("status", "Not Started"), "gray")
                    }
                },
                "Technologies Used": {
                    "multi_select": tech_options
                },
                "Skills Applied": {
                    "multi_select": skills_options
                },
                "Timeline": {
                    "rich_text": [{"text": {"content": project.get("timeline", "")}}]
                }
            }
            
            # Add URLs if available
            if project.get("github_link"):
                properties["GitHub Link"] = {"url": project["github_link"]}
            
            if project.get("demo_link"):
                properties["Demo Link"] = {"url": project["demo_link"]}
            
            # Add lessons learned as a rich text field
            if project.get("lessons_learned"):
                lessons_text = "\n".join(f"• {lesson}" for lesson in project["lessons_learned"])
                properties["Lessons Learned"] = {
                    "rich_text": [{"text": {"content": lessons_text}}]
                }
            
            # Add next steps
            if project.get("next_steps"):
                steps_text = "\n".join(f"• {step}" for step in project["next_steps"])
                properties["Next Steps"] = {
                    "rich_text": [{"text": {"content": steps_text}}]
                }
            
            response = notion.pages.create(
                parent={"database_id": database_ids["projects_portfolio"]},
                properties=properties
            )
            print(f"  ✅ Added: {project['name']}")
        except Exception as e:
            print(f"  ❌ Failed to add {project['name']}: {e}")

def populate_weekly_reflections():
    """Create initial weekly reflection entries"""
    print(f"\n📊 Creating sample weekly reflections...")
    
    # Create a few sample weekly reflections
    current_week = datetime.now()
    
    sample_reflections = [
        {
            "week_date": current_week.strftime("%Y-%m-%d"),
            "hours_studied": 0,
            "concepts": "Ready to start the learning journey!",
            "challenges": "Setting up the learning system",
            "next_week_goals": "Complete environment setup and start with first module",
            "breakthrough": "Created comprehensive learning tracker system",
            "confidence_backend": 3,
            "confidence_database": 3,
            "confidence_system_design": 2,
            "confidence_algorithms": 2,
            "confidence_ai_ml": 2
        }
    ]
    
    for reflection in sample_reflections:
        try:
            response = notion.pages.create(
                parent={"database_id": database_ids["weekly_reflections"]},
                properties={
                    "Week Date": {
                        "date": {"start": reflection["week_date"]}
                    },
                    "Hours Studied": {
                        "number": reflection["hours_studied"]
                    },
                    "Concepts Learned": {
                        "rich_text": [{"text": {"content": reflection["concepts"]}}]
                    },
                    "Challenges Faced": {
                        "rich_text": [{"text": {"content": reflection["challenges"]}}]
                    },
                    "Goals for Next Week": {
                        "rich_text": [{"text": {"content": reflection["next_week_goals"]}}]
                    },
                    "Breakthrough Moments": {
                        "rich_text": [{"text": {"content": reflection.get("breakthrough", "")}}]
                    },
                    "Confidence - Backend": {
                        "number": reflection["confidence_backend"]
                    },
                    "Confidence - Database": {
                        "number": reflection["confidence_database"]
                    },
                    "Confidence - System Design": {
                        "number": reflection["confidence_system_design"]
                    },
                    "Confidence - Algorithms": {
                        "number": reflection["confidence_algorithms"]
                    },
                    "Confidence - AI/ML": {
                        "number": reflection["confidence_ai_ml"]
                    }
                }
            )
            print(f"  ✅ Added reflection for week: {reflection['week_date']}")
        except Exception as e:
            print(f"  ❌ Failed to add reflection: {e}")

def main():
    """Main function to populate all databases"""
    print("📊 Starting Notion Data Population...")
    print("=" * 60)
    
    # Parse learning plan
    print("\n📖 Loading data from JSON files (with legacy fallback)...")
    learning_modules, resources, projects = parse_learning_plan()
    
    print(f"Found: {len(learning_modules)} modules, {len(resources)} resources, {len(projects)} projects")
    
    # Populate databases
    populate_learning_modules(learning_modules)
    populate_resources(resources)
    populate_projects(projects)
    populate_weekly_reflections()
    
    print("\n" + "=" * 60)
    print("✅ Data population complete!")
    print("\nNext steps:")
    print("1. Visit your Notion workspace to see the populated data")
    print("2. Start tracking your learning progress")
    print("3. Update weekly reflections regularly")
    print("4. Customize the data by editing the JSON files in the 'data' directory")

if __name__ == "__main__":
    main()