import random

print("---------- ROCK PAPER SCISSORS ----------")

user_score = 0
computer_score = 0
game_data = {1 : "rock",2 : "paper",3 : "scissors"}

while True:
    print("\n1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choice = input("Enter your choice number: ")
    if choice.isdigit():
        ch = int(choice)
        if 1 <= ch <= 3:
            computer_choice = random.randint(1, 3)
            print(f"\nComputer choice: {game_data[computer_choice]}")
            print(f"Your choice: {game_data[ch]}")
            if computer_choice == ch:
                print("Tie")
            elif (ch == 1 and computer_choice == 3) or (ch == 2 and computer_choice == 1) or (ch == 3 and computer_choice == 2):
                print("You Win")
                user_score += 1
            else:
                print("Computer Wins")
                computer_score += 1

            continue_game = input("\nDo you want to play again? (y/n): ").lower()
            if continue_game == "n":
                print(f"\nUser Score: {user_score}")
                print(f"Computer Score: {computer_score}")
                print("Thank you for playing!")
                break
        else:
            print("Invalid Choice")
    else:
        print("Invalid Input")