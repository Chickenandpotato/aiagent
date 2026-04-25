import os

def get_files_info(working_directory, directory="."):
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    if not valid_target_dir:
        return (f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory")
    if not os.path.isdir(target_dir) :
        return (f"Error: \"{directory}\" is not a directory")
    
    result_string = ""
    for item in os.listdir(target_dir):
        file_path = os.path.join(target_dir, item)
        
        try:
            result_string += f"- {item}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}\n"
        except Exception as e:
            return f"Error: {e}"
    return result_string