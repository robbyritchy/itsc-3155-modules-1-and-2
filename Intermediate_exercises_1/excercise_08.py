def main():
    list=[]
    single_list=[]

    i=1
    while i<=10:
        num=input("Enter number " + str(i) + ": ")
        list.append(num)
        i=i+1

    for num in list:
        if list.count(num) == 1:                  #This count function I used came from chatgpt
            single_list.append(num)               #Everything else was done on my own

    print ("Original List: " + str(list))
    print ("Numbers that appear once: " + str(single_list))

if __name__ == "__main__":  
    main()
