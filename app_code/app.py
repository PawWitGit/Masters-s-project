""" In this file, create a GUI to app"""

from email.mime import image
from enum import auto
from logging import root
from re import I
import tkinter as tk
from tkinter import mainloop, ttk
from tkinter.tix import COLUMN
from turtle import bgcolor, width
from typing import Container
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter.filedialog import askopenfile


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        #configure the frame
        self.geometry("600x600")
        self.title('Air Pollution')
        self.resizable(1, 1)

        #columns and rows setup    
    
        
        self.create_widgets()

    def create_widgets(self):
        # username
        username_label = ttk.Label(self, text="Username:",background="red")
        

        #image
        image1 = Image.open("air_poll.png")
        
        test = ImageTk.PhotoImage(image1)
        label1 = ttk.Label(image=test)
        label1.image = test
        label1.grid(row=1,column=0)
       

        
if __name__ == "__main__":
    root = MainWindow()
    root.mainloop()