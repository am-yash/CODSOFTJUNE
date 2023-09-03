import tkinter as tk
import random

def play_game(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    result_label.config(text=f"Computer chose {computer_choice}")
    
    if user_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result_label.config(text="You win!")
    else:
        result_label.config(text="Computer wins!")

def play_again():
    result_label.config(text="")
    rock_button.config(state=tk.NORMAL)
    paper_button.config(state=tk.NORMAL)
    scissors_button.config(state=tk.NORMAL)
    play_again_button.pack_forget()

# main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

#display the result
result_label = tk.Label(root, text="",  font=("Courier", 16 ))
result_label.pack(pady=25)

# buttons for the user's choices
rock_button = tk.Button(root, text="Rock", width=10, command=lambda: user_choice("Rock"),bg="#1a8cff")
paper_button = tk.Button(root, text="Paper", width=10, command=lambda: user_choice("Paper"),bg="#1a8cff")
scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: user_choice("Scissors"),bg="#1a8cff")

rock_button.pack()
paper_button.pack()
scissors_button.pack()

# Play Again button
play_again_button = tk.Button(root, text="Play Again", width=10, command=play_again,bg="#2eb82e")

# Function of  user's choice
def user_choice(choice):
    play_game(choice)
    rock_button.config(state=tk.DISABLED)
    paper_button.config(state=tk.DISABLED)
    scissors_button.config(state=tk.DISABLED)
    play_again_button.pack()


root.mainloop()
