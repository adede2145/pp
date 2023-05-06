from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from PIL import Image, ImageTk

def Get(event):
    e1.delete(0, END)
    e2.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['Time'])
    e2.insert(0, select['Activities'])

def Delete():
    id = e1.get()
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='1e_rante')
    mycursor = mydb.cursor()
    try:
        sql = "delete from devices where id = %s"
        val = (id,)
        mycursor.execute(sql, val)
        mydb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("INFO", "Data deleted successfully")
        e1.delete(0, END)
        e2.delete(0, END)
    except Exception as e:
        print(e)
        mydb.rollback()
        mydb.close()

root = Tk()
root.geometry("910x580")
root.title("Recent activities")

# Load the background image
bg_image = Image.open("D:\giphy.gif")
bg_gif = ImageTk.PhotoImage(bg_image)

# Create a label widget for the background image and place it behind all other widgets
bg_label = Label(root, image=bg_gif)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.lower()

Button(root, text="delete", command=Delete, height=-5, width=10).place(x=660, y=300)

columns = ('Time', 'Activities')
listBox = ttk.Treeview(root, columns=columns, show='headings')
for column in columns:
    listBox.heading(column, text=column)
listBox.grid(row=1, column=0, columnspan=2)
listBox.place(x=500, y=50)

listBox.bind('<Double-Button-1>', Get)

e1 = Entry(root, width=30)
e1.place(x=100, y=100)

e2 = Entry(root, width=30)
e2.place(x=100, y=150)

root.mainloop()
