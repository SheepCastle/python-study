import random

def guessing_game():
    number = random.randint(0, 101)
    while True:
        answer = int(input("Please enter number between 0 to 100: "))
        if answer < number:
            print("It's too low. Please try again.")
        elif answer > number:
            print("It's too high. Please try again")
        elif answer == number:
            print("Your answer is right. have a great day")
            break
        
guessing_game()

