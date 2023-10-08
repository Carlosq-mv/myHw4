def allcaps(func):
    def caps():
        string1 = str(func())
        print(string1.upper())
    return caps

@allcaps
def greet():
    return "hello world!"

def main():
    greet();

main()

    