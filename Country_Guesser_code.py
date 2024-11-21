import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import time as t
import pygame as pg
import random as r
from PIL import Image, ImageTk


fenetre = tk.Tk()
fenetre.title("Flag Guesser")
fenetre.attributes('-fullscreen', True)
a10 = "Arial", 10
a14 = "Arial", 14
a18 = "Arial", 18
a30 = "Arial", 30
a50 = "Arial", 50
a60 = "Arial", 60
style = ttk.Style()
style.configure("Button1.TButton", font=a18, padding=(10, 5))
style.configure("Button2.TButton", background="#c82333", bordercolor="#c82333", foreground="white", borderwidth=1, relief="solid", font=a18, padding=(10, 5))
style.map("Button2.TButton", background=[("active", "#c82333"), ("!disabled", "#c82333")], bordercolor=[("active", "#c82333"), ("!disabled", "#c82333")], foreground=[("active", "white"), ("!disabled", "white")],)

difficulty_selection = "30 drapeaux 'moyen'"
time_selection = 15
musique_selection = "Funky.1.mp3"
nocturne_selection = "Désactivé"
volume_selection = 50

for col in range(3): # Affiche les lignes et colonnes
    for row in range(9):
        cell = tk.Label(fenetre, text=f"Col {col}, Row {row}", borderwidth=1, relief="solid", width=0, height=0)
        cell.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

fenetre.columnconfigure(0, weight=6)
fenetre.columnconfigure(1, weight=12)
fenetre.columnconfigure(2, weight=1)

fenetre.rowconfigure(0, weight=4)
fenetre.rowconfigure(1, weight=8)
fenetre.rowconfigure(2, weight=1)
fenetre.rowconfigure(3, weight=1)
fenetre.rowconfigure(4, weight=1)
fenetre.rowconfigure(5, weight=1)
fenetre.rowconfigure(6, weight=6)
fenetre.rowconfigure(7, weight=4)
fenetre.rowconfigure(8, weight=4)

pg.mixer.init()
pg.mixer.music.load("Funky.1.mp3")
pg.mixer.music.play(loops=-1)


def quitter():
    if messagebox.askokcancel("Exit", "Voulez-vous vraiment quitter ?"):
        fenetre.quit()   


def difficulty_save(event):
    global difficulty_selection
    difficulty_selection = difficulty_combobox.get()


def time_save(event):
    global time_selection
    time_selection = time_combobox.get()

def clear_selection_difficulty(event):
    difficulty_combobox.select_clear()

def clear_selection_time(event):
    time_combobox.select_clear()

def commencer():
    global time_selection
    game_fenetre = tk.Toplevel()
    game_fenetre.title("Flag Guesser - Game")
    game_fenetre.attributes('-fullscreen', True)

    def countdown():
        nonlocal time_left
        if time_left > 0:
            time_left -= 1
            timer_label.configure(text=str(time_left))
            game_fenetre.after(1000, countdown)

    for col in range(3):
        for row in range(3):
            cell = tk.Label(game_fenetre, text=f"Col {col}, Row {row}", borderwidth=1, relief="solid", width=0, height=0)
            cell.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    
    game_fenetre.columnconfigure(0, weight=20)
    game_fenetre.columnconfigure(1, weight=6)
    game_fenetre.columnconfigure(2, weight=1)

    game_fenetre.rowconfigure(0, weight=3)
    game_fenetre.rowconfigure(1, weight=3)
    game_fenetre.rowconfigure(2, weight=6)

    exit_game = ttk.Button(game_fenetre, text="Exit", command=game_fenetre.destroy, width=10, bootstyle=DANGER)
    exit_game.grid(sticky="ne", column=2, row=0, pady=0, padx=0)

    timer_label = ttk.Label(game_fenetre, text="",font=a50)
    timer_label.grid(row=0, column=1, padx=0, sticky="sw")

    score_label = ttk.Label(game_fenetre, text="Score", font=a30)
    score_label.grid(column=0, row=0, sticky="nw", padx= 20)

    guess_label = ttk.Label(game_fenetre, text="Devine le drapeau : ", font=a30)
    guess_label.grid(column=0, row=0, sticky="sw", padx= 20)

    nameflag_combobox = ttk.Combobox(game_fenetre, )

    
    if difficulty_selection == "30 drapeaux 'moyen'":
        image_originale = Image.open("Vietnam.png")
        image_redimensionnee = image_originale.resize((700, 466))
        image_vietnam = ImageTk.PhotoImage(image_redimensionnee)
        label_vietnam = ttk.Label(game_fenetre, image=image_vietnam)
        label_vietnam.image = image_vietnam
        label_vietnam.grid(column=0, row=1, sticky="w", padx=(300, 0), pady=0)

    time_left = int(time_selection) + 1
    timer_label.configure(text=str(time_left))
    countdown()

    


