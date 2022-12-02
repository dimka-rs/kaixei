#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk

# buttons on page
class Page:
    buttons = list()

# chapter with pages
class Chapter:
    pages = list()

# book with chapters
class Book:
    chapters = list()

width=1024
height=600
rootwindowx=10
rootwindowy=10
nbpadw=10
nbpadh=20
statush=20
#frames = {1:"f1", 2:"f2"}

def btn_cb():
    return


# root window
root = tk.Tk()
root.geometry(f'{width}x{height}+{rootwindowx}+{rootwindowy}')
root.title('kaixei')
root.resizable(width=None, height=None)

style = ttk.Style(root)
style.configure('TNotebook', tabposition='ws')
style.configure('TNotebook.Tab', padding=[nbpadw,nbpadh])
style.configure("TButton", padding=20) # background="#c00"
style.configure("TFrame", padding=60)

# create a notebook
notebook = ttk.Notebook(root, style='TNotebook', width=width-nbpadw, height=height-statush)
notebook.pack(side='top', fill='both') ## pady=10, expand=True

# create frames
f1 = ttk.Frame(notebook, padding=10)
f2 = ttk.Frame(notebook, padding=10)

f1.pack(fill='both', expand=True)
f2.pack(fill='both', expand=True)

# add frames to notebook
notebook.add(f1, text='Frame1')
notebook.add(f2, text='Frame2')

# add buttons to frames
chapter1 = Chapter()
for pg in range(2):
    chapter1.pages.append(Page())

    for btn in range(16):
        chapter1.pages[pg].buttons.append(ttk.Button(f1 if pg==0 else f2, text=f'Button {str(pg)} {str(btn)}', command=btn_cb))
        chapter1.pages[pg].buttons[-1].grid(padx=10, pady=10, row=btn//4, column=btn%4)


# add status bar
status = tk.Label(root, text="kaixei status", bg='#101010')
#status.pack(fill='x', expand=True, side='bottom')
status.pack(side='bottom', fill='x')

root.mainloop()
