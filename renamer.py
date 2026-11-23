
import os
from datetime import datetime

# 1. Ask for folder path
folder_path = input("Enter the folder path: ")

if not os.path.isdir(folder_path):
    print("Invalid folder path!")

else:

    # 2. Ask for filename prefix
    prefix = input("Enter the new filename prefix: ")

    # 3. Ask for starting number
    start_number = int(input("Enter the starting number: "))

    # 4. Ask for file types
    file_types = input(
        "Enter file extensions (jpg,png), or press Enter for all files: "
    )

    # Convert extensions into a list
    if file_types.strip() == "":
        extensions = []
    else:
        extensions = [
            ext.strip().lower()
            for ext in file_types.split(",")
        ]

        # Add dot if missing
        extensions = [
            ext if ext.startswith(".") else "." + ext
            for ext in extensions
        ]

    # 5. Ask whether to use date in filename
    date_option = input(
        "Include date in filename? (yes/no): "
    ).lower()

    date_type = ""

    if date_option == "yes":
        date_type = input(
            "Use creation date or modification date? (creation/modification): "
        ).lower()

    # 6. Collect files
    files = []

    for filename in os.listdir(folder_path):

        file_path = os.path.join(folder_path, filename)

        # Skip folders
        if not os.path.isfile(file_path):
            continue

        # Get file extension
        extension = os.path.splitext(filename)[1].lower()

        # Check selected file types
        if extensions and extension not in extensions:
            continue

        files.append(filename)

    # Sort filenames
    files.sort()

    # 7. Prepare new filenames
    rename_list = []
    number = start_number

    for filename in files:

        old_path = os.path.join(folder_path, filename)

        # Preserve original extension
        extension = os.path.splitext(filename)[1]

        # Add date if requested
        date_prefix = ""

        if date_type == "creation":
            timestamp = os.path.getctime(old_path)
            date_prefix = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")

        elif date_type == "modification":
            timestamp = os.path.getmtime(old_path)
            date_prefix = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")

        # Build new filename
        if date_prefix:
            new_name = f"{date_prefix}_{prefix}_{number:03d}{extension}"
        else:
            new_name = f"{prefix}_{number:03d}{extension}"

        new_path = os.path.join(folder_path, new_name)

        rename_list.append((filename, new_name, new_path))

        number += 1

    # 8. Preview
    print("\n----- Rename Preview -----")

    for old_name, new_name, new_path in rename_list:
        print(f"{old_name}  ->  {new_name}")

    # 9. Check for existing files and duplicate targets
    safe_list = []
    skipped = 0
    planned_names = set()

    for old_name, new_name, new_path in rename_list:

        old_path = os.path.join(folder_path, old_name)

        # Check if new name already exists
        if os.path.exists(new_path) and old_path != new_path:
            print(f"Skipped (name already exists): {new_name}")
            skipped += 1
            continue

        # Check for duplicate new names
        if new_name.lower() in planned_names:
            print(f"Skipped (duplicate target name): {new_name}")
            skipped += 1
            continue

        planned_names.add(new_name.lower())
        safe_list.append((old_name, new_name, new_path))

    # 10. Ask for confirmation
    confirm = input("\nDo you want to rename these files? (yes/no): ").lower()

    renamed = 0
    failed = 0

    if confirm == "yes":

        # 11. Rename files
        for old_name, new_name, new_path in safe_list:

            old_path = os.path.join(folder_path, old_name)

            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {old_name} -> {new_name}")
                renamed += 1

            except OSError as e:
                print(f"Failed to rename {old_name}: {e}")
                failed += 1

    else:
        print("Renaming cancelled.")

    # 12. Summary
    print("\n----- Summary -----")
    print("Total files found:", len(files))
    print("Successfully renamed:", renamed)
    print("Skipped:", skipped)
    print("Failed:", failed)
