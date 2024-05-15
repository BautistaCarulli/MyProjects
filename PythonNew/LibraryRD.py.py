import random
import tkinter as tk
from tkinter import scrolledtext

adjectives = ["brillante", "sombrío", "misterioso", "luminosa", "silencioso"]
nouns = ["noche", "mar", "bosque", "estrella", "viento"]
verbs = ["susurra", "grita", "canta", "baila", "fluye"]
adverbs = ["suavemente", "intensamente", "misteriosamente", "elegantemente", "bruscamente"]
prepositions = ["en", "sobre", "bajo", "entre", "alrededor de"]

def generate_poem():
    lines = []
    for _ in range(4): 
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        verb = random.choice(verbs)
        adverb = random.choice(adverbs)
        preposition = random.choice(prepositions)
        noun2 = random.choice(nouns)
        
        line = f"El {adjective} {noun} {verb} {adverb} {preposition} el {noun2}."
        lines.append(line)
    
    return "\n".join(lines)

def display_poem():
    poem = generate_poem()
    poem_display.delete('1.0', tk.END)
    poem_display.insert(tk.INSERT, poem)

root = tk.Tk()
root.title("Generador de Poesía Aleatoria")

title_label = tk.Label(root, text="Generador de Poesía Aleatoria", font=("Helvetica", 16, "bold"))
generate_button = tk.Button(root, text="Generar Poema", command=display_poem)
poem_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10, font=("Helvetica", 12))

title_label.pack(pady=10)
generate_button.pack(pady=5)
poem_display.pack(pady=10)

root.mainloop()
