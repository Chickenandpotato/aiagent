from functions.get_file_content import get_file_content

def test():

    print("Results from lorem.txt")
    print(get_file_content("calculator", "lorem.txt"))

    print("Results from main.py")
    print(get_file_content("calculator", "main.py"))
    
    print("Results from pkg/calculator.py")
    print(get_file_content("calculator", "pkg/calculator.py"))
    
    print("Results from /bin/cat")
    print(get_file_content("calculator", "/bin/cat"))

    print("Results from pkg/does_not_exist.py")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))

if __name__ == "__main__":
    test()