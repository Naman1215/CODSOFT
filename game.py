import random
import time

def rock_paper_scissors():
    """
    A complete Rock, Paper, Scissors game with score tracking.
    """
    user_score = 0
    computer_score = 0
    options = ['rock', 'paper', 'scissors']

    print("--- Welcome to Rock, Paper, Scissors! ---")

    while True:
        # --- Get User and Computer Choices ---
        user_choice = input("\nChoose Rock, Paper, or Scissors: ").lower()
        
        # Validate user input
        if user_choice not in options:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(options)
        
        # --- Display Choices ---
        print(f"\nYour choice: {user_choice.capitalize()} 🗿📄✂️")
        print("Computer is choosing...")
        time.sleep(1) # Add a small delay for suspense
        print(f"Computer's choice: {computer_choice.capitalize()}")

        # --- Game Logic ---
        result = ""
        if user_choice == computer_choice:
            result = "It's a tie! 🤝"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            result = "You win this round! 🎉"
            user_score += 1
        else:
            result = "Computer wins this round! 💻"
            computer_score += 1
            
        # --- Display Result and Score ---
        print(f"\nResult: {result}")
        print(f"Score -> You: {user_score} | Computer: {computer_score}")
        print("-----------------------------------------")

        # --- Play Again ---
        play_again = input("Play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break
            
    # --- End of Game ---
    print("\nThanks for playing!")
    print(f"🏆 Final Score -> You: {user_score} | Computer: {computer_score} 🏆")


# Run the game
if __name__ == "__main__":
    rock_paper_scissors()