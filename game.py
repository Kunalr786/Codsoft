import random
import tkinter as tk
from tkinter import messagebox

# Game logic
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    # User input
    user_choice = choice_var.get()
    # Computer selection
    computer_choice = random.choice(["rock", "paper", "scissors"])
    # Determine the winner
    result = determine_winner(user_choice, computer_choice)
    # Display result
    messagebox.showinfo("Result", f"You chose {user_choice}, computer chose {computer_choice}.\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissors")

# User interface
choice_var = tk.StringVar()
choices = ["rock", "paper", "scissors"]
choice_label = tk.Label(root, text="Choose rock, paper, or scissors:")
choice_label.pack()
for choice in choices:
    choice_button = tk.Radiobutton(root, text=choice, variable=choice_var, value=choice)
    choice_button.pack()

play_button = tk.Button(root, text="Play", command=play_game)
play_button.pack()

root.mainloop()
