import os

def split_file_path(file_path):
    path, file_name = os.path.split(file_path)
    file_name, file_ext = os.path.splitext(file_name)
    return path, file_name, file_ext


path = "/home/user/documents/file.txt"
result = split_file_path(path)
print(result)

