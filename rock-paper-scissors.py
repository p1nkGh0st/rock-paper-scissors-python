import random

print("🎮 Welcome to Rock-Paper-Scissors!")

# 1. Define the choices
options = ["rock", "paper", "scissors"]

# 2. Get user input and computer choice
user_choice = input("Enter rock, paper, or scissors: ").lower().strip()
computer_choice = random.choice(options)

# Check if the user entered a valid choice
if user_choice not in options:
    print(
        "❌ Invalid choice! Please run the program again and enter rock, paper, or scissors."
    )
else:
    print(f"\nYou: {user_choice}")
    print(f"Computer: {computer_choice}\n")

    # 3. Determine the winner
    if user_choice == computer_choice:
        print("🤝 It's a tie!")

    # Logic for User Win
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 You win!")

    # All other cases -> Computer Win
    else:
        print("💻 Computer wins! Better luck next time.")
