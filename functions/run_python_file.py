import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_path = os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs

        if not valid_target_path:
            return (f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory")
        if not os.path.isfile(target_path) :
            return (f"Error: \"{file_path}\" does not exist or is not a regular file")
        if not target_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_path]
        if args:    
            command.extend(args)
        run_result = subprocess.run(command, text=True, capture_output=True, timeout=30)
        output_string = ""
        if run_result.returncode != 0:
            output_string += f"Process exited with code {run_result.returncode}\n"
        if not run_result.stderr and not run_result.stdout:
            output_string += "No output produced\n"
        else:
            output_string += f"STDOUT: {run_result.stdout}STDERR:{run_result.stderr}"
        
        return output_string
    
    except Exception as e:
        return f"Error: executing Python file: {e}"
    

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a specified file relative to the working directory, takes additional arguments as well",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
                "file_path": types.Schema(
                type=types.Type.STRING,
                description="path to file to run, relative to the working directory (default is the working directory itself)",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="arguments to input into the python file",
            ),
        },
        required=["file_path"],
    ),
)