import tkinter as tk
from tkinter import ttk, Text, WORD
import scraper

MOOD_MAPPING = {
    'Happy': ['comedy', 'musical', 'feel-good'],
    'Sad': ['drama', 'tragedy'],
    'Adventurous': ['action', 'adventure', 'fantasy'],
    'Relaxed': ['drama', 'romance', 'slice of life']
} 


def fetch_and_recommend():
    mood = mood_combobox.get()
    global movies
    movies = scraper.fetch_movies_from_imdb(MOOD_MAPPING[mood])
    for movie in movies:
        title, year, desc = movie
        recommendations_list.insert(tk.END, f"{title} ({year}) - {desc} \n\n\n")

app = tk.Tk()
app.title("IMDB Movie Recommender")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label = tk.Label(app, text="Select your mood:")
label.grid(row=0, column=1, sticky=tk.W, pady=0)

mood_combobox = ttk.Combobox(app, values=list(MOOD_MAPPING.keys()))
mood_combobox.grid(row=0, column=4, pady=0)

recommend_button = tk.Button(app, text="Recommend Movies", command=fetch_and_recommend)
recommend_button.grid(row=4, column=0, columnspan=2, pady=5)

recommendations_list = Text(frame, wrap=WORD)
recommendations_list.grid(row=5, column=0, columnspan=2, pady=0)

app.mainloop()

