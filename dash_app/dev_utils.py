import os

def get_file_structure(folder_path, indent_level=0):
    """Returns the file structure of a given folder as text."""
    try:
        # Initialize the text output with the current folder
        structure = ""
        indent = " " * (indent_level * 4)  # 4 spaces per indentation level
        
        # Iterate through the items in the folder
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            
            if item == '__pycache__':
                continue
            
            if os.path.isdir(item_path):
                # If it's a directory, add it to the structure and recurse
                structure += f"{indent}- {item}/\n"
                structure += get_file_structure(item_path, indent_level + 1)
            else:
                # If it's a file, add it to the structure
                structure += f"{indent}- {item}\n"
        
        return structure
    
    except FileNotFoundError:
        return "Folder not found."
    except PermissionError:
        return "Permission denied."
    except Exception as e:
        return str(e)
