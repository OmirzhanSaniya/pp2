import os

path = input()

exist = os.path.exists(path)

access_read = os.access(path, os.R_OK)
access_write = os.access(path, os.W_OK)
access_exec = os.access(path, os.X_OK)

print("Existence:", exist)
print("Readability:", access_read)
print("Writability:", access_write)
print("Executability:", access_exec)
