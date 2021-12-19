from tkinter import *
import tkinter as tk
from tkinter import messagebox as mb
import time

page = tk.Tk()
page.geometry("750x750")
page.title("Wikipedia Voice Search")
tk.Label(page, text="Search with your voice",
         fg="Black", font="Gabriola 45 bold").pack()

page.mainloop()
