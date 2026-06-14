"""
FILE ORGANIZER - EXAMPLE USAGE SCRIPTS
========================================

This file contains multiple examples showing how to use the FileOrganizer class
in different scenarios. Copy and modify these examples for your own use cases.
"""

from file_organizer import FileOrganizer
from pathlib import Path
import json


# ============================================================================
# EXAMPLE 1: Simple Interactive Organization (Default Mode)
# ============================================================================
def example_1_interactive():
    """
    Run the tool interactively - user provides directory path via terminal.
    This is the safest way for beginners.
    """
    print("EXAMPLE 1: Interactive Organization")
    print("-" * 50)
    
    # Create organizer
    organizer = FileOrganizer("/path/to/your/messy/folder")
    
    # Preview changes first
    print("\n📋 Previewing changes...")
    organizer.organize_files(dry_run=True)
    
    # Ask user to confirm
    response = input("\nProceed with organization? (yes/no): ")
    if response.lower() == 'yes':
        organizer.organize_files(dry_run=False)
        organizer.display_statistics()


# ============================================================================
# EXAMPLE 2: Downloads Folder Cleanup (Real-World Use Case)
# ============================================================================
def example_2_downloads_cleanup():
    """
    Organize a typical Downloads folder into common categories.
    """
    print("\nEXAMPLE 2: Downloads Folder Cleanup")
    print("-" * 50)
    
    downloads_path = Path.home() / "Downloads"
    organizer = FileOrganizer(str(downloads_path))
    
    # Use default categories (already optimized for downloads)
    print(f"Organizing: {downloads_path}")
    organizer.organize_files(dry_run=True)
    
    # Automatic execution (no confirmation for scripted tasks)
    organizer.organize_files(dry_run=False)
    
    # Show results
    organizer.display_statistics()


# ============================================================================
# EXAMPLE 3: Custom Categories - Content Creator Workflow
# ============================================================================
def example_3_content_creator():
    """
    Organize files for a content creator with custom categories:
    Raw Footage, Edited Videos, Images, Audio, Assets, Projects
    """
    print("\nEXAMPLE 3: Content Creator Organization")
    print("-" * 50)
    
    # Define custom categories
    content_categories = {
        "Raw Footage": [".mp4", ".avi", ".mov", ".mkv", ".flv"],
        "Edited Videos": [".mp4", ".avi", ".mov"],  # Can overlap with raw
        "Images": [".jpg", ".jpeg", ".png", ".psd", ".ai"],
        "Audio": [".mp3", ".wav", ".aac", ".flac"],
        "Graphics & Assets": [".psd", ".ai", ".svg", ".sketch"],
        "Projects": [".prproj", ".aep", ".fcpxml"],  # Adobe/Final Cut projects
        "Archives": [".zip", ".rar", ".7z"],
    }
    
    organizer = FileOrganizer("/path/to/content/folder")
    organizer.set_custom_categories(content_categories)
    
    print("Custom categories configured for content creation")
    organizer.organize_files(dry_run=True)
    organizer.organize_files(dry_run=False)


# ============================================================================
# EXAMPLE 4: Custom Categories - Professional Workspace
# ============================================================================
def example_4_professional_workspace():
    """
    Organize a professional workspace with business-focused categories.
    """
    print("\nEXAMPLE 4: Professional Workspace")
    print("-" * 50)
    
    professional_categories = {
        "Presentations": [".pptx", ".ppt", ".key", ".odp"],
        "Spreadsheets": [".xlsx", ".xls", ".csv", ".numbers"],
        "Documents": [".docx", ".doc", ".pdf", ".txt", ".rtf"],
        "Reports": [".pdf", ".docx", ".xlsx"],
        "Contracts": [".pdf", ".docx"],
        "Emails": [".eml", ".msg"],
        "Databases": [".db", ".sqlite", ".accdb"],
        "Backups": [".zip", ".backup", ".bak"],
    }
    
    organizer = FileOrganizer("/path/to/work/folder")
    organizer.set_custom_categories(professional_categories)
    
    organizer.organize_files()
    organizer.display_statistics()


# ============================================================================
# EXAMPLE 5: Photography Organization by File Type
# ============================================================================
def example_5_photography_workflow():
    """
    Organize photography files with RAW files, JPEGs, and edited versions.
    """
    print("\nEXAMPLE 5: Photography Workflow")
    print("-" * 50)
    
    photo_categories = {
        "RAW Files": [".raw", ".cr2", ".nef", ".dng"],  # Camera-specific
        "Previews": [".jpg", ".jpeg", ".png"],
        "Edited": [".tiff", ".psd", ".png"],
        "Archives": [".zip", ".rar"],
    }
    
    organizer = FileOrganizer("/path/to/photo/shoot")
    organizer.set_custom_categories(photo_categories)
    
    organizer.organize_files()
    organizer.display_statistics()


