import tkinter as tk
from tkinter import ttk
import sqlite3

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_myapp()



    def init_myapp(self):
        frame = tk.Frame(bg='#d7d8e0', bd=2)
        frame.pack(side=tk.TOP, fill=tk.X)




if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Pizza App")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()