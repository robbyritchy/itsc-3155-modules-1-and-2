def cube_of_int(num):
    i=0
    while i<=int(num):
        print (i ** 2)
        i=i+1

def main():
    num = input("Enter an integer greater than 1: ")
    answer= cube_of_int(num)
    print (answer)


if __name__ == "__main__":
    main()
    
#I didn't use any outside sources for this one
#But I learned how to do most of this from the video i cited previously
#https://www.youtube.com/watch?v=kqtD5dpn9C8
