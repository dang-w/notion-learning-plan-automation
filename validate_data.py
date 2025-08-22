#!/usr/bin/env python3
"""
Data Validation Script
Validates JSON data against schemas and ensures backward compatibility
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Any, Tuple
import jsonschema
from jsonschema import validate, ValidationError, Draft7Validator

class DataValidator:
    """Validates learning tracker data for consistency and compatibility"""
    
    def __init__(self):
        self.data_dir = Path("data")
        self.schemas_dir = self.data_dir / "schemas"
        self.errors = []
        self.warnings = []
        
    def load_json_file(self, filepath: Path) -> Dict[str, Any]:
        """Load and parse a JSON file"""
        try:
            with open(filepath, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            self.errors.append(f"File not found: {filepath}")
            return {}
        except json.JSONDecodeError as e:
            self.errors.append(f"Invalid JSON in {filepath}: {e}")
            return {}
    
    def validate_against_schema(self, data: Dict, schema: Dict, filename: str) -> bool:
        """Validate data against a JSON schema"""
        try:
            validate(instance=data, schema=schema)
            return True
        except ValidationError as e:
            self.errors.append(f"Schema validation failed for {filename}: {e.message}")
            return False
    
    def validate_modules(self) -> bool:
        """Validate learning modules data"""
        print("📚 Validating learning modules...")
        
        # Load data and schema
        modules_file = self.data_dir / "learning_modules.json"
        schema_file = self.schemas_dir / "learning_module.schema.json"
        
        modules_data = self.load_json_file(modules_file)
        schema = self.load_json_file(schema_file)
        
        if not modules_data or not schema:
            return False
        
        # Validate against schema
        if not self.validate_against_schema(modules_data, schema, "learning_modules.json"):
            return False
        
        # Additional validation
        modules = modules_data.get("modules", [])
        module_ids = set()
        
        for module in modules:
            # Check for duplicate IDs
            if module.get("id") in module_ids:
                self.errors.append(f"Duplicate module ID: {module.get('id')}")
            else:
                module_ids.add(module.get("id"))
            
            # Validate estimated hours
            if module.get("estimated_hours", 0) <= 0:
                self.warnings.append(f"Module '{module.get('name')}' has invalid estimated hours")
            
            # Check phase format
            phase = module.get("phase", "")
            if not phase.startswith("Phase"):
                self.warnings.append(f"Module '{module.get('name')}' has non-standard phase format: {phase}")
        
        print(f"  ✅ Validated {len(modules)} modules")
        return True
    
    def validate_resources(self) -> bool:
        """Validate resources data"""
        print("📖 Validating resources...")
        
        # Load data and schema
        resources_file = self.data_dir / "resources.json"
        schema_file = self.schemas_dir / "resource.schema.json"
        
        resources_data = self.load_json_file(resources_file)
        schema = self.load_json_file(schema_file)
        
        if not resources_data or not schema:
            return False
        
        # Validate against schema
        if not self.validate_against_schema(resources_data, schema, "resources.json"):
            return False
        
        # Additional validation
        resources = resources_data.get("resources", [])
        resource_ids = set()
        
        # Load module IDs for cross-reference validation
        modules_file = self.data_dir / "learning_modules.json"
        modules_data = self.load_json_file(modules_file)
        valid_module_ids = {m.get("id") for m in modules_data.get("modules", [])}
        
        for resource in resources:
            # Check for duplicate IDs
            if resource.get("id") in resource_ids:
                self.errors.append(f"Duplicate resource ID: {resource.get('id')}")
            else:
                resource_ids.add(resource.get("id"))
            
            # Validate URLs
            url = resource.get("url")
            if url and not (url.startswith("http://") or url.startswith("https://")):
                self.warnings.append(f"Resource '{resource.get('name')}' has invalid URL format")
            
            # Validate module references
            for module_id in resource.get("module_ids", []):
                if module_id not in valid_module_ids:
                    self.warnings.append(f"Resource '{resource.get('name')}' references unknown module: {module_id}")
            
            # Validate rating
            rating = resource.get("rating")
            if rating is not None and (rating < 1 or rating > 5):
                self.errors.append(f"Resource '{resource.get('name')}' has invalid rating: {rating}")
        
        print(f"  ✅ Validated {len(resources)} resources")
        return True
    
    def validate_projects(self) -> bool:
        """Validate projects data"""
        print("🚀 Validating projects...")
        
        # Load data and schema
        projects_file = self.data_dir / "projects.json"
        schema_file = self.schemas_dir / "project.schema.json"
        
        projects_data = self.load_json_file(projects_file)
        schema = self.load_json_file(schema_file)
        
        if not projects_data or not schema:
            return False
        
        # Validate against schema
        if not self.validate_against_schema(projects_data, schema, "projects.json"):
            return False
        
        # Additional validation
        projects = projects_data.get("projects", [])
        project_ids = set()
        
        for project in projects:
            # Check for duplicate IDs
            if project.get("id") in project_ids:
                self.errors.append(f"Duplicate project ID: {project.get('id')}")
            else:
                project_ids.add(project.get("id"))
            
            # Validate URLs
            for url_field in ["github_link", "demo_link"]:
                url = project.get(url_field)
                if url and not (url.startswith("http://") or url.startswith("https://")):
                    self.warnings.append(f"Project '{project.get('name')}' has invalid {url_field}")
            
            # Check timeline format
            timeline = project.get("timeline", "")
            if timeline and "Month" not in timeline:
                self.warnings.append(f"Project '{project.get('name')}' has non-standard timeline format")
        
        print(f"  ✅ Validated {len(projects)} projects")
        return True
    
    def check_legacy_compatibility(self) -> bool:
        """Check if data is compatible with legacy format"""
        print("\n🔄 Checking backward compatibility...")
        
        # Check if the refactored populator can still handle legacy mode
        modules_file = self.data_dir / "learning_modules.json"
        
        # Temporarily rename files to test legacy fallback
        import shutil
        backup_created = False
        
        if modules_file.exists():
            shutil.move(modules_file, modules_file.with_suffix('.json.bak'))
            backup_created = True
        
        try:
            # Import the populator to test legacy functions
            import notion_data_populator
            
            # Test legacy extraction
            legacy_modules = notion_data_populator.get_legacy_modules()
            legacy_resources = notion_data_populator.get_legacy_resources()
            legacy_projects = notion_data_populator.get_legacy_projects()
            
            if len(legacy_modules) > 0 and len(legacy_resources) > 0 and len(legacy_projects) > 0:
                print("  ✅ Legacy extraction functions working")
            else:
                self.errors.append("Legacy extraction functions returned empty data")
                return False
            
        except Exception as e:
            self.errors.append(f"Legacy compatibility check failed: {e}")
            return False
        finally:
            # Restore backup
            if backup_created:
                shutil.move(modules_file.with_suffix('.json.bak'), modules_file)
        
        return True
    
    def check_data_consistency(self) -> bool:
        """Check consistency across all data files"""
        print("\n🔍 Checking data consistency...")
        
        # Load all data
        modules_data = self.load_json_file(self.data_dir / "learning_modules.json")
        resources_data = self.load_json_file(self.data_dir / "resources.json")
        projects_data = self.load_json_file(self.data_dir / "projects.json")
        
        modules = modules_data.get("modules", [])
        resources = resources_data.get("resources", [])
        projects = projects_data.get("projects", [])
        
        # Check phase consistency
        module_phases = {m.get("phase") for m in modules}
        project_phases = {p.get("phase") for p in projects}
        
        # All project phases should exist in module phases
        for phase in project_phases:
            if phase and phase not in module_phases:
                self.warnings.append(f"Project phase '{phase}' not found in modules")
        
        # Check skill consistency
        all_skills = set()
        for module in modules:
            all_skills.update(module.get("skills", []))
        
        for project in projects:
            for skill in project.get("skills_applied", []):
                if skill not in all_skills:
                    self.warnings.append(f"Project skill '{skill}' not defined in any module")
        
        # Count statistics
        stats = {
            "total_modules": len(modules),
            "total_resources": len(resources),
            "total_projects": len(projects),
            "total_estimated_hours": sum(m.get("estimated_hours", 0) for m in modules),
            "unique_technologies": len(set(tech for p in projects for tech in p.get("technologies", []))),
            "unique_skills": len(all_skills)
        }
        
        print(f"  📊 Statistics:")
        for key, value in stats.items():
            print(f"     - {key.replace('_', ' ').title()}: {value}")
        
        return True
    
    def generate_report(self) -> None:
        """Generate validation report"""
        print("\n" + "=" * 60)
        print("📋 VALIDATION REPORT")
        print("=" * 60)
        
        if not self.errors and not self.warnings:
            print("✅ All validations passed successfully!")
            print("✨ Data is ready for use with Notion!")
        else:
            if self.errors:
                print(f"\n❌ ERRORS ({len(self.errors)}):")
                for error in self.errors:
                    print(f"   • {error}")
            
            if self.warnings:
                print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
                for warning in self.warnings:
                    print(f"   • {warning}")
            
            print("\n📝 Recommendations:")
            if self.errors:
                print("   • Fix all errors before running the Notion populator")
            if self.warnings:
                print("   • Review warnings for data quality improvements")
    
    def run(self) -> bool:
        """Run all validations"""
        print("🔍 Starting Data Validation...")
        print("=" * 60)
        
        # Check if data directory exists
        if not self.data_dir.exists():
            self.errors.append(f"Data directory not found: {self.data_dir}")
            self.generate_report()
            return False
        
        # Run all validations
        validations = [
            self.validate_modules(),
            self.validate_resources(),
            self.validate_projects(),
            self.check_legacy_compatibility(),
            self.check_data_consistency()
        ]
        
        # Generate report
        self.generate_report()
        
        # Return success if no errors
        return len(self.errors) == 0

def main():
    """Main entry point"""
    validator = DataValidator()
    success = validator.run()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()