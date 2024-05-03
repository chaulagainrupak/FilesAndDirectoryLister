import os

def list_directory(directory):
    directories = []
    files = []
    excluded_files = ['index.html', 'files.py', 'style.css', 'dirs.txt', 'files.txt']

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path) and item not in ['dirs', 'files']:
            directories.append(item)
            list_directory(item_path)
        elif os.path.isfile(item_path) and item not in excluded_files:
            files.append(item)

    with open(os.path.join(directory, "dirs.txt"), "w") as dir_file:
        for dir_name in directories:
            dir_file.write(f"<li><a href=\"{dir_name.replace(' ', '%20')}/\">&#x1F4C1; {dir_name}</a></li>\n")

    with open(os.path.join(directory, "files.txt"), "w") as file_file:
        for file_name in files:
            if file_name != excluded_files:
                file_file.write(f"<li><a href=\"{file_name.replace(' ', '%20')}\">&#x1F4C4; {file_name}</a></li>\n")

    if not directories and not files:
        with open(os.path.join(directory, "files.txt"), "w") as file_file:
            file_file.write("<li>NO FILES FOUND</li>\n")

    print(f"Done processing directory: {directory}")

def main():
    current_directory = os.getcwd()
    list_directory(current_directory)

if __name__ == "__main__":
    main()
