from tkinter import messagebox, ttk 
from PIL import ImageTk, Image
import tkinter 
import sv_ttk as sv
from mysql import connector as sql 
import importlib 

#make the mysql connection here

connect = sql.connect(host = 'localhost', user = 'root', password = '', database = "Hotel")
cursor = connect.cursor()

#to login or not to login 

def funcLogin():
    uname = user.get()
    pw = pwd.get()

    quer = 'SELECT * FROM Login WHERE Username = %s AND Password = %s'
    cursor.execute(quer, [(uname), (pw)])
    result = cursor.fetchall()

    if result:
        messagebox.showinfo("Yay!","Yay you logged in. Wow, such empty!")
        root.destroy()
        importlib.import_module('alpha build')
        return True
    elif uname == '':
        messagebox.showerror('Oh no :(',"Please enter a username")
    elif pw == '':
        messagebox.showerror('Oh no :(',"Please enter a password")
    else:
        messagebox.showinfo("Oh no :(","Your username or password is incorrect, try again xD", icon = 'error')
        return False
    

#main UI code

root = tkinter.Tk()
root.title("Login")
root.geometry("500x400")

style = ttk.Style()
style.configure("Accent.TButton")
global user; global pwd

img = ImageTk.PhotoImage(Image.open("E:\\Login stuff\logo.png"))
lab = ttk.Label(root, image = img)
lab.place(x= 63, y= 10)

u= ttk.Label(root, text = 'Username')
u.place(x =142, y= 220)
p = ttk.Label(root, text = 'Password')
p.place(x= 142, y= 270)

user = ttk.Entry(root)
user.place(x= 217, y= 220)

pwd = ttk.Entry(root, show = "●")
pwd.place(x= 217, y= 270)

login = ttk.Button(root, text = 'Login', style = 'Accent.TButton', command = funcLogin)
login.place(x = 225, y = 320)

sv.use_dark_theme()
root.mainloop()
