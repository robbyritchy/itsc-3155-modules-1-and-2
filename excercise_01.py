def grade_to_letter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"

def main():
    
        grade = int(input("Enter a grade between 0 and 100: "))
        letter_grade = grade_to_letter(grade)
        print(f"The letter grade for {grade} is {letter_grade}.")
    

                 #my code wasn't compiling so I ran the question through chatgpt
                               #and it added this
