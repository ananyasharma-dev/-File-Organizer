import os
import shutil
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import logging

class FileOrganizer:
    """
    A powerful file organization tool that sorts files into categorized folders.
    Features: duplicate handling, activity logging, custom categories, and detailed reports.
    """
    
    # Default file categories and their extensions
    DEFAULT_CATEGORIES = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico"],
        "Videos": [".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv", ".webm"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".xls", ".ppt", ".pptx", ".csv"],
        "Audio": [".mp3", ".wav", ".aac", ".flac", ".m4a", ".wma", ".ogg"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".iso"],
        "Code": [".py", ".js", ".java", ".cpp", ".html", ".css", ".json", ".xml", ".sql"],
        "Executables": [".exe", ".msi", ".dmg", ".app", ".apk"],
    }
    
    def __init__(self, source_dir, log_file="file_organizer_log.json"):
        """Initialize the organizer with a source directory and log file."""
        self.source_dir = Path(source_dir)
        self.log_file = Path(log_file)
        self.categories = self.DEFAULT_CATEGORIES.copy()
        self.operations_log = []
        self.stats = {
            "total_files_processed": 0,
            "files_moved": 0,
            "duplicates_handled": 0,
            "errors": []
        }
        
        # Setup logging
        self.setup_logging()
        
    def setup_logging(self):
        """Configure logging for terminal output."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger = logging.getLogger(__name__)
        
    def validate_source_directory(self):
        """Check if source directory exists and is accessible."""
        if not self.source_dir.exists():
            raise FileNotFoundError(f"Directory not found: {self.source_dir}")
        if not self.source_dir.is_dir():
            raise NotADirectoryError(f"Not a directory: {self.source_dir}")
        self.logger.info(f"✓ Source directory validated: {self.source_dir}")
        
    def set_custom_categories(self, categories):
        """Allow users to define custom file categories."""
        self.categories = categories
        self.logger.info(f"✓ Custom categories loaded: {list(categories.keys())}")
        
    def get_file_category(self, file_path):
        """Determine which category a file belongs to based on extension."""
        suffix = file_path.suffix.lower()
        for category, extensions in self.categories.items():
            if suffix in extensions:
                return category
        return "Other"  # Default category for uncategorized files
    
    def handle_duplicate(self, destination_path):
        """Handle duplicate filenames by appending a number."""
        if not destination_path.exists():
            return destination_path
        
        stem = destination_path.stem  # filename without extension
        suffix = destination_path.suffix  # file extension
        parent = destination_path.parent
        
        counter = 1
        while True:
            new_name = f"{stem}_{counter}{suffix}"
            new_path = parent / new_name
            if not new_path.exists():
                self.stats["duplicates_handled"] += 1
                self.logger.warning(f"⚠ Duplicate found. Renaming to: {new_name}")
                return new_path
            counter += 1
    
    def organize_files(self, dry_run=False):
        """
        Scan and organize files into categorized folders.
        
        Args:
            dry_run (bool): If True, show what would be moved without actually moving.
        """
        self.validate_source_directory()
        self.logger.info(f"{'[DRY RUN] ' if dry_run else ''}Starting file organization...")
        
        # Get all files in the source directory (non-recursive)
        files_to_process = [f for f in self.source_dir.iterdir() if f.is_file()]
        self.stats["total_files_processed"] = len(files_to_process)
        
        if not files_to_process:
            self.logger.info("No files found to organize.")
            return
        
        # Group files by category
        files_by_category = defaultdict(list)
        for file_path in files_to_process:
            category = self.get_file_category(file_path)
            files_by_category[category].append(file_path)
        
        # Create folders and move files
        for category, files in files_by_category.items():
            category_folder = self.source_dir / category
            
            # Create category folder if it doesn't exist
            if not dry_run:
                category_folder.mkdir(exist_ok=True)
            
            self.logger.info(f"\n📁 Processing category: {category}")
            
            for file_path in files:
                destination_path = category_folder / file_path.name
                
                # Handle duplicates
                if destination_path.exists():
                    destination_path = self.handle_duplicate(destination_path)
                
                try:
                    if dry_run:
                        self.logger.info(f"  [PREVIEW] {file_path.name} → {category}/")
                    else:
                        shutil.move(str(file_path), str(destination_path))
                        self.stats["files_moved"] += 1
                        self.logger.info(f"  ✓ {file_path.name} → {category}/")
                    
                    # Log the operation
                    self.operations_log.append({
                        "timestamp": datetime.now().isoformat(),
                        "action": "moved",
                        "source": str(file_path),
                        "destination": str(destination_path),
                        "category": category
                    })
                    
                except Exception as e:
                    error_msg = f"Failed to move {file_path.name}: {str(e)}"
                    self.logger.error(f"  ✗ {error_msg}")
                    self.stats["errors"].append(error_msg)
                    self.operations_log.append({
                        "timestamp": datetime.now().isoformat(),
                        "action": "error",
                        "file": str(file_path),
                        "error": str(e)
                    })
        
        # Save log file
        if not dry_run:
            self.save_log()
            self.print_summary()
    
    def save_log(self):
        """Save detailed operation log to JSON file."""
        log_data = {
            "session_timestamp": datetime.now().isoformat(),
            "source_directory": str(self.source_dir),
            "statistics": self.stats,
            "operations": self.operations_log
        }
        
        try:
            with open(self.log_file, 'w') as f:
                json.dump(log_data, f, indent=2)
            self.logger.info(f"\n✓ Log saved to: {self.log_file}")
        except Exception as e:
            self.logger.error(f"Failed to save log: {str(e)}")
    
    def print_summary(self):
        """Print a summary of the organization operation."""
        print("\n" + "="*60)
        print("FILE ORGANIZATION SUMMARY")
        print("="*60)
        print(f"Total files processed:    {self.stats['total_files_processed']}")
        print(f"Files successfully moved: {self.stats['files_moved']}")
        print(f"Duplicates handled:       {self.stats['duplicates_handled']}")
        print(f"Errors encountered:       {len(self.stats['errors'])}")
        
        if self.stats['errors']:
            print("\nErrors:")
            for error in self.stats['errors']:
                print(f"  • {error}")
        
        print("="*60 + "\n")
    
    def display_statistics(self):
        """Display file organization statistics."""
        self.logger.info("\n" + "="*60)
        self.logger.info("DIRECTORY STATISTICS")
        self.logger.info("="*60)
        
        category_counts = defaultdict(int)
        category_size = defaultdict(int)
        
        for category_folder in self.source_dir.iterdir():
            if category_folder.is_dir() and category_folder.name in self.categories:
                for file in category_folder.iterdir():
                    if file.is_file():
                        category_counts[category_folder.name] += 1
                        category_size[category_folder.name] += file.stat().st_size
        
        for category in sorted(category_counts.keys()):
            count = category_counts[category]
            size_mb = category_size[category] / (1024 * 1024)
            self.logger.info(f"{category:15} | Files: {count:4} | Size: {size_mb:8.2f} MB")
        
        self.logger.info("="*60 + "\n")


def main():
    """Main function to demonstrate the File Organizer."""
    print("\n" + "="*60)
    print("FILE ORGANIZER AUTOMATION TOOL")
    print("="*60 + "\n")
    
    # Get directory to organize
    while True:
        directory = input("Enter the directory path to organize (or 'demo' for demo mode): ").strip()
        
        if directory.lower() == 'demo':
            # Create a demo directory with sample files
            demo_dir = Path("demo_files")
            demo_dir.mkdir(exist_ok=True)
            
            # Create sample files
            sample_files = [
                "document.pdf", "image.jpg", "video.mp4", "song.mp3",
                "archive.zip", "script.py", "spreadsheet.xlsx", "presentation.pptx",
                "image.png", "photo.jpg", "document.txt", "video.avi"
            ]
            
            for filename in sample_files:
                (demo_dir / filename).touch()
            
            directory = str(demo_dir)
            print(f"\n✓ Demo directory created with sample files at: {demo_dir}\n")
            break
        else:
            if Path(directory).exists():
                break
            else:
                print("❌ Directory not found. Please try again.\n")
    
    try:
        # Initialize organizer
        organizer = FileOrganizer(directory)
        
        # Show preview
        print("\n📋 DRY RUN (Preview mode):")
        print("-" * 60)
        organizer.organize_files(dry_run=True)
        
        # Ask for confirmation
        print("\nDo you want to proceed with the actual organization?")
        confirm = input("Type 'yes' to continue or 'no' to cancel: ").strip().lower()
        
        if confirm == 'yes':
            print("\n🔄 Starting actual file organization...\n")
            organizer.organize_files(dry_run=False)
        else:
            print("\n❌ Operation cancelled. No files were moved.\n")
        
        # Display statistics
        organizer.display_statistics()
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}\n")


if __name__ == "__main__":
    main()
