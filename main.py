import tkinter as tk
from tkinter import ttk
import sqlite3


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('pizza.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS pizza (id integer primary key, name text, price integer)''')
        self.conn.commit()

    def insert_data(self, name, price):
        self.cursor.execute('''INSERT INTO pizza(name, price) VALUES ( ?, ?)''',
                            (name, price))
        self.conn.commit()


class Main(tk.Frame):
    def __init__(self, root, db):
        super().__init__(root)
        self.init_myapp()
        self.db = db

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
        self.view()

    def buy(self):
        ChoosePizza(self.db)


    def view(self):
        db.cursor.execute('''SELECT * FROM pizza''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.cursor.fetchall()]


class ChoosePizza(tk.Toplevel):
    def __init__(self, db):
        super().__init__(root)
        self.init_subapp()
        self.db = db

    def init_subapp(self):
        self.title("Choose Pizza")
        self.geometry("600x400+326+235")

        self.margarita = tk.Button(self, text='Buy margarita', command=self.buy_pizza('margarita', 300), bg='#d7d8e0', bd=0,
                                   height=1, width=30)
        self.europa = tk.Button(self, text='Buy europa', command=self.buy_pizza('europa', 450), bg='#d7d8e0', bd=0,
                                height=1, width=30)
        self.mexico = tk.Button(self, text='Buy mexico', command=self.buy_pizza('mexico', 320), bg='#d7d8e0', bd=0,
                                height=1, width=30)
        self.palermo = tk.Button(self, text='Buy palermo', command=self.buy_pizza('palermo', 280), bg='#d7d8e0', bd=0,
                                 height=1, width=30)
        self.pepperoni = tk.Button(self, text='Buy pepperoni', command=self.buy_pizza('pepperoni', 350), bg='#d7d8e0', bd=0,
                                   height=1, width=30)

        self.pepperoni.pack()
        self.margarita.pack()
        self.europa.pack()
        self.mexico.pack()
        self.palermo.pack()

    def buy_pizza(self, text, price):
        db.insert_data(text, price)



if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root, db)
    app.pack()
    root.title("Pizza App")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
