from functions.run_python_file import run_python_file

def test():

    print("Calculator usage instructions")
    print(run_python_file("calculator", "main.py"))

    print("run calculator (ugly output)")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    print("Run calculator test successfully")
    print(run_python_file("calculator", "tests.py"))

    print("Should return Error (../main.py)")
    print(run_python_file("calculator", "../main.py"))

    print("Should return Error (nonexistent.py)")
    print(run_python_file("calculator", "nonexistent.py"))

    print("Should return Error (lorem.txt)")
    print(run_python_file("calculator", "lorem.txt"))


if __name__ == "__main__":
    test()