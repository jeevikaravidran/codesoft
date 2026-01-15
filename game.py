import random
user_score = 0
computer_score = 0
Play_again = "yes"
while Play_again == "yes":
    user_choices = int(input("Enter your choice (0 = Rock, 1 = Paper, 2 = Scissors): "))
    computer_choices = random.randint(0, 2)
    if user_choices < 0 or user_choices > 2:
        print("Invalid input. Please enter 0, 1 or 2.")
    else:
        print("You chose:", user_choices)
        print("Computer chose:", computer_choices)
        if user_choices == computer_choices:
            print("It's a Tie")
            user_score += 1
            computer_score += 1
        elif user_choices == 0 and computer_choices == 2:
            print("You Win")
            user_score += 1
        elif user_choices == 2 and computer_choices == 0:
             print("You Lose")
             computer_score += 1
        elif user_choices > computer_choices:
            print("You Win")
            user_score += 1
        elif user_choices < computer_choices:
            print("You Lose")
            computer_score += 1
        print("Your score:", user_score)
        print("Computer score:", computer_score)
    Play_again = input("You want toPlay again? (yes/no): ")
print("Final Scores - Your score:", user_score, "Computer score:", computer_score)
if user_score > computer_score:
    print("Congratulations!. You win the Game.")
else:
    print("Computer win the Game. Better luck next time!")
print("Game Over")