# ============================================================================
# EXAMPLE 6: Code Projects Organization
# ============================================================================
def example_6_code_projects():
    """
    Organize a folder with multiple coding projects and resources.
    """
    print("\nEXAMPLE 6: Code Projects")
    print("-" * 50)
    
    code_categories = {
        "Python": [".py", ".pyc", ".pyw"],
        "JavaScript": [".js", ".jsx", ".ts", ".tsx"],
        "Web": [".html", ".css", ".scss"],
        "Data": [".json", ".xml", ".csv", ".sql"],
        "Config": [".yaml", ".yml", ".toml", ".ini", ".conf"],
        "Docs": [".md", ".txt", ".rst"],
        "Archives": [".zip", ".gz", ".tar"],
    }
    
    organizer = FileOrganizer("/path/to/projects")
    organizer.set_custom_categories(code_categories)
    
    organizer.organize_files()
    organizer.display_statistics()


# ============================================================================
# EXAMPLE 7: Batch Process Multiple Directories
# ============================================================================
def example_7_batch_processing():
    """
    Process multiple directories in sequence (useful for backing up multiple folders).
    """
    print("\nEXAMPLE 7: Batch Processing")
    print("-" * 50)
    
    # List of directories to organize
    directories = [
        "/path/to/folder1",
        "/path/to/folder2",
        "/path/to/folder3",
    ]
    
    for directory in directories:
        try:
            print(f"\n📁 Processing: {directory}")
            organizer = FileOrganizer(directory)
            organizer.organize_files(dry_run=False)
            organizer.display_statistics()
        except Exception as e:
            print(f"❌ Error processing {directory}: {str(e)}")


# ============================================================================
# EXAMPLE 8: School/Student Organization
# ============================================================================
def example_8_student_workspace():
    """
    Organize a student's files by subject and file type.
    """
    print("\nEXAMPLE 8: Student Workspace")
    print("-" * 50)
    
    student_categories = {
        "Assignments": [".docx", ".pdf", ".txt"],
        "Presentations": [".pptx", ".ppt", ".key"],
        "Research": [".pdf", ".docx", ".xlsx"],
        "Code Projects": [".py", ".java", ".js", ".cpp"],
        "Spreadsheets": [".xlsx", ".xls", ".csv"],
        "Notes": [".txt", ".docx", ".md"],
        "Media": [".mp4", ".mp3", ".jpg", ".png"],
    }
    
    organizer = FileOrganizer("/path/to/school/files")
    organizer.set_custom_categories(student_categories)
    
    organizer.organize_files()


# ============================================================================
# EXAMPLE 9: Reading and Analyzing the Log File
# ============================================================================
def example_9_analyze_logs():
    """
    Read and analyze the generated log file to understand what was organized.
    """
    print("\nEXAMPLE 9: Log File Analysis")
    print("-" * 50)
    
    log_file = Path("file_organizer_log.json")
    
    if log_file.exists():
        with open(log_file, 'r') as f:
            log_data = json.load(f)
        
        # Display summary
        stats = log_data.get('statistics', {})
        print(f"Session Time: {log_data['session_timestamp']}")
        print(f"Source: {log_data['source_directory']}")
        print(f"\nStatistics:")
        print(f"  Total Processed: {stats.get('total_files_processed', 0)}")
        print(f"  Moved: {stats.get('files_moved', 0)}")
        print(f"  Duplicates: {stats.get('duplicates_handled', 0)}")
        print(f"  Errors: {len(stats.get('errors', []))}")
        
        # Show detailed operations
        operations = log_data.get('operations', [])
        print(f"\nOperations ({len(operations)} total):")
        for op in operations[:5]:  # Show first 5
            if op.get('action') == 'moved':
                print(f"  ✓ {Path(op['source']).name} → {op['category']}/")
            elif op.get('action') == 'error':
                print(f"  ✗ Error: {op.get('error')}")
        
        if len(operations) > 5:
            print(f"  ... and {len(operations) - 5} more operations")
    else:
        print("No log file found. Run organize_files() first.")


