import os

def find_md_files(folder):
    """
    Find all .md files in the specified folder and its subdirectories.

    Parameters:
    folder (str): The path to the folder where .md files should be searched.

    Returns:
    list: A list of paths to .md files.
    """
    md_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".md"):
                md_files.append(os.path.join(root, file))
    return md_files

if __name__ == "__main__":
    folder_name = "src"
    if not os.path.exists(folder_name):
        print(f"The folder '{folder_name}' does not exist.")
    else:
        md_files = find_md_files(folder_name)
        if md_files:
            print("Markdown files found:")
            for md_file in md_files:
                print(md_file)
        else:
            print("No Markdown files found in the folder.")