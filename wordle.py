import tkinter as tk
from tkinter import messagebox
import random
# Test
# Word list for the game
word_list = ["apple", "grape", "lemon", "melon", "berry", "peach", "mango", "plane"]
max_attempts = 6  # Maximum number of guesses allowed

# Function to check the user's guess
def check_guess():
    global attempts
    guess = entry.get().lower()
    if len(guess) != 5:
        messagebox.showerror("Error", "Please enter a 5-letter word.")
        return

    if guess not in word_list:
        messagebox.showerror("Error", "Not in word list.")
        return

    display_result(guess)
    attempts += 1

    if guess == word:
        messagebox.showinfo("Congratulations", "You guessed the word!")
        new_game()
    elif attempts >= max_attempts:
        messagebox.showinfo("Game Over", "You've run out of guesses! The word was '{word}'.")
        new_game()

# Function to display the result
def display_result(guess):
    for i in range(5):
        label = result_labels[attempts][i]
        letter = guess[i]
        if letter == word[i]:
            label.config(text=letter, bg="green")
        elif letter in word:
            label.config(text=letter, bg="yellow")
        else:
            label.config(text=letter, bg="grey")




# Function to start a new game
def new_game():
    global word, attempts, result_labels
    word = random.choice(word_list)
    attempts = 0
    entry.delete(0, tk.END)

    # Clear previous results
    for row in result_labels:
        for label in row:
            label.config(text="", bg="white")

# Setup GUI
root = tk.Tk()
root.title("Wordle Game")

frame = tk.Frame(root)
frame.pack(pady=20)

entry = tk.Entry(frame, font=("Arial", 18), width=5)
entry.grid(row=0, column=0, padx=10)

check_button = tk.Button(frame, text="Check", command=check_guess)
check_button.grid(row=0, column=1)

result_frame = tk.Frame(root)
result_frame.pack(pady=20)

result_labels = [
    [tk.Label(result_frame, text="", font=("Arial", 18), width=4, height=2, bg="white") for _ in range(5)]
    for _ in range(max_attempts)
]
for row_index, row in enumerate(result_labels):
    for col_index, label in enumerate(row):
        label.grid(row=row_index, column=col_index, padx=5)

new_game_button = tk.Button(root, text="New Game", command=new_game)
new_game_button.pack(pady=10)

new_game()
root.mainloop()
