# Ashish Bairwa
import os

FILE_FORMATS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar"]
}

def move_file(source, destination):
    """Manually move a file from source to destination."""
    with open(source, "rb") as src_file:
        data = src_file.read()
    with open(destination, "wb") as dest_file:
        dest_file.write(data)
    os.remove(source)

def organize_files(directory):
    """Organize files in the given directory into subfolders."""
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, file_extension = os.path.splitext(file_name)

        # Find the matching category
        for folder, extensions in FILE_FORMATS.items():
            if file_extension in extensions:
                target_folder = os.path.join(directory, folder)

                # Create folder manually if it doesn't exist
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                # Move the file
                target_file_path = os.path.join(target_folder, file_name)
                move_file(file_path, target_file_path)
                print(f"Moved: {file_name} to {target_folder}")
                break

if __name__ == "__main__":
    desktop_path = os.path.expanduser("~/Downloads")
    organize_files(desktop_path)
    print("Desktop cleaning completed.")
