import os
import shutil
from datetime import datetime
import hashlib


def calculate_md5(file_path):
    """Calculate the MD5 checksum of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def organize_files(directory):
    if not os.path.isdir(directory):
        print(f"{directory} is not a valid directory.")
        return

    file_types = {
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'documents': ['.pdf', '.docx', '.txt', '.pptx', '.xlsx'],
        'audio': ['.mp3', '.wav', '.aac', '.flac'],
        'video': ['.mp4', '.mov', '.avi', '.mkv'],
        'archives': ['.zip', '.tar', '.gz', '.rar'],
    }

    seen_files = {}

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()
            file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d')

            # Calculate the file's MD5 checksum
            file_md5 = calculate_md5(file_path)

            # Check for duplicates
            if file_md5 in seen_files:
                print(f"Duplicate found: {filename} is a duplicate of {seen_files[file_md5]}. Removing duplicate.")
                os.remove(file_path)
                continue
            else:
                seen_files[file_md5] = filename

            # Determine the destination folder
            for folder, extensions in file_types.items():
                if file_ext in extensions:
                    date_folder = os.path.join(directory, folder, file_mtime)
                    os.makedirs(date_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(date_folder, filename))
                    break
            else:
                # If the file type is not recognized, move it to an 'others' folder
                date_folder = os.path.join(directory, 'others', file_mtime)
                os.makedirs(date_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(date_folder, filename))

    print("Files have been organized and duplicates removed.")


if __name__ == "__main__":
    organize_files('C:/Users/saima/Downloads')
