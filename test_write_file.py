from functions.write_file import write_file

def test():

    print("Results for 'wait, this isn't lorem ipsum'")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

    print("Results for 'lorem ipsum dolor sit amet'")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

    print("Results for 'this should not be allowed'")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

if __name__ == "__main__":
    test()