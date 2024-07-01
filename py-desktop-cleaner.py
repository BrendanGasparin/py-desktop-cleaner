import os
from pathlib import Path
import shutil

# Get the user's home directory
home_directory = os.path.expanduser("~")
# Get the user's OneDrive directory
onedrive = os.path.join(home_directory, "OneDrive")
# Get the source directory to move files from
source_directory = os.path.join(onedrive, "Desktop")
# Set the destination directory to move files to
destination_parent = Path(home_directory) / "OneDrive" / "Desktop Organizer"
# Set the names of the subdirectories within the destination directory
destination_directories = ["Audio", "Documents", "Images", "Spreadsheets", "Videos"]

# Extensions of the files that will be organized and the subdirectories to organize them into
extensions = {
    ".mp3": "Audio",
    ".ogg": "Audio",
    ".wav": "Audio",
    ".doc": "Documents",
    ".docx": "Documents",
    ".pdf": "Documents",
    ".rtf": "Documents",
    ".txt": "Documents",
    ".bmp": "Images",
    ".gif": "Images",
    ".jpg": "Images",
    ".png": "Images",
    ".xls": "Spreadsheets",
    ".xlsx": "Spreadsheets",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",
    ".mp4": "Videos",
    ".wmv": "Videos"
}

# Check if the parent directory for the files exists and create it if it doesn't
if not destination_parent.exists():
    destination_parent.mkdir(parents=True, exist_ok=True)
    print(f"Directory '{destination_parent}' created.")

# Check if the sub-directories for the files exist and create them if they don't
for directory in destination_directories:
    destination_subdirectory = Path(destination_parent) / directory
    if not destination_subdirectory.exists():
        destination_subdirectory.mkdir(parents=True, exist_ok=True)
        print(f"Directory '{destination_subdirectory}' created.")

# Iterate through every file in the source directory
for filename in os.listdir(source_directory):
    file_path = os.path.join(source_directory, filename)

    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()

        # If the file has one of the supported extensions then move it to its rightful destination
        if extension in extensions:
            folder_name = extensions[extension]
            folder_path = os.path.join(destination_parent, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            destination_path = os.path.join(folder_path, filename)
            shutil.move(file_path, destination_path)

            print(f"Moved {filename} to directory: {folder_name}")
        else:
            print(f"Skipped {filename}. Unsupported file extension.")

print("File organization completed.")
