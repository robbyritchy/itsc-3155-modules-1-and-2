def main():
 string= input("Enter a string: ")
 

 i=len(string)-1
 while i>=0:
   print(string[i],end="")
   i=i-1

 
 #OR... MUCH COOLER WAY I LEARNED s[::-1] - reverse
 #print(string[::-1])

 

if __name__ == "__main__": 
   main()

