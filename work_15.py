import os
from collections import namedtuple


def get_directory_contents(directory_path):
    entries = os.scandir(directory_path)
    User = namedtuple('User', ['name', 'extension', 'is_directory', 'parent_directory'])
    client = []

    for entry in entries:
        name = os.path.splitext(entry.name)[0]
        extension = os.path.splitext(entry.name)[1] if not entry.is_dir() else ""
        is_directory = entry.is_dir()
        parent_directory = os.path.basename(os.path.normpath(directory_path))
        user = User(name, extension, is_directory, parent_directory)
        client.append(user)

    return client


directory_path = input("напишите полный путь к катологу: ")
contents = get_directory_contents(directory_path)

if __name__ == '__main__':
    for client in contents:
        print(client)