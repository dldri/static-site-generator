import os
import shutil
from pathlib import Path

# Global Variables
COPY_FROM = "static"
COPY_TO = "public"


def delete_public():
    root_contents = os.listdir()
    if COPY_TO in root_contents:
        print("Public folder exists..")
        print(f"Deleting exisiting '{COPY_TO}' folder..")
        shutil.rmtree(COPY_TO)
        print(f"'{COPY_TO}' folder and its contents have been deleted..")


def copy_static():
    print(f"Copying contents from '{COPY_FROM}' folder to '{COPY_TO} folder..")
    print("=====")
    # Traverse the COPY_FROM folders
    for root, dirs, files in os.walk(COPY_FROM):
        for name in dirs:
            new_directory_path = os.path.join(COPY_TO, name)
            os.makedirs(new_directory_path)
            print(f"{new_directory_path} folder created")
        for name in files:
            og_file_path = os.path.join(root, name)
            new_file_path = og_file_path.replace(COPY_FROM, COPY_TO)
            shutil.copy(og_file_path, new_file_path)
            print(f"{og_file_path} -> {new_file_path}")
    print("=====")
    print(f"'{COPY_TO}' generated successfully from '{COPY_FROM}'!")
