def main():
    string=input("Enter a string: ")
    new_string= ""
    i=0

    while i<len(string):
      if string[i] != " ":
         if string[i].islower():
           new_string = new_string + string[i]

     
      i=i+1
      j=0
    while j<len(string):
      if string[j] != " ":
         if string[j].isupper():
           new_string = new_string + string[j]

     
      j=j+1

    print (new_string)

if __name__ == "__main__":
    main()