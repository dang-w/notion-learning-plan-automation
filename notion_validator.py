#!/usr/bin/env python3
"""
Notion Learning Tracker Validator
Validates that all databases and pages were created correctly
"""

import os
import json
from notion_client import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Notion client
notion = Client(auth=os.environ["NOTION_TOKEN"])

def validate_database_exists(database_id, database_name):
    """Validate that a database exists and is accessible"""
    try:
        database = notion.databases.retrieve(database_id=database_id)
        print(f"✅ {database_name}: Found with {len(database['properties'])} properties")
        return True
    except Exception as e:
        print(f"❌ {database_name}: Error - {e}")
        return False

def validate_database_has_data(database_id, database_name):
    """Check if database has entries"""
    try:
        response = notion.databases.query(database_id=database_id, page_size=10)
        entry_count = len(response['results'])
        print(f"📊 {database_name}: {entry_count} entries found")
        return entry_count > 0
    except Exception as e:
        print(f"❌ {database_name} data check failed: {e}")
        return False

def validate_page_exists(page_id, page_name):
    """Validate that a page exists and is accessible"""
    try:
        page = notion.pages.retrieve(page_id=page_id)
        print(f"✅ {page_name}: Page exists and is accessible")
        return True
    except Exception as e:
        print(f"❌ {page_name}: Error - {e}")
        return False

def validate_environment():
    """Check if all required environment variables are set"""
    print("🔧 Validating Environment Setup...")
    print("-" * 40)

    required_vars = ["NOTION_TOKEN", "NOTION_PARENT_PAGE_ID"]
    missing_vars = []

    for var in required_vars:
        if var in os.environ and os.environ[var]:
            print(f"✅ {var}: Set")
        else:
            print(f"❌ {var}: Missing or empty")
            missing_vars.append(var)

    return len(missing_vars) == 0

def validate_files():
    """Check if all required files exist"""
    print("\n📁 Validating Required Files...")
    print("-" * 40)

    required_files = [
        "database_ids.json",
        "learning_plan.md",
        ".env"
    ]

    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}: Found")
        else:
            print(f"❌ {file}: Missing")
            missing_files.append(file)

    return len(missing_files) == 0

def validate_databases():
    """Validate all databases exist and have correct structure"""
    print("\n🗄️ Validating Databases...")
    print("-" * 40)

    try:
        with open("database_ids.json", "r") as f:
            database_ids = json.load(f)
    except FileNotFoundError:
        print("❌ database_ids.json not found. Run notion_database_creator.py first.")
        return False

    databases = [
        ("learning_modules", "Learning Modules"),
        ("resources_library", "Resources Library"),
        ("projects_portfolio", "Projects Portfolio"),
        ("weekly_reflections", "Weekly Reflections")
    ]

    all_valid = True
    for db_key, db_name in databases:
        if db_key in database_ids:
            if not validate_database_exists(database_ids[db_key], db_name):
                all_valid = False
        else:
            print(f"❌ {db_name}: ID not found in database_ids.json")
            all_valid = False

    return all_valid

def validate_data():
    """Check if databases have been populated with data"""
    print("\n📊 Validating Data Population...")
    print("-" * 40)

    try:
        with open("database_ids.json", "r") as f:
            database_ids = json.load(f)
    except FileNotFoundError:
        print("❌ database_ids.json not found.")
        return False

    databases = [
        ("learning_modules", "Learning Modules"),
        ("resources_library", "Resources Library"),
        ("projects_portfolio", "Projects Portfolio"),
        ("weekly_reflections", "Weekly Reflections")
    ]

    all_have_data = True
    for db_key, db_name in databases:
        if db_key in database_ids:
            if not validate_database_has_data(database_ids[db_key], db_name):
                all_have_data = False

    return all_have_data

def validate_notion_connection():
    """Test basic Notion API connection"""
    print("\n🔗 Testing Notion API Connection...")
    print("-" * 40)

    try:
        # Try to retrieve the parent page
        parent_page = notion.pages.retrieve(page_id=os.environ["NOTION_PARENT_PAGE_ID"])
        print("✅ Notion API connection successful")
        print(f"✅ Parent page accessible: {parent_page.get('properties', {}).get('title', {}).get('title', [{}])[0].get('text', {}).get('content', 'Unknown')}")
        return True
    except Exception as e:
        print(f"❌ Notion API connection failed: {e}")
        return False

def run_comprehensive_validation():
    """Run all validation checks"""
    print("🔍 Notion Learning Tracker - System Validation")
    print("=" * 60)

    checks = [
        ("Environment Setup", validate_environment),
        ("File Existence", validate_files),
        ("Notion Connection", validate_notion_connection),
        ("Database Structure", validate_databases),
        ("Data Population", validate_data)
    ]

    results = {}
    for check_name, check_function in checks:
        results[check_name] = check_function()

    # Summary
    print("\n📋 Validation Summary")
    print("=" * 60)

    all_passed = True
    for check_name, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{check_name}: {status}")
        if not passed:
            all_passed = False

    if all_passed:
        print("\n🎉 All validations passed! Your Notion Learning Tracker is ready to use.")
        print("\n🚀 Next steps:")
        print("1. Visit your Learning Management System page in Notion")
        print("2. Explore the Learning Dashboard")
        print("3. Start your first weekly reflection")
        print("4. Begin tracking your learning modules")
    else:
        print("\n⚠️ Some validations failed. Please address the issues above.")
        print("\n🔧 Common fixes:")
        print("1. Check your .env file has the correct tokens")
        print("2. Ensure database_ids.json exists (run notion_database_creator.py)")
        print("3. Verify Notion integration has proper permissions")

    return all_passed

def main():
    """Main validation function"""
    return run_comprehensive_validation()

if __name__ == "__main__":
    main()