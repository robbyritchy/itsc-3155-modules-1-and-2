def get_unique_list(list):
    new_list=[]
    i = 0
    while i<len(list):
        if list[i] not in new_list:                
            new_list.append(list[i])
        i=i+1
    
    return new_list
    
def main():
    sample_list=[1,2,2,3,5]
    unique_list= get_unique_list(sample_list)
    print(unique_list)


if __name__ == "__main__":
    main()