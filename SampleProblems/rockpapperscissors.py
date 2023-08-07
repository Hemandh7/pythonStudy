import random

def get_user_choice():
    while True:
        user_input = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower()
        if user_input in ['rock', 'paper', 'scissors', 'q']:
            return user_input
        else:
            print("Invalid choice. Please enter 'rock', 'paper', 'scissors', or 'q' to quit.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif user_choice == 'rock' and computer_choice == 'scissors':
        return "user"
    elif user_choice == 'scissors' and computer_choice == 'paper':
        return "user"
    elif user_choice == 'paper' and computer_choice == 'rock':
        return "user"
    else:
        return "computer"

def display_score(user_wins, computer_wins, draws):
    print(f"Score: User - {user_wins}, Computer - {computer_wins}, Draws - {draws}")

def main():
    user_wins = 0
    computer_wins = 0
    draws = 0

    while True:
        user_choice = get_user_choice()
        if user_choice == 'q':
            print("Thanks for playing. Final Score:")
            break

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        if result == "draw":
            draws += 1
            print("It's a draw!")
        elif result == "user":
            user_wins += 1
            print("You win!")
        else:
            computer_wins += 1
            print("Computer wins!")

        display_score(user_wins, computer_wins, draws)

if __name__ == "__main__":
    main()
