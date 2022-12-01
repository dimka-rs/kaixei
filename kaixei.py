#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk

width=800
height=480
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

style = ttk.Style(root)
style.configure('TNotebook', tabposition='ws')
style.configure('TNotebook.Tab', padding=[nbpadw,nbpadh])
style.configure("TButton", padding=20) # background="#c00"
style.configure("TFrame", padding=60)

# create a notebook
notebook = ttk.Notebook(root, style='TNotebook')
notebook.pack(expand=True) ## add pady=10 ?

# create frames
f1 = ttk.Frame(notebook, width=width-nbpadw, height=height-statush, padding=10)
f2 = ttk.Frame(notebook, width=width-nbpadw, height=height-statush, padding=10)

f1.pack(fill='both', expand=True)
f2.pack(fill='both', expand=True)

# add frames to notebook
notebook.add(f1, text='Frame1')
notebook.add(f2, text='Frame2')

# add buttons to frames
b1a = ttk.Button(f1, text="Button 1 A", command=btn_cb)
b1a.pack(expand=True)
b1b = ttk.Button(f1, text="Button 1 B", command=btn_cb)
b1b.pack(expand=True)
b1c = ttk.Button(f1, text="Button 1 C", command=btn_cb)
b1c.pack(expand=True)

# FIXME: adding these shrinks frame to buttons area. Why?
'''
b2a = ttk.Button(f2, text="Button 2 A", command=btn_cb)
b2a.pack(expand=True)
b2b = ttk.Button(f2, text="Button 2 B", command=btn_cb)
b2b.pack(expand=True)
b2c = ttk.Button(f2, text="Button 2 C", command=btn_cb)
b2c.pack(expand=True)
'''

# add status bar
status = tk.Label(root, text="kaixei status")
status.pack(fill='x', expand=True, side='bottom')

root.mainloop()
