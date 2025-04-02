#!/usr/bin/env python3
"""
Package the ANPE GUI application as a standalone executable.
"""

import os
import sys
import subprocess
import platform
import shutil
from pathlib import Path

def main():
    """Main packaging function."""
    print("Packaging ANPE GUI application...")
    
    # Add parent directory to path for imports
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)
    
    # Determine the operating system
    system = platform.system()
    print(f"Detected operating system: {system}")
    
    # Create the dist directory if it doesn't exist
    dist_dir = Path(parent_dir) / "dist"
    dist_dir.mkdir(exist_ok=True)
    
    # Package using PyInstaller
    try:
        print("Running PyInstaller...")
        subprocess.run(
            ["pyinstaller", "--onefile", "--windowed", 
             os.path.join(os.path.dirname(__file__), "anpe_gui.spec")],
            check=True,
            cwd=parent_dir  # Run from parent directory
        )
        print("PyInstaller completed successfully.")
        
        # Additional steps for specific platforms
        if system == "Darwin":  # macOS
            print("Performing additional steps for macOS...")
            # Create a DMG file if possible
            try:
                app_path = dist_dir / "anpe_gui.app"
                if app_path.exists():
                    subprocess.run(
                        ["hdiutil", "create", "-volname", "ANPE GUI", 
                         "-srcfolder", str(app_path), "-ov", "-format", "UDZO", 
                         str(dist_dir / "anpe_gui.dmg")],
                        check=True
                    )
                    print("Created DMG file: dist/anpe_gui.dmg")
            except Exception as e:
                print(f"Warning: Could not create DMG file: {e}")
        
        elif system == "Windows":
            print("Performing additional steps for Windows...")
            # Create a simple ZIP file if possible
            try:
                exe_path = dist_dir / "anpe_gui.exe"
                if exe_path.exists():
                    import zipfile
                    zip_path = dist_dir / "anpe_gui_windows.zip"
                    with zipfile.ZipFile(str(zip_path), 'w') as zipf:
                        zipf.write(str(exe_path), arcname="anpe_gui.exe")
                    print(f"Created ZIP file: {zip_path}")
            except Exception as e:
                print(f"Warning: Could not create ZIP file: {e}")
        
        print("Packaging completed successfully!")
        print(f"Executable available in the {dist_dir} directory.")
        
    except subprocess.CalledProcessError as e:
        print(f"Error: PyInstaller failed with error code {e.returncode}")
        print(e.output)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 