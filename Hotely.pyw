from tkinter import Label, mainloop, messagebox, ttk
import tkinter 
from PIL import ImageTk, Image
import sv_ttk as sv
from mysql import connector as sql 
import os

#make the mysql connection here

connect = sql.connect(host = 'localhost', user = 'root', password = '', database = "Hotel")
cursor = connect.cursor()

#some define statements for the UI

def gRecords():
    def show():
        cursor.execute("SELECT * FROM Guest")
        records = cursor.fetchall()
        
        for i, (GuestID, GuestName, RoomType, CheckinDate, CheckoutDate, RoomNo, BookingSource, NetPayment) in enumerate(records, start=1):
            tree.insert("", "end", values=(GuestID, GuestName, RoomType, CheckinDate, CheckoutDate, RoomNo, BookingSource, NetPayment))
            
    root2 = tkinter.Toplevel(root)      #things
    root2.title("Guest Records")        #required for 
    root2.resizable(False, False)       #the frame
    label = ttk.Label(root2, text="Guest Records", font=("Segoe UI",15)).grid(row=0, columnspan=1)
    cols = ('Guest ID', 'Guest Name', 'Room Type','Check-in Date', 'Check-out Date', 'Room Number', 'Booking Source', 'Net Payment')
    tree = ttk.Treeview(root2, columns=cols, show='headings')
    tree.column("#1", width = 100)
    tree.column("#2", width = 100)    #changes the width of every. single. column.
    tree.column("#3", width = 100)
    tree.column("#4", width = 100)
    tree.column("#5", width = 100)
    tree.column("#6", width = 100)
    tree.column("#7", width = 100)
    tree.column("#8", width = 100)
    for col in cols:
        tree.heading(col, text=col)    
        tree.grid(row=1, column=0, columnspan=1)
    show()
    sv.use_dark_theme()
    root2.mainloop()

def guestDelete():
    def delCommand():
        def delRecord():
            delete = delEntry.get()
            qu = "DELETE FROM Guest WHERE GuestName = %s"
            cursor.execute(qu, [(delete)])
            connect.commit()
            root3.destroy()
            messagebox.showinfo("Delete", 'Delete successful')
            root2.destroy()
        def close():
            root2.destroy()

        root3 = tkinter.Toplevel(root2)
        root3.title("Confirmation")
        root3.geometry("300x170")
        root3.resizable(False, False)

        ttk.Label(root3, text = 'Are you sure that you', font = ('SegoeUI', 19)).place(x = 27, y = 10)
        ttk.Label(root3, text = 'want to delete this guest?', font = ('SegoeUI', 19)).place(x = 7, y = 47)

        y = ttk.Button(root3, text = "Yes", command = delRecord).place(x = 55, y = 100, width = 70, height = 40)
        n = ttk.Button(root3, text = 'No', style = 'Accent.TButton', command = close).place(x = 155, y = 100, width = 70, height = 40)
 
    root2 = tkinter.Toplevel(root)
    root2.title("Delete Guest")
    root2.resizable(False, False)
    root2.geometry("300x200")

    ttk.Label(root2, text = "Delete Guest Record", font = ('Segoe UI', 20)).place(x= 15,y = 10)
    ttk.Label(root2, text = "Guest Name", font = ('Segoe UI', 12)).place(x = 25, y = 78)

    delEntry = ttk.Entry(root2)
    delEntry.place(x = 125, y = 75)

    updButton = ttk.Button(root2, text = 'Delete', command = delCommand)
    updButton.place(x = 115, y = 138)

    sv.use_dark_theme()


