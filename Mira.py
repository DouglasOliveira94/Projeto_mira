import tkinter as tk
import pygetwindow

def get_screen_center():
    screen = pygetwindow.getWindowsWithTitle('')[0]  # Obtém a janela da tela principal
    center_x = screen.left + screen.width / 2 - 3
    center_y = screen.top + screen.height / 2 - 413  # Ajuste para mover o ponto mais para cima
    return center_x, center_y

def move_window_to_center(window):
    center_x, center_y = get_screen_center()
    window.geometry(f"+{int(center_x)}+{int(center_y)}")

def move_red_dot(event):
    canvas.coords(red_dot, event.x-5, event.y-55, event.x+5, event.y-45)  # Ajuste para mover o ponto mais para cima

root = tk.Tk()
root.overrideredirect(True)
root.attributes('-topmost', True)
root.geometry("5x5")
root.configure(bg='black')
root.bind("<B1-Motion>", move_red_dot)

canvas = tk.Canvas(root, width=5, height=5, bg='black', highlightthickness=0)
canvas.pack()

red_dot = canvas.create_oval(1, 1, 4, 4, fill='red')

move_window_to_center(root)

root.mainloop()
