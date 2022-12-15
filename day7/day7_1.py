from parse import *


class File:
    def __init__(self, name:str, size:int):
        self.name = name
        self.size = size


class Folder:
    def __init__(self, name:str):
        self.name = name
        self.sub_folders = list()
        self.files = list()

    def get_size(self) -> int:
        file_sizes = sum([x.size for x in self.files])
        sub_folder_sizes = sum([x.get_size() for x in self.sub_folders])

        return file_sizes + sub_folder_sizes


def run():
    current_path = ''
    root_folder = Folder(current_path)
    folder_dict = dict()
    folder_dict[current_path] = root_folder
    with open("day7_data.txt") as data:
        while True:
            line = data.readline()
            if not line:
                break
            command_parsed = parse("$ {command:2}{arguments}", line)
            if command_parsed:
                if command_parsed['command'] == 'cd':
                    argument = command_parsed['arguments'].strip()
                    if argument == '/':
                        current_path = ''
                    elif argument == '..':
                        current_path = current_path[0:current_path.rfind('/')]
                    else:
                        current_path += f"/{argument}"
                    print(current_path)
                elif command_parsed['command'] == 'ls':
                    if current_path not in folder_dict.keys():
                        new_folder = Folder(current_path)
                        folder_dict[current_path] = new_folder
                        parent = folder_dict[current_path[0:current_path.rfind('/')]]
                        parent.sub_folders.append(new_folder)
            else:
                if not line.startswith('dir'):
                    file_parse = parse("{size:d} {name}", line.strip())
                    folder_dict[current_path].files.append(File(file_parse['name'], file_parse['size']))

    total_size = 0
    for folder in folder_dict:
        if folder_dict[folder].get_size() <= 100000:
            total_size += folder_dict[folder].get_size()
            print(folder, folder_dict[folder].get_size())
    print(total_size)






if __name__ == "__main__":
    run()
