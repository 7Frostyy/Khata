import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog


def createWidgets():

    global textArea
    textArea = Text(root)
    textArea.grid(sticky = N+E+S+W)

    menuBar = Menu(root)
    root.config(menu=menuBar)
    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="New", command="")
    fileMenu.add_command(label="Open", command="")
    fileMenu.add_command(label="Save", command="")
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command="")
    menuBar.add_cascade(label="File", menu=fileMenu)
root = tk.Tk()
root.title("Notepad")
file = None

createWidgets()

root.mainloop()
