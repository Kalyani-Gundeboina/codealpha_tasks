import tkinter as tk

def get_response(user_input):
    user_input = user_input.lower()
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."

def send_message():
    message = user_input.get()
    if message.strip() == "":
        return
    chat_box.insert(tk.END, "You: " + message)
    response = get_response(message)
    chat_box.insert(tk.END, "Bot: " + response)
    user_input.delete(0, tk.END)

window = tk.Tk()
window.title("Simple Rule-Based Chatbot")
window.geometry("400x400")

chat_box = tk.Listbox(window, width=50, height=15)
chat_box.pack(pady=10)

user_input = tk.Entry(window, width=40)
user_input.pack(pady=5)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=5)

window.mainloop()
