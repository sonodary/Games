import tkinter as tk
from PingPong_Game.main import pingpong
from Snake_Game.main import snakegame
from Turtle_Crossing_Game.main import turtlegame

FONT = ("Courier", 15, "normal")

app = tk.Tk()
app.title("Games")
app.configure(background="#0A0F1E")
app.geometry("800x600")
canvas = tk.Canvas(app, width=800, height=300, highlightthickness=0, bg="#0A0F1E")
canvas.grid(column=0, row=0, columnspan=3)
canvas.create_text(400, 200, text="Choose a game to play", fill="white", font=("Courier", "30"))

# Button to play PingPong
pingPong_button = tk.Button(text="Ping Pong",  highlightthickness=0, width=20, height=3, font=FONT, fg="black", command=pingpong)
pingPong_button.grid(column=1, row=1)
# Snake game
snake_button = tk.Button(text="Snake",  highlightthickness=0, width=20, height=3, font=FONT, command=snakegame)
snake_button.grid(column=0, row=2)
# Turtle Game
turtle_button = tk.Button(text="Turtle",  highlightthickness=0, width=20, height=3, font=FONT, command=turtlegame)
turtle_button.grid(column=2, row=2)

app.mainloop()
