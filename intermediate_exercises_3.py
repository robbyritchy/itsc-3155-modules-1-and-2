def letter_count(string):
  new_dict={}
  
  #u=list(set(string))  #more efficient
  u=string
  i=0
  while i<len(u):
    new_dict.update({u[i] : str(string.count(u[i]))})
    i=i+1
    
  return new_dict





def main():
  string = input("Enter a string: ")
  new_dict = letter_count(string)
  print(new_dict)

if __name__ == "__main__":
  main()