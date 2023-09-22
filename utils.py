
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

project_path = str(Path(__file__).resolve().parent)
generate_project_tree(project_path=project_path,exclude=['.env', '.git','static','__pycache__','__init__.py'])