def checkOnline():
    def show():
        cursor.execute("SELECT * FROM Guest WHERE BookingSource = 'Online'")    #executes SQL query
        records = cursor.fetchall()
        
        for i, (GuestID, GuestName, RoomType, CheckinDate, CheckoutDate, RoomNo, BookingSource, NetPayment) in enumerate(records, start=1):  #adds values
            tree.insert("", "end", values=(GuestID, GuestName, RoomType, CheckinDate, CheckoutDate, RoomNo, BookingSource, NetPayment))   #to TreeView
            
    root2 = tkinter.Toplevel(root)               #things required 
    root2.title("Check-in/Checkout Details")     #for the 
    root2.resizable(False, False)                #frame
    label = ttk.Label(root2, text="Online Check-in/Check-out", font=("Segoe UI",15)).grid(row=0, columnspan=1)
    cols = ('Guest ID', 'Guest Name', 'Room Type','Check-in Date', 'Check-out Date', 'Room Number', 'Booking Source', 'Net Payment')
    tree = ttk.Treeview(root2, columns=cols, show='headings')
    tree.column("#1", width = 100)
    tree.column("#2", width = 100)    
    tree.column("#3", width = 100)
    tree.column("#4", width = 100)
    tree.column("#5", width = 100)
    tree.column("#6", width = 100)
    tree.column("#7", width = 100)
    tree.column("#8", width = 100)
    for col in cols:
        tree.heading(col, text=col)    
        tree.grid(row=1, column=0, columnspan=1)       #slap that treeview into a grid
    show()
    sv.use_dark_theme()
    root2.mainloop()

def checkOffline():
    def show():
        cursor.execute("SELECT * FROM Guest WHERE BookingSource = 'Offline'")
        records = cursor.fetchall()
        
        for i, (GuestID, GuestName, RoomType, CheckinDate, CheckoutDate, RoomNo, BookingSource, NetPayment) in enumerate(records, start=1):
            tree.insert("", "end", values=(GuestID, GuestName, RoomType, CheckinDate, CheckoutDate, RoomNo, BookingSource, NetPayment))
            
    root2 = tkinter.Toplevel(root)
    root2.title("Check-in/Checkout Details")
    root2.resizable(False, False)
    label = ttk.Label(root2, text="Offline Check-in/Check-out", font=("Segoe UI",15)).grid(row=0, columnspan=1)
    cols = ('Guest ID', 'Guest Name', 'Room Type','Check-in Date', 'Check-out Date', 'Room Number', 'Booking Source', 'Net Payment')
    tree = ttk.Treeview(root2, columns=cols, show='headings')
    tree.column("#1", width = 100)
    tree.column("#2", width = 100)    
    tree.column("#3", width = 100)
    tree.column("#4", width = 100)
    tree.column("#5", width = 100)
    tree.column("#6", width = 100)
    tree.column("#7", width = 100)
    tree.column("#8", width = 100)
    for col in cols:
        tree.heading(col, text=col)    
        tree.grid(row=1, column=0, columnspan=1)
    show()
    sv.use_dark_theme()
    root2.mainloop()

def netPayment():
    def show():
        cursor.execute("SELECT GuestName, NetPayment FROM Guest")
        records = cursor.fetchall()
        
        for i, (GuestName,NetPayment) in enumerate(records, start=1):
            tree.insert("", "end", values=(GuestName,NetPayment))
            
    root2 = tkinter.Toplevel(root)
    root2.title("Payment")
    root2.resizable(False, False)
    label = ttk.Label(root2, text="Payment Details", font=("Segoe UI",15)).grid(row=0, columnspan=1)
    cols = ('Guest Name','Net Payment')
    tree = ttk.Treeview(root2, columns=cols, show='headings')
    tree.column("#1", width = 100)
    tree.column("#2", width = 100)    
    for col in cols:
        tree.heading(col, text=col)    
        tree.grid(row=1, column=0, columnspan=1)
    show()
    sv.use_dark_theme()
    root2.mainloop()

