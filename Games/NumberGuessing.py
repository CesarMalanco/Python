# Author: reDragonCoder

import random
import tkinter as tk
from tkinter import messagebox

class GuessingGame:
    def __init__(self, root):
        self.root=root
        self.root.title("Number Guessing Game")
        self.root.config(bg="#1e1e1e")

        window_width=500
        window_height=300
        screen_width=root.winfo_screenwidth()
        screen_height=root.winfo_screenheight()
        position_x=(screen_width//2)-(window_width//2)
        position_y=(screen_height//2)-(window_height//2)
        root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")


        self.number_to_guess=random.randint(0, 100)
        self.chances=7
        self.guess_counter=0

        self.label=tk.Label(root, text="\nYou have 7 attempts to guess the number from 0 to 100", font=("Arial", 14), bg="#1e1e1e", fg="white", pady=10)
        self.label.pack()

        self.entry=tk.Entry(root, font=("Arial", 14), bg="#333333", fg="white", bd=2, insertbackground="white", justify='center')
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", lambda event: self.check_guess()) 

        self.guess_button=tk.Button(root, text="Guess", command=self.check_guess, font=("Arial", 14), bg="#00aaff", fg="white", bd=2)
        self.guess_button.pack(pady=5)

        self.result_label=tk.Label(root, text="", font=("Arial", 14), bg="#1e1e1e", fg="white", pady=10)
        self.result_label.pack()

        self.reset_button=tk.Button(root, text="Restart game", command=self.restart_game, font=("Arial", 14), bg="#ff5050", fg="white", bd=2)
        self.reset_button.pack(pady=5)
    
    def check_guess(self):
        try:
            guess=int(self.entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please introduce a valid number")
            return
        
        self.guess_counter+=1

        if guess==self.number_to_guess:
            self.result_label.config(text=f"Correct! The number is {self.number_to_guess}. You guess it on the {self.guess_counter} attempt")
            self.disable_widgets()
        elif self.guess_counter>=self.chances:
            self.result_label.config(text=f"Sorry, you've used all your chances. The number was {self.number_to_guess}")
            self.disable_widgets()
        elif guess>self.number_to_guess:
            self.result_label.config(text="Your guess is higher")
        else:
            self.result_label.config(text="Your guess is lower")
    
    def disable_widgets(self):
        self.entry.config(state='disabled')
        self.guess_button.config(state='disabled')
    
    def restart_game(self):
        self.number_to_guess=random.randint(0, 100)
        self.guess_counter=0
        self.entry.config(state='normal')
        self.entry.delete(0, tk.END)
        self.guess_button.config(state='normal')
        self.result_label.config(text="")

if __name__ == "__main__":
    root=tk.Tk()
    game=GuessingGame(root)
    root.mainloop()