def settings():
    settings_fenetre = tk.Toplevel()
    settings_fenetre.title("Flag Guesser - Settings")
    settings_fenetre.attributes('-fullscreen', True)

    settings_fenetre.columnconfigure(0, weight=9)
    settings_fenetre.columnconfigure(1, weight=1)

    settings_fenetre.rowconfigure(0, weight=10)
    settings_fenetre.rowconfigure(1, weight=2)
    settings_fenetre.rowconfigure(2, weight=2)
    settings_fenetre.rowconfigure(3, weight=2)
    settings_fenetre.rowconfigure(4, weight=2)
    settings_fenetre.rowconfigure(5, weight=35)

    def clear_selection_musique(event):
        musique_combobox.select_clear()
    
    def clear_selection_nocturne(event):
        nocturne_combobox.select_clear()

    def change_musique(event):
        pg.mixer.music.load(musique_combobox.get())
        pg.mixer.music.play(loops=-1)

    def volume(event):
        pg.mixer.music.set_volume(volume_scale.get()/100)

    def apply_custom_styles():
        style.configure("Button1.TButton", bootstyle=DANGER, font=a18, padding=(10, 5))
        style.configure("Button2.TButton", background="#c82333", bordercolor="#c82333", foreground="white", borderwidth=1, relief="solid", font=a18, padding=(10, 5))
        style.map("Button2.TButton", background=[("active", "#c82333"), ("!disabled", "#c82333")], bordercolor=[("active", "#c82333"), ("!disabled", "#c82333")], foreground=[("active", "white"), ("!disabled", "white")],)
    
    def nocturne_mode(event):
        if nocturne_combobox.get() == "Activé":
            style.theme_use("darkly") # Change tout les widget en foncés
            apply_custom_styles()            
        elif nocturne_combobox.get() == "Désactivé":
            style.theme_use("litera")
            apply_custom_styles()

    def settings_fenetre_exit():
        global musique_selection, nocturne_selection, volume_selection
        musique_selection = musique_combobox.get()
        nocturne_selection = nocturne_combobox.get()
        volume_selection = volume_scale.get()
        settings_fenetre.destroy()
    

    exit_settings = ttk.Button(settings_fenetre, text="Exit", command=settings_fenetre_exit, width=10, bootstyle=DANGER)
    exit_settings.grid(sticky="ne", row=0, column=1, pady=0, padx=0)

    paramètre_label = ttk.Label(settings_fenetre, text="Paramètres", font=a60)
    paramètre_label.grid(sticky="n", row=0, column=0, pady=(50, 0), padx=(50, 0))

    musique_label = ttk.Label(settings_fenetre, text="Choix de la musique :", font=a18)
    musique_label.grid(sticky="w", row=1, column=0, pady=(0, 0), padx=(300, 0))

    musique_combobox = ttk.Combobox(settings_fenetre, values = ["Chill.1.mp3", "Chill.2.mp3", "Enérgique.1.mp3", "Enérgique.2.mp3", "Funky.1.mp3", "Funky.2.mp3","Pop.1.mp3", "Pop.2.mp3", "Phonk.1.mp3", "Phonk.2.mp3"], state = "readonly", width=10, font=a10)
    musique_combobox.grid(sticky="e", row=1, column=0, pady=(0, 0), padx=(0, 750))
    musique_combobox.set(musique_selection)
    musique_combobox.bind("<FocusIn>", clear_selection_musique)
    musique_combobox.bind("<<ComboboxSelected>>", change_musique)

    volume_label = ttk.Label(settings_fenetre, text="Volume musique :", font=a18)
    volume_label.grid(sticky="w", row=2, column=0, pady=(0, 0), padx=(300, 0))

    volume_scale = ttk.Scale(settings_fenetre, from_=0, to=100, orient="horizontal", command = volume, length=150)
    volume_scale.grid(sticky="e", row=2, column=0, pady=(0, 0), padx=(0, 740))
    volume_scale.set(volume_selection)

    nocturne_label = ttk.Label(settings_fenetre, text="Mode nocturne :", font=a18)
    nocturne_label.grid(sticky="w", row=3, column=0, pady=(0, 0), padx=(300, 0))
    
    nocturne_combobox = ttk.Combobox(settings_fenetre, values = ["Désactivé", "Activé"], state="readonly", width=10, font= a10)
    nocturne_combobox.grid(sticky="e", row=3, column=0, pady=(0, 0), padx=(0, 810))
    nocturne_combobox.set(nocturne_selection)
    nocturne_combobox.bind("<FocusIn>", clear_selection_nocturne)
    nocturne_combobox.bind("<<ComboboxSelected>>", nocturne_mode)
    


