import os

path = input()

if os.path.isfile(path):
    if os.access(path, os.W_OK):
        try:
            os.remove(path)
            print("File deleted successfully.")
        except OSError as e:
            print(f"Error: {e.strerror}")
    else:
        print("The file is not accessible.")
else:
    print("The file does not exist.")
