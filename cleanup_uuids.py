#!/usr/bin/env python3
"""
Remove UUID suffixes from Notion export filenames
Handles both files and directories
"""

import os
import re
import sys

def remove_uuid(name):
    """Remove UUID pattern from filename while preserving extension"""
    # Pattern matches space + 32 character hex string at the end of filename
    uuid_pattern = r'\s+[a-f0-9]{32}(?=\.|$)'
    clean_name = re.sub(uuid_pattern, '', name)
    
    # Also remove patterns like "1956509554a780..." (numeric prefix + hex)
    numeric_uuid_pattern = r'\s+[0-9]{3,4}[a-f0-9]{24,28}(?=\.|$)'
    clean_name = re.sub(numeric_uuid_pattern, '', clean_name)
    
    return clean_name

def rename_item(old_path):
    """Rename a file or directory by removing UUID"""
    dir_path = os.path.dirname(old_path)
    old_name = os.path.basename(old_path)
    
    # Skip if no UUID pattern found
    new_name = remove_uuid(old_name)
    if new_name == old_name:
        return old_path
    
    new_path = os.path.join(dir_path, new_name)
    
    # Handle naming conflicts
    if os.path.exists(new_path):
        base, ext = os.path.splitext(new_name)
        counter = 1
        while os.path.exists(new_path):
            if ext:
                new_name = f"{base}_{counter}{ext}"
            else:
                new_name = f"{base}_{counter}"
            new_path = os.path.join(dir_path, new_name)
            counter += 1
    
    try:
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} → {new_name}")
        return new_path
    except Exception as e:
        print(f"Error renaming {old_name}: {e}")
        return old_path

def cleanup_directory(root_dir):
    """Recursively clean up UUIDs from all files and directories"""
    # First pass: collect all paths
    all_items = []
    
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # Add files
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            all_items.append(full_path)
        
        # Add directories (process from deepest to root)
        for dirname in dirnames:
            full_path = os.path.join(dirpath, dirname)
            all_items.append(full_path)
    
    # Process all items (files and dirs from deepest level up)
    renamed_count = 0
    for item_path in all_items:
        if os.path.exists(item_path):  # Check if still exists (might have been renamed)
            old_name = os.path.basename(item_path)
            new_path = rename_item(item_path)
            if new_path != item_path:
                renamed_count += 1
    
    return renamed_count

if __name__ == "__main__":
    # Use current directory if no argument provided
    target_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    
    if not os.path.isdir(target_dir):
        print(f"Error: {target_dir} is not a directory")
        sys.exit(1)
    
    print(f"Cleaning up UUIDs in: {os.path.abspath(target_dir)}")
    print("-" * 50)
    
    count = cleanup_directory(target_dir)
    
    print("-" * 50)
    print(f"Renamed {count} items")