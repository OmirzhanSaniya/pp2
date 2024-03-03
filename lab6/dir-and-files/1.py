import os

path = input()

all_elements = os.listdir(path)

files = [item for item in all_elements if os.path.isfile(os.path.join(path, item))]
directories = [item for item in all_elements if os.path.isdir(os.path.join(path, item))]

print("Directories:", directories)
print("Files:", files)
print("All:", all_elements)