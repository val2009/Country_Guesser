import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter.font as font


fenetre = tk.Tk()
fenetre.title("Country Guesser")
fenetre.attributes('-fullscreen', True)
a14 = "Arial", 14
a30 = "Arial", 30


def quitter():
    fenetre.quit()



exit = ttk.Button(fenetre, text="Exit", command=quitter, width=10, bootstyle=DANGER)
exit.grid(row=0, column=0, pady=20, padx=20)

start = ttk.Label(fenetre, text="Country Guesser", font=a30)
start.grid(row=0, column=0,  pady=150, padx=20)

fenetre.mainloop()