from importlib.metadata import files
import tkinter as tk
from tkinter import *
from tkinter import Canvas, Frame, filedialog, Text, PhotoImage
import os
from PIL import Image, ImageTk

root = tk.Tk()
root.title("GUI Application")
root.iconphoto(True, PhotoImage(file='alatoo.png'))
files = []


def open_file():
    filename = filedialog.askopenfilename(filetypes=(("Images",
                                                      "*.jpeg;*.jpg;*.png"),))
    files.append(filename)
    print(filename)
    for file in files:
        tag = tk.Label(canvas, text=file, bg="gray")
        tag.pack()


def run_file():
    for file in files:
        os.startfile(file)


def edit_file():
    for file in files:
        img = Image.open(file)
        img = img.resize((1080, 1080))
        img = img.convert("1")
        img.save(file)

def exit():
    root.quit()


root.rowconfigure(0, minsize=400, weight=1)
root.columnconfigure(1, minsize=400, weight=1)

canvas = tk.Canvas(root)
frame = tk.Frame(root, relief=tk.RAISED, bd=2)

openFile = tk.Button(frame, text="Select file", command=open_file)
openFile.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

runFile = tk.Button(frame, text="Open file", command=run_file)
runFile.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

editFile = tk.Button(frame, text="Edit file", command=edit_file)
editFile.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

closeApp = tk.Button(frame, text="Close", command=exit)
closeApp.bind('<Escape>', exit())
closeApp.grid(row=600, column=0, sticky="ew", padx=5, pady=5)

frame.grid(row=0, column=0, sticky="ns")
canvas.grid(row=0, column=1, sticky="nsew")

for file in files:
    tag = tk.Label(canvas, text=file)
    tag.pack()

root.mainloop()
