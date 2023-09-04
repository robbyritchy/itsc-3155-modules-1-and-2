def check_suffix(string1, string2):
    if string1.endswith(string2) or string2.endswith(string1):
        return True
    return False

def main():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    
    if check_suffix(string1, string2):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()

#My resources were the same as the first exercise, here's the link again: https://www.youtube.com/watch?v=kqtD5dpn9C8
#I checked my work in chat gpt and made some slight changes
#My biggest error was using the find() method instead of the endswith() method 