
import os
from pathlib import Path

def generate_project_tree(project_path, exclude):
    
    tree = ""
    for dirpath, dirnames, filenames in os.walk(project_path):
        depth = dirpath.replace(project_path, '').count(os.sep)
        dir_base_name = os.path.basename(dirpath)
        
        if dir_base_name in exclude:
            dirnames[:] = []  # remove directory names from list to prevent further walking
            continue

        indent = ' ' * 4 * (depth - 1)
        tree += '{}{}/\n'.format(indent, dir_base_name)
        for f in filenames:
            tree += '{}{}\n'.format(indent + ' ' * 4, f)
    with open('project_tree.txt', 'w') as f:
        f.write(tree)
    print("tree generated ")
    return tree

def remove_comments_from_file(input_filepath, remove_empty_lines=True):
    
    with open(input_filepath, 'r') as file:
        lines = file.readlines()
    
    # Filter out lines that start with #
    cleaned_lines = [line for line in lines if not line.strip().startswith("#")]
    
    # Further filter to remove empty lines if specified
    if remove_empty_lines:
        cleaned_lines = [line for line in cleaned_lines if line.strip() != ""]
    
    # Determine output file name
    output_filepath = input_filepath.rsplit('.', 1)[0] + '_no_comments.py'
    
    # Save cleaned lines to output file
    with open(output_filepath, 'w') as file:
        file.writelines(cleaned_lines)
    
    return output_filepath



def main():
    project_path = str(Path(__file__).resolve().parent)
    
    # file_path = "base\settings.py"
    # output_path = remove_comments_from_file(file_path,remove_empty_lines=True)
    # print(f"Cleaned file saved to: {output_path}")

    generate_project_tree(project_path=project_path,exclude=['.env','.venv', '.git','static','__pycache__','__init__.py'])







if __name__ == "__main__":
    main()