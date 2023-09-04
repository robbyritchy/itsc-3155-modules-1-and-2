
def main():
    first_list = []
    second_list= []
    i=0
    while i<5:
        first=input("Enter a number for the first list: ")
        first_list.append(first)
        i=i+1
    j=0
    while j<5:
        second=input("Enter a number for the second list: ")
        second_list.append(second)
        j=j+1
    compare_list =[]
    n=0
    
    while n<5:
        p=0
        while p<5:
            if first_list[n] == second_list[p]:
                compare_list.append(first_list[n])
                p=p+1
            else:
                p=p+1

            

        n=n+1

 
    print ("First List: " + str(first_list))
    print ("Second List: " + str(second_list))
    print ("Common List: " + str(compare_list))



if __name__ == "__main__":
    main()