from tkinter import mainloop, ttk, messagebox
import tkinter 
from PIL import ImageTk, Image
from mysql import connector as sql 
import sv_ttk as sv
import os 

#make the mysql connection here

connect = sql.connect(host = 'localhost', user = 'root', password = '', database = "Hotel")
cursor = connect.cursor()

#define stuff

def regUI():
    def regFunc():
        gID = id.get()
        gName = name.get()
        roomType = rType.get()
        cIN = cid.get()
        cOUT = cod.get()
        room = roomNo.get()
        book= bookMode.get()
        pay = netPay.get()

        data = []
        data.append(gID)
        data.append(gName)
        data.append(roomType)
        data.append(cIN)
        data.append(cOUT)
        data.append(room)
        data.append(book)
        data.append(pay)        
        cust=(data)
        sq="INSERT INTO Guest(GuestID,GuestName,RoomType,CheckinDate,CheckoutDate,RoomNo,BookingSource,NetPayment)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        
        cursor.execute(sq,cust)
        connect.commit()
        messagebox.showinfo('Yay!', 'Guest Addition Successful')
        root.destroy()


    root2 = tkinter.Toplevel(root)
    root2.title("User Registration")
    root2.resizable(False, False)
    root2.geometry("300x500")

    ttk.Label(root2, text = "Enter User Details", font = ('Segoe UI', 20)).place(x = 15, y = 10)

    ttk.Label(root2, text = 'GuestID', font = ('Segoe UI', 12)).place(x = 20, y = 78)
    ttk.Label(root2, text = 'Guest Name', font = ('Segoe UI', 12)).place(x = 20, y =123)
    ttk.Label(root2, text = 'Room Type', font = ('Segoe UI', 12)).place(x = 20, y =168)
    ttk.Label(root2, text = 'Check-in Date', font = ('Segoe UI', 12)).place(x = 20, y =213)
    ttk.Label(root2, text = 'Check-out Date', font = ('Segoe UI', 12)).place(x = 20, y =258)
    ttk.Label(root2, text = 'Room Number', font = ('Segoe UI', 12)).place(x = 20, y =303)
    ttk.Label(root2, text = 'Booking Source', font = ('Segoe UI', 12)).place(x = 20, y =348)
    ttk.Label(root2, text = 'Net Payment', font = ('Segoe UI', 12)).place(x = 20, y =393)

    id = ttk.Entry(root2)
    id.place(x = 133, y = 75)
    name = ttk.Entry(root2)
    name.place(x = 133, y = 120)
    rType = ttk.Entry(root2)
    rType.place(x = 133, y = 165)
    cid = ttk.Entry(root2)
    cid.place(x = 133, y = 210)
    cod = ttk.Entry(root2)
    cod.place(x = 133, y = 255)
    roomNo = ttk.Entry(root2)
    roomNo.place(x = 133, y = 300)
    bookMode = ttk.Entry(root2)
    bookMode.place(x = 133, y = 345)
    netPay = ttk.Entry(root2)
    netPay.place(x = 133, y = 390)

    ttk.Button(root2, text = 'Add Guest', style = 'Accent.TButton', command = regFunc).place(x = 110, y = 445)

def adminReg():
    root.withdraw()
    os.startfile('Admin Register.pyw')

def adminLogin():
    root.withdraw()
    os.startfile('Hotely.pyw')

#UI

root = tkinter.Tk()
root.title("Welcome!")
root.resizable(False, False)
root.geometry("500x400")

img = ImageTk.PhotoImage(Image.open("logo.png"))
lab = ttk.Label(root, image = img)
lab.place(x= 63, y= 5)

photo = ImageTk.PhotoImage(Image.open('smol logo.png'))     
root.iconphoto(True, photo)

uReg = ttk.Button(root, text = 'User Registration', style = 'Accent.TButton', command  = regUI).place(x = 130, y = 210, width = 230, height = 42)
adReg = ttk.Button(root, text = 'Administrator Registration', command = adminReg).place(x = 130, y = 270, width = 230, height = 42)
adLogin = ttk.Button(root, text = 'Administrator Login', command = adminLogin).place(x = 130, y = 330, width = 230, height = 42)


sv.use_dark_theme()
mainloop()