def letter_count(string):
  new_dict={}
  
  i=0
  while i<len(string):
    if string[i] not in new_dict:
        new_dict.update({string[i] : str(string.count(string[i]))})
    i=i+1
    
  return new_dict





def main():
  string = input("Enter a string: ")
  new_dict = letter_count(string)
  print(new_dict)

if __name__ == "__main__":
  main()