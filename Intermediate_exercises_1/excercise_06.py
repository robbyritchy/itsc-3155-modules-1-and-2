
#I was having a hard time with this one so most of it came from google
#Ill explain how it works

def main():
    row = int(input("Enter the row number (1-5): "))    #user inputs a number that will correspond to the row of the grid
    column = int(input("Enter the column number (1-5): ")) #user inputs a number that will correspond to the collum of the grid
    
    if 1 <= row <= 5 and 1 <= column <= 5:              #Creates dimensions of the grid to be printed 
        grid = [[0 for _ in range(5)] for _ in range(5)]  
        grid[row - 1][column - 1] = 1                    #Takes the previously inputed numbers and prints a grid with 
                                                         #the number '1' at the designated coordinates and zeros everywhere else
        for r in grid:
            print(" ".join(map(str, r)))
    else:
        print("Invalid row or column number. Please enter numbers between 1 and 5.") #Prints message if user input was not between 1 and five

if __name__ == "__main__":  #Calls main function
    main()


