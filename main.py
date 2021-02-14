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

        self.pizza_img = tk.PhotoImage(file='pizza.png')

        btn = tk.Button(frame, text='Buy', command=self.buy, bg='#d7d8e0', bd=0,
                        compound=tk.TOP, image=self.pizza_img)
        btn.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=('Id', 'Details', 'Price'), height=15, show='headings')
        self.tree.column('Id', width=50, anchor=tk.CENTER)
        self.tree.column('Details', width=380, anchor=tk.CENTER)
        self.tree.column('Price', width=130, anchor=tk.CENTER)

        self.tree.heading('Id', text='Id')
        self.tree.heading('Details', text='Details')
        self.tree.heading('Price', text='Price')

        self.tree.pack()


    def buy(self):
        ChoosePizza()


class ChoosePizza(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_subapp()

    def init_subapp(self):
        self.title("Choose Pizza")
        self.geometry("600x400+326+235")


if __name__ == "__main__":
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Pizza App")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
