def ad_int(num_list):
  total=0
  i=0
  while i<5:
    total=total + int(num_list[i])
    i= i+1
    
  return total

def is_integer(s):
  try:
    num=int(s)
    return True
  except:
    return False



def main():
  num_list=[]
  i=0
  while i<5:
    num=input("Enter an integer: ")

    if is_integer(num):
       num_list.append(int(num))
       i=i+1
    else:
      print("Invalid input. Please enter an int")
  new_sum=ad_int(num_list)

  print(new_sum)
      

  

if __name__ == "__main__":
  main()