def roomNo():
    root2 = tkinter.Toplevel(root)     #UI for updating data
    root2.title("Update")
    root2.resizable(False, False)
    root2.geometry("300x220")    

    def update(): 
        lab = updEntry.get()          
        name = nameEntry.get()
        data=[]
        data.append(lab)
        data.append(name)
        query = "UPDATE guest SET RoomNo  = %s WHERE GuestName = %s"
        val = (data)
        cursor.execute(query,val)           #executes query
        connect.commit()                    #commits to database
        messagebox.showinfo('Yay', 'Update Successful')
        root2.destroy()
         
    ttk.Label(root2, text = "Update Room Number", font = ('Segoe UI', 20)).place(x= 15,y = 10)
    ttk.Label(root2, text = "Room Number", font = ('Segoe UI', 12)).place(x = 15, y = 120)
    ttk.Label(root2, text = 'Guest Name', font = ('Segoe UI', 12)).place(x = 15, y = 75)

    updEntry = ttk.Entry(root2)
    updEntry.place(x = 125, y = 120)
    nameEntry = ttk.Entry(root2)
    nameEntry.place(x = 125, y = 75)

    updButton = ttk.Button(root2, text = 'Update', style = 'Accent.TButton', command = update)
    updButton.place(x = 115, y = 175)

    sv.use_dark_theme()

def updCheckout():
    root2 = tkinter.Toplevel(root)
    root2.title("Update")
    root2.resizable(False, False)
    root2.geometry("300x220")    

    def update(): 
        lab = updEntry.get()
        name = nameEntry.get()
        data=[]
        data.append(lab)
        data.append(name)
        query = "UPDATE guest SET CheckoutDate  = %s WHERE GuestName = %s"
        val = (data)
        cursor.execute(query,val)
        connect.commit()
        messagebox.showinfo('Yay', 'Update Successful')
        root2.destroy()
         
    ttk.Label(root2, text = "Update Check-out Date", font = ('Segoe UI', 20)).place(x= 15,y = 10)
    ttk.Label(root2, text = "Check-out Date", font = ('Segoe UI', 12)).place(x = 15, y = 120)
    ttk.Label(root2, text = 'Guest Name', font = ('Segoe UI', 12)).place(x = 15, y = 75)

    updEntry = ttk.Entry(root2)
    updEntry.place(x = 125, y = 120)
    nameEntry = ttk.Entry(root2)
    nameEntry.place(x = 125, y = 75)

    updButton = ttk.Button(root2, text = 'Update', style = 'Accent.TButton', command = update)
    updButton.place(x = 115, y = 175)

    sv.use_dark_theme()

def cmdLine():
    def adminLogin():           #Administrator login function
        uname1 = user1.get()
        pw1 = pwd1.get()

        quer = 'SELECT * FROM Admin WHERE Username = %s AND Password = %s'
        cursor.execute(quer, [(uname1), (pw1)])
        result = cursor.fetchall()
        if result:
            root1.withdraw()
            root2.withdraw()
            os.startfile("command line.py")
        else:
            messagebox.showerror('Error', 'Username/Password is incorrect')

    root2 = tkinter.Toplevel()             #UI for Administrator login
    root2.title("Update")
    root2.resizable(False, False)
    root2.geometry("300x220")

    ttk.Label(root2, text = "Administrator Login", font = ('Segoe UI', 20)).place(x= 10,y = 10)
    ttk.Label(root2, text = "Username", font = ('Segoe UI', 12)).place(x = 15, y = 75)
    ttk.Label(root2, text = 'Password', font = ('Segoe UI', 12)).place(x = 15, y = 120)

    user1 = ttk.Entry(root2)
    user1.place(x = 125, y = 75)
    pwd1 = ttk.Entry(root2, show = "●")
    pwd1.place(x = 125, y = 120)

    admin = ttk.Button(root2, text = 'Login', style = 'Accent.TButton', command = adminLogin)
    admin.place(x = 115, y = 175)

    sv.use_dark_theme()

#to login or not to login 

