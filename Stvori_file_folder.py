from pathlib import Path
import shutil

def add_file_folder():
    while True:
        file_folder = input("Do you want to make a file or a folder? (file/folder): ")

        if file_folder == "file":
            naming = input("Name your file (example: new_file.txt): ")
            file = Path(naming)
            if file.exists():
                print(f"File '{naming}' already exists!")
            else:
                file.touch()  
                print(f"File '{naming}' added!")
            break

        elif file_folder == "folder":
            naming = input("Name your folder (example: new_folder): ")
            folder = Path(naming)
            if folder.exists():
                print(f"Folder '{naming}' already exists!")
            else:
                folder.mkdir()
                print(f"Folder '{naming}' added!")
            break
        else:
            print("Invalid input! Please type 'file' or 'folder'.")

def warning_before_delete():
    confirm = input("Do you want to proceed with deleting? (yes/no): ")
    return confirm == "yes"

def delete_file_folder():
    while True:
        file_folder = input("What do you want to delete? (file/folder): ")

        if file_folder == "file":
            naming = input("Name your file to delete (example: old_file.txt): ")
            file = Path(naming)
            if file.exists() and file.is_file():
                if warning_before_delete():
                    file.unlink()
                    print(f"File '{naming}' successfully deleted!")
                else:
                    print("Deletion canceled!")
            else:
                print(f"File '{naming}' doesn't exist or isn't a valid file!")
            break

        elif file_folder == "folder":
            naming = input("Name your folder to delete (example: old_folder): ")
            folder = Path(naming)
            if folder.exists() and folder.is_dir():
                if warning_before_delete():
                    shutil.rmtree(naming)
                    print(f"Folder '{naming}' successfully deleted!")
                else:
                    print("Deletion canceled!")
            else:
                print(f"Folder '{naming}' doesn't exist or isn't a valid folder!")
            break
        else:
            print("Invalid input! Please type 'file' or 'folder'.")

def main():
    while True:
        action = input("What do you want to do? (add/delete) or type 'exit' to quit: ")
        
        if action == "add":
            add_file_folder()
        elif action == "delete":
            delete_file_folder()
        elif action == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid action! Please type 'add', 'delete', or 'exit'.")

main()
