import os
import shutil

source_folder = input("Enter folder path: ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    if os.path.isfile(file_path):

        extension = os.path.splitext(filename)[1].lower()

        moved = False

        for folder, extensions in file_types.items():

            if extension in extensions:

                destination_folder = os.path.join(
                    source_folder,
                    folder
                )

                os.makedirs(destination_folder, exist_ok=True)

                shutil.move(
                    file_path,
                    os.path.join(destination_folder, filename)
                )

                moved = True
                break

        if not moved:

            other_folder = os.path.join(
                source_folder,
                "Others"
            )

            os.makedirs(other_folder, exist_ok=True)

            shutil.move(
                file_path,
                os.path.join(other_folder, filename)
            )

print("Files Organized Successfully!")
