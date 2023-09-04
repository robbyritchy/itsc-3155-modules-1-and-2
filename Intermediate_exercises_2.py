def get_combined_dict(my_dict_1, my_dict_2):
  new_dict={}
  for key in my_dict_1:
    if key in my_dict_2:
      new_dict.update( {key : my_dict_1[key] + my_dict_2[key]})
    
    
  return new_dict



def main():
  my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
  my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
  combined_dict = get_combined_dict(my_dict_1, my_dict_2)
  print(combined_dict)

if __name__ == "__main__":
  main()