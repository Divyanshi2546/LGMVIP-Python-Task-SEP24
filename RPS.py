import tkinter as tk
from random import choice
from tkinter import messagebox


# Function to determine the winner
def determine_winner(user_choice):
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = choice(options)

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
            (user_choice == 'Scissors' and computer_choice == 'Paper') or \
            (user_choice == 'Paper' and computer_choice == 'Rock'):
        result = "You win!"
    else:
        result = "Computer wins!"

    result_message = f"You chose {user_choice}\nComputer chose {computer_choice}\n{result}"
    messagebox.showinfo("Game Result", result_message)


# Function to handle button clicks
def user_choice(choice):
    determine_winner(choice)


# Set up the Tkinter window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("300x300")

# Add buttons for Rock, Paper, and Scissors
label = tk.Label(window, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14))
label.pack(pady=20)

rock_button = tk.Button(window, text="Rock", width=15, height=2, command=lambda: user_choice('Rock'))
rock_button.pack(pady=10)

paper_button = tk.Button(window, text="Paper", width=15, height=2, command=lambda: user_choice('Paper'))
paper_button.pack(pady=10)

scissors_button = tk.Button(window, text="Scissors", width=15, height=2, command=lambda: user_choice('Scissors'))
scissors_button.pack(pady=10)

# Run the Tkinter main loop
window.mainloop()
