import tkinter as tk
from tkinter import messagebox, filedialog
import random, string

# Massive pre-defined words list with Gen Z words
adjectives = [
    "Cool", "Happy", "Brave", "Clever", "Mighty", "Swift", "Shiny", "Funky", "Chill", "Bold", "Energetic", "Witty", "Gentle", "Lively", "Daring", "Fearless", "Vibrant", "Jolly", "Sly", "Majestic",
    "Savage", "Lit", "Dope", "Epic", "Legendary", "Hyped", "Rad", "Snazzy", "Zesty", "Quirky", "Slick", "Drippy", "Woke", "Vibey", "Slayin", "Juicy", "Edgy", "Fierce", "Spicy", "Gassed"
]

nouns = [
    "Tiger", "Dragon", "Falcon", "Wizard", "Knight", "Panda", "Wolf", "Phoenix", "Ninja", "Bear", "Lion", "Eagle", "Panther", "Samurai", "Fox", "Cheetah", "Hawk", "Gladiator", "Rhino", "Viking",
    "Goat", "Beast", "Sniper", "Baller", "Maverick", "Storm", "Shadow", "Rebel", "Champion", "Outlaw", "Bandit", "Ghost", "Rogue", "Maverick", "Alpha", "Zephyr", "Blaze", "Titan", "Drifter", "Cyclone"
]

def generate_usernames():
    try:
        count = int(entry_count.get())
        length = int(entry_length.get()) if entry_length.get() else None
        usernames = []
        
        for _ in range(count):
            name = random.choice(adjectives) + random.choice(nouns)
            if var_numbers.get():
                name += str(random.randint(10, 99))
            if var_specials.get():
                name += random.choice(string.punctuation)
            usernames.append(name[:length] if length else name)
        
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, "\n".join(usernames))
    except ValueError:
        messagebox.showerror("Invalid Input", "Enter valid numbers for count and length.")

def save_usernames():
    usernames = text_output.get("1.0", tk.END).strip()
    if not usernames:
        return messagebox.showwarning("No Usernames", "Nothing to save!")
    
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(usernames)
        messagebox.showinfo("Saved", "Usernames saved successfully!")

# UI Setup
root = tk.Tk()
root.title("Username Generator")
root.geometry("400x400")

tk.Label(root, text="Number of Usernames:").pack()
entry_count = tk.Entry(root)
entry_count.pack()

tk.Label(root, text="Max Length (optional):").pack()
entry_length = tk.Entry(root)
entry_length.pack()

var_numbers, var_specials = tk.BooleanVar(value=True), tk.BooleanVar(value=False)
tk.Checkbutton(root, text="Include Numbers", variable=var_numbers).pack()
tk.Checkbutton(root, text="Include Special Characters", variable=var_specials).pack()

tk.Button(root, text="Generate", command=generate_usernames, bg="blue", fg="white").pack(pady=5)
text_output = tk.Text(root, height=10, width=40)
text_output.pack()
tk.Button(root, text="Save", command=save_usernames, bg="green", fg="white").pack(pady=5)

root.mainloop()