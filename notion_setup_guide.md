# Notion API Setup Guide

## Step 1: Create Notion Integration (5 minutes)

1. **Go to Notion Developers**: https://developers.notion.com/my-integrations
2. **Create New Integration**:
   - Name: "Learning Tracker Automation"
   - Associated workspace: [Select your workspace]
   - Capabilities: Check all boxes (Read, Update, Insert content)
3. **Copy the Integration Token** (starts with `secret_`)

## Step 2: Grant Permissions (2 minutes)

1. **In your Notion workspace**:
   - Create a new page called "Learning Management System"
   - Click the "⋯" menu → "Add connections" → Select your integration
   - This grants the integration access to this page and all its children

## Step 3: Environment Setup (3 minutes)

1. **Install Python packages**:
   ```bash
   pip install notion-client python-dotenv
   ```

2. **Create `.env` file** in your project directory:
   ```env
   NOTION_TOKEN=your_integration_token_here
   NOTION_PARENT_PAGE_ID=your_learning_management_page_id_here
   ```

3. **Get your parent page ID**:
   - Open your "Learning Management System" page in Notion
   - Copy the URL: `https://notion.so/Your-Page-Title-32characterID`
   - The 32-character string at the end is your page ID

## Ready for Automation!

Once these steps are complete, you can run the automation scripts.