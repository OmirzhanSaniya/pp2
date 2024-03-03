import os

path = input()

if os.path.exists(path):
    print("The path exists:")
    all_elements = os.listdir(path)

    for element in all_elements:
        full_path = os.path.join(path, element)
        if os.path.isfile(full_path):
            print("File:", element)
        elif os.path.isdir(full_path):
            print("Directory:", element)
else:
    print("The path does not exist.")
