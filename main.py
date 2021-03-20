import tkinter as tk


root = tk.Tk()

def move_window(event):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

