# Python Bulk File Renamer

## About the Project

Python Bulk File Renamer is a beginner-friendly Python project that automatically renames multiple files in a selected folder using a common prefix and sequential numbering.

It helps save time when renaming large numbers of files, such as event photographs, while preserving their original file extensions.

## Features

- Accepts a folder path from the user.
- Allows the user to specify a common filename prefix.
- Supports custom starting numbers.
- Preserves original file extensions.
- Allows users to select which file types to rename.
- Displays a preview of new filenames before applying changes.
- Prevents accidental overwriting of existing files.
- Handles renaming errors.
- Supports renaming files using creation or modification dates.

## Example

### Before Renaming

    Event_Photos/
    ├── IMG_001.jpg
    ├── IMG_002.jpg
    ├── IMG_003.jpg
    └── IMG_004.png

### After Renaming

    Event_Photos/
    ├── event_photo_001.jpg
    ├── event_photo_002.jpg
    ├── event_photo_003.jpg
    └── event_photo_004.png

### Example with Date

    2026-11-21_event_photo_001.jpg
    2026-11-21_event_photo_002.jpg
    2026-11-21_event_photo_003.jpg

## Technologies Used

- Python
- `os` module
- `datetime` module

## Project Structure

    bulk_file_renamer/
    │
    ├── renamer.py
    └── README.md

## How to Run

### 1. Clone the Repository

    git clone <your-repository-url>

### 2. Navigate to the Project Folder

    cd bulk_file_renamer

### 3. Run the Python Program

    python renamer.py

### 4. Provide the Required Inputs

Enter the folder path, filename prefix, starting number, and file types when prompted.

Review the preview and confirm if you want to apply the renaming.

## Additional Challenge

The program supports adding file creation or modification dates to filenames.

Example:

    2026-11-21_event_photo_001.jpg

This helps organize files based on their date.

## Summary

This project helped me understand Python file handling, working with file paths, loops, conditions, lists, sets, string formatting, exception handling, and the `os` and `datetime` modules. It also demonstrates how Python can automate repetitive tasks.
