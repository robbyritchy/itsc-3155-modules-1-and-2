def main():
    all_numbers=[]
    even_numbers=[]

    stop = "QUIT"

    i=0
    while i<1:
        num = input("Enter a number or QUIT to quit: ")
        if  num == stop:
            break
        else:
            if int(num)%2 == 0:
                even_numbers.append(num)
        all_numbers.append(num)
    
        

    print("All numbers: " + str(all_numbers))
    print("Even numbers: " + str(even_numbers))

if __name__ == "__main__":  
    main()



