# -----------------------------------------------------------
# demonstrates the frontend and backend scripts of book inventory GUI app on Windows
# using local database books and tkinter library to generate windows dialog boxes
#
# This is the front end part if this application, which includes different labels and buttons
# email dhruvdave61@gmail.com
# ----------------------------------------------------------

from tkinter import *
from backend import Database

# retrieving the local database books
database = Database("books.db")


class Window(object):

    def __init__(self, window):

        # generating the new window
        self.window = window

        # providing title to the new window
        self.window.wm_title("BookStore")

        # Providing different labels for the book information
        l1 = Label(window, text="Title")
        l1.grid(row=0, column=0)

        l2 = Label(window, text="Author")
        l2.grid(row=0, column=2)

        l3 = Label(window, text="Year")
        l3.grid(row=1, column=0)

        l4 = Label(window, text="ISBN")
        l4.grid(row=1, column=2)

        # different text boxes to fill data in and editing the data
        self.title_text = StringVar()
        self.e1 = Entry(window, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)

        self.author_text = StringVar()
        self.e2 = Entry(window, textvariable=self.author_text)
        self.e2.grid(row=0, column=3)

        self.year_text = StringVar()
        self.e3 = Entry(window, textvariable=self.year_text)
        self.e3.grid(row=1, column=1)

        self.isbn_text = StringVar()
        self.e4 = Entry(window, textvariable=self.isbn_text)
        self.e4.grid(row=1, column=3)

        # list box to provide the list of books
        self.list1 = Listbox(window, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        # scroll bar to scroll through multiple books
        sb1 = Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)

        # creating a listbox
        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        # bind method used to know which list item is selected
        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        # different buttons to perform several operations in the book inventory
        b1 = Button(window, text="View all", width=12, command=self.view_command)
        b1.grid(row=2, column=3)

        b2 = Button(window, text="Search entry", width=12, command=self.search_command)
        b2.grid(row=3, column=3)

        b3 = Button(window, text="Add entry", width=12, command=self.add_command)
        b3.grid(row=4, column=3)

        b4 = Button(window, text="Update selected", width=12, command=self.update_command)
        b4.grid(row=5, column=3)

        b5 = Button(window, text="Delete selected", width=12, command=self.delete_command)
        b5.grid(row=6, column=3)

        b6 = Button(window, text="Close", width=12, command=window.destroy)
        b6.grid(row=7, column=3)

    # this method is used to get which book is selected by the user from the list
    def get_selected_row(self, event):
        index = self.list1.curselection()[0]
        self.selected_tuple = self.list1.get(index)
        self.e1.delete(0, END)
        self.e1.insert(END, self.selected_tuple[1])
        self.e2.delete(0, END)
        self.e2.insert(END, self.selected_tuple[2])
        self.e3.delete(0, END)
        self.e3.insert(END, self.selected_tuple[3])
        self.e4.delete(0, END)
        self.e4.insert(END, self.selected_tuple[4])

    # this method executes when the view button pressed
    def view_command(self):
        self.list1.delete(0, END)
        for row in database.view():
            self.list1.insert(END, row)\

    # this method executes when the search button pressed, which searches the book into the database
    def search_command(self):
        self.list1.delete(0, END)
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(),
                                   self.isbn_text.get()):
            self.list1.insert(END, row)

    # this method executes when the insert button pressed, which inserts the new book into the database
    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END,
                          (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))

    # this method executes when the delete button pressed, which deletes the record from the database
    def delete_command(self):
        database.delete(self.selected_tuple[0])

    # this method executes when the update button pressed, which updates the record in the database
    def update_command(self):
        database.update(self.selected_tuple[0], self.title_text.get(), self.author_text.get(), self.year_text.get(),
                        self.isbn_text.get())


window = Tk()
Window(window)
window.mainloop()