exit = ttk.Button(fenetre, text="Exit", command=quitter, width=10, bootstyle=DANGER)
exit.grid(sticky="ne", row=0, column=2, pady=0, padx=0)

start = ttk.Label(fenetre, text="Flag Guesser", font=a60)
start.grid(sticky="sw", row=1, column=1,  pady=(0, 25), padx=(190, 0))

play = ttk.Button(fenetre, text="Jouer", command=commencer, width=10, style="Button1.TButton")
play.grid(sticky="nw", row=2, column=1, pady=(0, 0), padx=(340, 0))

paramètre = ttk.Button(fenetre, text="Paramètres", command=settings, width=10, style="Button1.TButton")
paramètre.grid(sticky="nw", row=3, column=1, pady=(0, 0), padx=(340, 0))

Quitter_buton = ttk.Button(fenetre, text="Quitter", command = quitter, width=10, style="Button2.TButton")
Quitter_buton.grid(sticky="nw", column=1, row=4, padx=(340, 0), pady=(0, 0))



explain_difficulty = ttk.Label(fenetre, text="Choix de la difficulté.", font=a14)
explain_difficulty.grid(sticky="w", row=7, column=0,  pady=(0, 30), padx=(10, 0))

list_difficulty = ["20 drapeaux 'facile'", "30 drapeaux 'moyen'", "40 drapeaux 'difficile'"]
difficulty_combobox = ttk.Combobox(fenetre, values = list_difficulty, state = "readonly", width=18, font=a10)
difficulty_combobox.grid(sticky="sw", row=7, column=0, pady=(0, 15), padx=(10, 0))
difficulty_combobox.set("30 drapeaux 'moyen'")
difficulty_combobox.bind("<FocusIn>", clear_selection_difficulty)
difficulty_combobox.bind("<<ComboboxSelected>>", difficulty_save)


explain_time = ttk.Label(fenetre, text="Temps par round en seconde.", font=a14)
explain_time.grid(sticky="nw", row=8, column=0,  pady=(0, 0), padx=(10, 0))

time_combobox = ttk.Combobox(fenetre, values=[5, 10, 15, 20, 25, 30], state="readonly",  width=5, font=a10)
time_combobox.grid(sticky="w", row=8, column=0, pady=(10, 0), padx=(10, 0))
time_combobox.set(15)
time_combobox.bind("<FocusIn>", clear_selection_time)
time_combobox.bind("<<ComboboxSelected>>", time_save)



fenetre.mainloop()