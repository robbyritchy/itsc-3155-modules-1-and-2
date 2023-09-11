def main():
    input_string = input("Enter a string: ")
    
    char_list = list(input_string)  #This divides the input string into a list of characters
    
    #This splits the list of characters into sublists all with size 3
    sublist_size = 3
    char_sublists = [char_list[i:i+sublist_size] for i in range(0, len(char_list), sublist_size)]
    
    print("List of Characters:", char_list)
    print("List of Lists with 3 Characters Each:", char_sublists)

if __name__ == "__main__":
    main()



#This code below was my original work, I just got so lost I asked chat gpt for help
#I commented an explanation of the code I copied

"""
def main():
    message=input("Enter a string: ")
    size=len(message) 
    list_amount= (size//3) + (size%3)
    list=[]

    i=0
    while i<list_amount:
        j=0
        while j<3:
            list.append(str(message[j]))
            j=j+1
        i=i+1
  
        
print (str(list))

if __name__ == "__main__":  
    main()
"""
