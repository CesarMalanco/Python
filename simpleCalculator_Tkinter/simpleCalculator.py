# Author: reDragonCoder

# Libraries
import tkinter as tk
from tkinter import messagebox

# Execution(w/GUI)
def click(event):
    text=event.widget.cget("text")
    if(text=='='):
        try:
            result=eval(str(screen.get()))
            screen.delete(0, tk.END)
            screen.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Operation")
            screen.delete(0, tk.END)
    elif text=='C':
        screen.delete(0, tk.END)
    else:
        screen.insert(tk.END, text)

root=tk.Tk()
root.title("Calculator")
root.iconphoto(False, tk.PhotoImage(file='calculatorImg.png'))

root.configure(bg="black")

screen=tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="solid")
screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons=[
    "7", "8", "9", "+",
    "4", "5", "6", "-",
    "1", "2", "3", "*",
    "C", "0", "=", "/"
]

row=1
col=0

for btn in buttons:
    if btn in ["+", "-", "*", "/", "=", "C"]:
        button=tk.Button(root, text=btn, font=("Arial", 18), relief="solid", padx=20, pady=20, bg="orange", fg="white")
    else:
        button=tk.Button(root, text=btn, font=("Arial", 18), relief="solid", padx=20, pady=20, bg="gray", fg="white")
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", click)
    col+=1
    if col>3:
        col=0
        row+=1

root.mainloop()