# Ashish Bairwa
import os

def move_file(source, destination):
    """Manually move a file from source to destination."""
    with open(source, "rb") as src_file:
        data = src_file.read()
    with open(destination, "wb") as dest_file:
        dest_file.write(data)
    os.remove(source)


def revert_organization(directory):
    """Revert organized files back to the main directory."""
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)

        if not os.path.isdir(folder_path):
            continue

        # Move files back to the main directory
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                target_file_path = os.path.join(directory, file_name)
                move_file(file_path, target_file_path)
                print(f"Moved back: {file_name} from {folder_path}")

        # Remove the folder manually
        os.rmdir(folder_path)
        print(f"Removed folder: {folder_name}")

if __name__ == "__main__":
    desktop_path = os.path.expanduser("~/Downloads")
    revert_organization(desktop_path)
    print("Reversion completed.")
