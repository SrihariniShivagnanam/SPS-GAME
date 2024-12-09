import tkinter as tk
import random

# Initialize the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.configure(bg="light yellow")

# Game variables
choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0
round_count = 0


# Functions
def play(choice):
    global user_score, computer_score, round_count
    round_count += 1

    computer_choice = random.choice(choices)
    result = determine_winner(choice, computer_choice)

    if result == "Win":
        user_score += 1
        result_text.set(f"You Win! {choice} beats {computer_choice}.")
    elif result == "Lose":
        computer_score += 1
        result_text.set(f"You Lose! {computer_choice} beats {choice}.")
    else:
        result_text.set(f"It's a Draw! Both chose {choice}.")

    update_scores()
    if round_count >= 5:  # End game after 5 rounds
        end_game()


def determine_winner(user, computer):
    if user == computer:
        return "Draw"
    elif (user == "Rock" and computer == "Scissors") or \
            (user == "Paper" and computer == "Rock") or \
            (user == "Scissors" and computer == "Paper"):
        return "Win"
    else:
        return "Lose"


def update_scores():
    score_text.set(f"Your Score: {user_score} | Computer Score: {computer_score}")


def end_game():
    if user_score > computer_score:
        final_result = "Congratulations! You Won the Game!"
    elif user_score < computer_score:
        final_result = "Game Over! You Lost the Game!"
    else:
        final_result = "It's a Tie! Well Played!"

    result_text.set(final_result)
    # Disable buttons
    rock_button.config(state=tk.DISABLED)
    paper_button.config(state=tk.DISABLED)
    scissors_button.config(state=tk.DISABLED)


# GUI Elements
result_text = tk.StringVar()
result_text.set("Make your choice!")
score_text = tk.StringVar()
score_text.set("Your Score: 0 | Computer Score: 0")

# Labels
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 16), fg="blue", bg="lightblue", pady=10)
result_label.pack(pady=20)

score_label = tk.Label(root, textvariable=score_text, font=("Arial", 14), bg="lightblue", pady=5)
score_label.pack(pady=10)

# Buttons
rock_button = tk.Button(root, text="Rock", font=("Arial", 12), bg="white", fg="black", width=12, height=2,
                        relief="raised", borderwidth=3, command=lambda: play("Rock"))
rock_button.pack(side=tk.LEFT, padx=20, pady=10)

paper_button = tk.Button(root, text="Paper", font=("Arial", 12), bg="white", fg="black", width=12, height=2,
                         relief="raised", borderwidth=3, command=lambda: play("Paper"))
paper_button.pack(side=tk.LEFT, padx=20, pady=10)

scissors_button = tk.Button(root, text="Scissors", font=("Arial", 12), bg="white", fg="black", width=12, height=2,
                            relief="raised", borderwidth=3, command=lambda: play("Scissors"))
scissors_button.pack(side=tk.LEFT, padx=20, pady=10)

# Run the application
root.mainloop()
