def main():
    word_list=[]
    i=0
    while i<5:
        word=input("Enter a word: ")
        word_list.append(word)
        i=i+1

    print ("Words: " + str(word_list))
    print("One String: " + str(word_list[0])+ " " + str(word_list[1])+ " " + str(word_list[2]) + " " + str(word_list[3]) + " " + str(word_list[4]))


if __name__ == "__main__":  
    main()