def funcLogin():     #checks your usernames and passwords
    global root1
    uname = user.get()       #fetches username
    pw = pwd.get()           #fetches password

    quer = 'SELECT * FROM Login WHERE Username = %s AND Password = %s'
    cursor.execute(quer, [(uname), (pw)])
    result = cursor.fetchall()

    if result:  
        root.withdraw()
        root1 = tkinter.Toplevel(root)      #creates another window with same Tcl interpreter
        root1.title("Hotely")
        root1.geometry("800x450")
        root1.resizable(False,False)              

        #spaghetti code begins
        ttk.Label(root1, text = "Welcome,", font = ('Segoe UI', 35)).place(x = 25, y = 10)     #Opening 
        ttk.Label(root1, text =  uname, font = ('Segoe UI',35, 'bold')).place(x = 240, y = 10) #text

        ttk.Label(root1, text = 'Guest Data', font = ('Segoe UI', 15)).place(x = 35, y = 80)

        gRecord = ttk.Button(root1, text = "Show Guest Records", command = gRecords)
        gRecord.place(x = 35, y = 120, width = 230, height =  42)

        gDelete = ttk.Button(root1, text = 'Delete Guest Record', command = guestDelete)
        gDelete.place(x = 35, y = 175, width = 230, height = 42)

        ttk.Label(root1, text = 'Check-in/Check-out', font = ('Segoe UI', 15)).place(x = 35, y = 240)

        online = ttk.Button(root1, text = 'Online Check-in/Check-out', command = checkOnline)
        online.place(x = 35, y = 280, width = 230, height = 42)

        offline = ttk.Button(root1, text = 'Offline Check-in/Check-out', command = checkOffline)
        offline.place(x = 35, y = 335, width = 230, height = 42)

        ttk.Label(root1, text = "Payments", font = ("Segoe UI", 15)).place(x = 450, y = 80)

        payment = ttk.Button(root1, text = 'Payment Details', command = netPayment)
        payment.place(x = 450, y = 120, width = 230, height = 42)

        ttk.Label(root1, text = 'Updates', font = ('Segoe UI', 15)).place(x = 450, y = 240)

        roomNO = ttk.Button(root1, text = 'Update Room Number', command = roomNo)
        dateCheckout = ttk.Button(root1, text = 'Update Check-out Date', command = updCheckout)
        roomNO.place(x = 450, y = 280, width = 230, height = 42)
        dateCheckout.place(x = 450, y = 335, width = 230, height = 42)

        cmdline = ttk.Button(root1, text = 'Use command-line tools', style = 'Accent.TButton', command = cmdLine)
        cmdline.place(x = 565, y = 400, width = 230, height = 42)

        ttk.Separator(root1, orient = "horizontal").place(x = 360, y = 100, height = 300, width = 3)

        sv.use_dark_theme()
        mainloop()
        return True

    elif uname == '':         #no username
        messagebox.showerror('Oh no :(',"Please enter a username")
    elif pw == '':            #no password
        messagebox.showerror('Oh no :(',"Please enter a password")
    else:                      #wrong username/password
        messagebox.showerror("Oh no :(","Your username or password is incorrect, try again")
        return False
    

#main UI code

root = tkinter.Tk()
root.title("Login")
root.geometry("500x400")
root.resizable(False, False)
photo = ImageTk.PhotoImage(Image.open('Assets\smol logo.png'))     
root.iconphoto(True, photo)

style = ttk.Style()
style.configure("Accent.TButton")
global user; global pwd

img = ImageTk.PhotoImage(Image.open("Assets\logo.png"))
lab = ttk.Label(root, image = img)
lab.place(x= 63, y= 10)

u= ttk.Label(root, text = 'Username')
u.place(x =142, y= 225)
p = ttk.Label(root, text = 'Password')
p.place(x= 142, y= 275)

user = ttk.Entry(root)
user.place(x= 217, y= 220)

pwd = ttk.Entry(root, show = "●")
pwd.place(x= 217, y= 270)

login = ttk.Button(root, text = 'Login', style = 'Accent.TButton', command = funcLogin)
login.place(x = 225, y = 320)

sv.use_dark_theme()
root.mainloop()