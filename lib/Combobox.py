import tkinter as tk
from tkinter import ttk

class Combobox(ttk.Combobox):
    def __init__(self, master,**kwargs):
        super().__init__(master,**kwargs)
        self.master = master
        self.set(self["values"][0])
    
    def on_change(self,callback):
        self.bind('<<ComboboxSelected>>', lambda e: callback(self.get()))