# ============================================================================
# EXAMPLE 10: Custom Error Handling and Logging
# ============================================================================
def example_10_advanced_error_handling():
    """
    Advanced usage with custom error handling and detailed reporting.
    """
    print("\nEXAMPLE 10: Advanced Error Handling")
    print("-" * 50)
    
    try:
        organizer = FileOrganizer("/path/to/folder")
        
        # Validate directory
        organizer.validate_source_directory()
        print("✓ Directory validated")
        
        # Organize with error handling
        organizer.organize_files(dry_run=True)
        organizer.organize_files(dry_run=False)
        
        # Check for errors
        if organizer.stats['errors']:
            print(f"\n⚠ {len(organizer.stats['errors'])} error(s) occurred:")
            for error in organizer.stats['errors']:
                print(f"  - {error}")
        else:
            print("\n✓ No errors!")
        
        # Display detailed statistics
        organizer.display_statistics()
        
    except FileNotFoundError as e:
        print(f"❌ Directory not found: {e}")
    except NotADirectoryError as e:
        print(f"❌ Not a valid directory: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


# ============================================================================
# EXAMPLE 11: Dry Run Analysis Without Execution
# ============================================================================
def example_11_dry_run_only():
    """
    Use dry-run to analyze a folder structure without making changes.
    Useful for testing custom categories before actual execution.
    """
    print("\nEXAMPLE 11: Dry Run Analysis")
    print("-" * 50)
    
    organizer = FileOrganizer("/path/to/folder")
    
    # Test different category configurations
    print("\n1️⃣ Testing with DEFAULT categories:")
    organizer.organize_files(dry_run=True)
    
    print("\n2️⃣ Testing with CUSTOM categories:")
    custom = {
        "Work": [".docx", ".xlsx", ".pptx", ".pdf"],
        "Personal": [".jpg", ".png", ".mp4"],
    }
    organizer.set_custom_categories(custom)
    organizer.organize_files(dry_run=True)
    
    print("\nNo files were actually moved. Ready to execute when you are!")


# ============================================================================
# EXAMPLE 12: Organizing with Logging to Console
# ============================================================================
def example_12_with_console_logging():
    """
    Run organization with detailed console output for debugging.
    """
    print("\nEXAMPLE 12: Console Logging")
    print("-" * 50)
    
    import logging
    
    # Set logging level to DEBUG for more details
    logging.getLogger().setLevel(logging.DEBUG)
    
    organizer = FileOrganizer("/path/to/folder")
    organizer.organize_files(dry_run=False)
    
    # This will show all DEBUG and INFO messages in console


# ============================================================================
# DEMO: Run a Quick Test
# ============================================================================
def demo_with_sample_files():
    """
    Create a demo directory with sample files and organize it.
    Perfect for testing without affecting real files.
    """
    print("\n" + "="*60)
    print("DEMO: File Organizer with Sample Files")
    print("="*60)
    
    # Create demo directory
    demo_dir = Path("demo_files_example")
    demo_dir.mkdir(exist_ok=True)
    
    # Create sample files
    sample_files = {
        # Images
        "vacation_photo.jpg": "Images",
        "screenshot.png": "Images",
        
        # Videos
        "tutorial.mp4": "Videos",
        "presentation.avi": "Videos",
        
        # Documents
        "resume.pdf": "Documents",
        "report.xlsx": "Documents",
        "notes.txt": "Documents",
        
        # Audio
        "song.mp3": "Audio",
        "podcast.wav": "Audio",
        
        # Code
        "script.py": "Code",
        "website.html": "Code",
        
        # Archives
        "backup.zip": "Archives",
    }
    
    for filename, category in sample_files.items():
        file_path = demo_dir / filename
        file_path.touch()
    
    print(f"\n✓ Created demo folder: {demo_dir}")
    print(f"✓ Created {len(sample_files)} sample files")
    
    # Organize the demo folder
    print("\n" + "-"*60)
    organizer = FileOrganizer(str(demo_dir))
    organizer.organize_files(dry_run=True)
    
    response = input("\nOrganize demo files? (yes/no): ")
    if response.lower() == 'yes':
        organizer.organize_files(dry_run=False)
        organizer.display_statistics()
        print(f"\n✓ Organized successfully!")
        print(f"✓ Check folder: {demo_dir}")


# ============================================================================
# MAIN: Choose Which Example to Run
# ============================================================================
if __name__ == "__main__":
    print("\n" + "="*70)
    print("FILE ORGANIZER - EXAMPLE USAGE SCRIPTS")
    print("="*70)
    print("""
AVAILABLE EXAMPLES:
1. Interactive Organization (Recommended for beginners)
2. Downloads Folder Cleanup
3. Content Creator Organization
4. Professional Workspace
5. Photography Organization
6. Code Projects Organization
7. Batch Process Multiple Directories
8. Student Workspace Organization
9. Log File Analysis
10. Advanced Error Handling
11. Dry Run Analysis (No execution)
12. Console Logging Debug
13. DEMO: Create & Organize Sample Files

Or run a specific example directly by calling its function!
Example: python example_usage.py 13
    """)
    
    # You can run a demo directly
    print("\nRunning DEMO with sample files...\n")
    demo_with_sample_files()
