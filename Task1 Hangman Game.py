import tkinter as tk
import random


words = ["apple", "brain", "chair", "dance", "eagle"]
secret_word = random.choice(words)
guessed = []
attempts_left = 6


window = tk.Tk()
window.title("Hangman Game")
window.geometry("350x300")


display_word = tk.StringVar()
message = tk.StringVar()
attempts_msg = tk.StringVar(value=f"Attempts Left: {attempts_left}")

def update_word_display():
    result = ""
    for ch in secret_word:
        if ch in guessed:
            result += ch + " "
        else:
            result += "_ "
    display_word.set(result.strip())


def make_guess():
    global attempts_left

    letter = input_box.get().lower()
    input_box.delete(0, tk.END)

    if len(letter) != 1 or not letter.isalpha():
        message.set("❗ Enter a single alphabet")
        return

    if letter in guessed:
        message.set("⚠️ Already guessed")
        return

    guessed.append(letter)

    if letter in secret_word:
        message.set("✅ Correct!")
    else:
        attempts_left -= 1
        attempts_msg.set(f"Attempts Left: {attempts_left}")
        message.set("❌ Wrong!")

    update_word_display()

    if all(l in guessed for l in secret_word):
        message.set(f"🎉 You Win! Word: {secret_word}")
        guess_btn.config(state="disabled")
    elif attempts_left == 0:
        message.set(f"💀 Game Over! Word: {secret_word}")
        guess_btn.config(state="disabled")


tk.Label(window, text="Hangman Game", font=("Helvetica", 18)).pack(pady=10)
tk.Label(window, textvariable=display_word, font=("Courier", 24)).pack(pady=10)
tk.Label(window, textvariable=attempts_msg, font=("Helvetica", 12)).pack()

input_box = tk.Entry(window, font=("Helvetica", 14), width=5, justify="center")
input_box.pack(pady=5)

guess_btn = tk.Button(window, text="Guess", command=make_guess)
guess_btn.pack(pady=5)

tk.Label(window, textvariable=message, font=("Helvetica", 12), fg="blue").pack(pady=10)


update_word_display()
window.mainloop()
