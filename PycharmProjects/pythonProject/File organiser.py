import os
import shutil


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

    for folder, extensions in file_types.items():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)
        for filename in os.listdir(directory):
            file_ext = os.path.splitext(filename)[1].lower()
            if file_ext in extensions:
                shutil.move(os.path.join(directory, filename), os.path.join(folder_path, filename))

    print("Files have been organized.")


if __name__ == "__main__":
    organize_files('C:/Users/saima/Downloads')
