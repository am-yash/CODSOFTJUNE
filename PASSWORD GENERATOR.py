import tkinter as tk
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    
    if password_length < 1:
        password_result.config(text="Invalid length")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    
    password_result.config(text=password)

#  main window
root = tk.Tk()
root.title("Password Generator")

#  password length
length_label = tk.Label(root, text="Enter password length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

# button to generate the password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# generated password
password_result = tk.Label(root, text="", font=("Helvetica", 16))
password_result.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()
