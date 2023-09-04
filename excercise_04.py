def make_list(num):
    numbers=[]
    
    i=0
    while i< int(num):
        value= input("Enter number " + str(i+1) + ": ")
        numbers.append(float(value))
        i=i+1
    print("List: " + str(numbers))

def main():
    num = input("Enter in an integer: ")
    make_list(num)

if __name__ == "__main__":
    main()

