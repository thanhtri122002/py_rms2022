from tkinter import *
import tkinter.ttk as ttk


class Admin:
    def __init__(self):
        self.__dishes = []

    def add_dish(self, name, price):
        new_dish = (name, price)
        self.__dishes.append(new_dish)

        for d in self.__dishes:
            print(d)

    def edit_dish(self, edited_name, edited_price, or_name):
        if edited_name == or_name:
            return
        else:
            for d in self.__dishes:
                if d[0] == or_name:
                    self.delete_dish(or_name)
                    new_dish = (edited_name, edited_price)
                    self.__dishes.append(new_dish)
                    break

        for d in self.__dishes:
            print(d)

    def delete_dish(self, name):
        for d in self.__dishes:
            if d[0] == name:
                self.__dishes.remove(d)
                break

        for d in self.__dishes:
            print(d)


win = Tk()
win.title("Admin")
win.resizable(False, False)

# Dishes listbox
lbx = Listbox(win, width=40)
#lbx.grid(columnspan=3, column=0, row=0)

# Treeview(table)
columns = ('name', 'price')
table = ttk.Treeview(win, columns=columns, show='headings')
table.heading('name', text="Name")
table.heading('price', text="Price")

table.grid(columnspan=3, column=0, row=0)

# Scrollbar
scrollbar = Scrollbar(win)
#scrollbar.grid(column=)

added_stuff = ""
dishes_amount = 0

# Create new admin instance
new_admin = Admin()


def submit_addition(dish: Entry, price: Entry, p: Toplevel):
    data = [dish.get(), price.get()]
    table.insert('', END, values=data)

    new_admin.add_dish(dish.get(), price.get())

    p.destroy()


def submit_edition(dish: Entry, price: Entry, p: Toplevel):
    selected_item = table.selection()[0]  # Get selected item

    cur_item = table.focus()
    or_name = table.item(cur_item)['values'][0]
    edited_data = [dish.get(), price.get()]
    edited_name = dish.get()
    edited_price = price.get()

    new_admin.edit_dish(edited_name, edited_price, or_name)

    table.item(selected_item, text="blub", values=edited_data)
    p.destroy()


def add():
    pop = Toplevel(win)
    pop.resizable(False, False)
    pop.title("Adding new dish")

    # Add dish name
    add_text = Label(pop, text='Add dish:')
    add_text.grid(column=0, row=0, padx=10, pady=10, sticky=W)

    stuff_entry = Entry(pop)
    stuff_entry.grid(column=1, row=0, padx=10)

    # Add dish price
    add_price_text = Label(pop, text='Price:')
    add_price_text.grid(column=0, row=1, padx=10, pady=10, sticky=W)

    price_entry = Entry(pop)
    price_entry.grid(column=1, row=1, padx=10)

    # Submit addition
    submit_add = Button(pop, text='Enter', command=lambda: submit_addition(stuff_entry, price_entry, pop))
    submit_add.grid(columnspan=2, column=0, row=2, padx=10, pady=10)


def edit():
    if len(table.selection()) == 0:
        err = Toplevel(win)
        err.title("ERROR")
        message = Label(err, text="You did not select the dish to edit!", font=("Arial", 50))
        message.pack()
        return

    pop = Toplevel(win)
    pop.resizable(False, False)
    pop.title("Adding new dish")

    # Add dish name
    edit_text = Label(pop, text='Edit dish:')
    edit_text.grid(column=0, row=0, padx=10, pady=10, sticky=W)

    edit_entry = Entry(pop)
    edit_entry.grid(column=1, row=0, padx=10)

    # Add dish price
    edit_price_text = Label(pop, text='Edit price:')
    edit_price_text.grid(column=0, row=1, padx=10, pady=10, sticky=W)

    price_entry = Entry(pop)
    price_entry.grid(column=1, row=1, padx=10)

    # Submit addition
    submit_edit = Button(pop, text='Enter', command=lambda: submit_edition(edit_entry, price_entry, pop))
    submit_edit.grid(columnspan=2, column=0, row=2, padx=10, pady=10)


def delete():
    if len(table.selection()) == 0:
        err = Toplevel(win)
        err.title("ERROR")
        message = Label(err, text="You did not select the dish to delete!", font=("Arial", 50))
        message.pack()
        return

    cur_item = table.focus()
    name = table.item(cur_item)['values'][0]

    new_admin.delete_dish(name)

    selected_item = table.selection()[0]  # Get selected item
    table.delete(selected_item)


add_butt = Button(win, text="Add", padx=70, command=add)
add_butt.grid(column=0, row=1, padx=50, pady=20)

edit_butt = Button(win, text="Edit", padx=70, command=edit)
edit_butt.grid(column=1, row=1, padx=50, pady=20)

del_butt = Button(win, text="Delete", padx=70, command=delete)
del_butt.grid(column=2, row=1, padx=50, pady=20)

win.mainloop()