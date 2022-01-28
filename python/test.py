from tkinter import YView


def run():
    for i in "hello":
        yield i

if __name__ == "__main__":
    print(str(run()))
    print(str(run()))



    

    