from tkinter import Label, mainloop, messagebox, ttk
import tkinter 
from PIL import ImageTk, Image
import sv_ttk as sv
from mysql import connector as sql 
import importlib 

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
            
    root2 = tkinter.Toplevel(root)
    root2.title("Guest Records")
    root2.resizable(False, False)
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

def graphs():
    print("Not done yet")

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
        query = "UPDATE guest SET RoomNo  = %s WHERE GuestName = %s"
        val = (data)
        cursor.execute(query,val)
        connect.commit()
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
    root1.withdraw()
    importlib.import_module("open beta.py")
#to login or not to login 

def funcLogin():     #checks your usernames and passwords
    global root1
    uname = user.get()
    pw = pwd.get()

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
        ttk.Label(root1, text = "Welcome,", font = ('Segoe UI', 35)).place(x = 25, y = 10)
        ttk.Label(root1, text =  uname, font = ('Segoe UI',35, 'bold')).place(x = 240, y = 10)

        ttk.Label(root1, text = 'Guest Data', font = ('Segoe UI', 15)).place(x = 35, y = 80)

        gRecord = ttk.Button(root1, text = "Show Guest Records", command = gRecords)
        gRecord.place(x = 35, y = 120, width = 230, height =  42)

        graph = ttk.Button(root1, text = 'Booking Mode Graph', command = graphs)
        graph.place(x = 35, y = 175, width = 230, height = 42)

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
        messagebox.showinfo("Oh no :(","Your username or password is incorrect, try again xD", icon = 'error')
        return False
    

#main UI code

root = tkinter.Tk()
root.title("Login")
root.geometry("500x400")
root.resizable(False, False)
photo = ImageTk.PhotoImage(Image.open('smol logo.png'))     
root.iconphoto(True, photo)

style = ttk.Style()
style.configure("Accent.TButton")
global user; global pwd

img = ImageTk.PhotoImage(Image.open("logo.png"))
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