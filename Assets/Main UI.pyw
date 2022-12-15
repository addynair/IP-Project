def main():
    #import stuff here

    from tkinter import Label, mainloop, messagebox, ttk
    import tkinter
    from PIL import ImageTk, Image
    import sv_ttk as sv
    from mysql import connector as sql
    import os
    import sys
    import win32mica
    from win32mica import MICAMODE
    import ctypes

    #make the mysql connection here

    connect = sql.connect(host='localhost',
                        user='root',
                        password='',
                        database="Hotel")
    cursor = connect.cursor()

    #some define statements for the UI


    def gRecords():

        def show():
            cursor.execute("SELECT * FROM Guest")
            records = cursor.fetchall()

            for i, (GuestID, GuestName, RoomType, CheckinDate, CheckoutDate,
                    RoomNo, BookingSource, NetPayment) in enumerate(records,
                                                                    start=1):
                tree.insert("",
                            "end",
                            values=(GuestID, GuestName, RoomType, CheckinDate,
                                    CheckoutDate, RoomNo, BookingSource,
                                    NetPayment))

        root2 = tkinter.Toplevel(root)  #things
        root2.title("Guest Records")  #required for
        root2.resizable(False, False)  #the frame
        root2.focus_set()
        label = ttk.Label(root2,
                        text="Guest Records",
                        font=("Segoe UI Variable Display",
                                15)).grid(row=0, columnspan=1)

        cols = ('Guest ID', 'Guest Name', 'Room Type', 'Checkin Date',
                'Checkout Date', 'Room Number', 'Booking Source', 'Net Payment')

        tree = ttk.Treeview(root2, columns=cols, show='headings')
        tree.column("#1", width=100)
        tree.column("#2", width=100)  #changes the width of every. single. column.
        tree.column("#3", width=100)
        tree.column("#4", width=100)
        tree.column("#5", width=100)
        tree.column("#6", width=100)
        tree.column("#7", width=100)
        tree.column("#8", width=100)
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
            root3.focus_set()

            ttk.Label(root3,
                    text='Are you sure that you',
                    font=('SegoeUI', 19),
                    background="#000000").place(x=27, y=10)
            ttk.Label(root3,
                    text='want to delete this guest?',
                    font=('SegoeUI', 19),
                    background="#000000").place(x=7, y=47)

            y = ttk.Button(root3, text="Yes", command=delRecord).place(x=55,
                                                                    y=100,
                                                                    width=70,
                                                                    height=40)
            n = ttk.Button(root3, text='No', style='Accent.TButton',
                        command=close).place(x=155, y=100, width=70, height=40)

            root3.configure(bg='#000000')
            root3.wm_attributes("-transparent", "#000000")
            root3.update()
            HWND = root3.frame()
            win32mica.ApplyMica(HWND, ColorMode=MICAMODE.DARK)

        root2 = tkinter.Toplevel(root)
        root2.title("Delete Guest")
        root2.resizable(False, False)
        root2.geometry("300x200")
        root2.focus_set()

        ttk.Label(root2,
                text="Delete Guest Record",
                font=('Segoe UI Variable Display', 20),
                background="#000000").place(x=15, y=10)
        ttk.Label(root2,
                text="Guest Name",
                font=('Segoe UI Variable Display', 12),
                background="#000000").place(x=25, y=78)

        delEntry = ttk.Entry(root2)
        delEntry.place(x=125, y=75, width= 145)

        updButton = ttk.Button(root2, text='Delete', command=delCommand)
        updButton.place(x=115, y=138)

        root2.configure(bg='#000000')
        root2.wm_attributes("-transparent", "#000000")
        root2.update()
        HWND = root2.frame()
        win32mica.ApplyMica(HWND, ColorMode=MICAMODE.DARK)

        sv.use_dark_theme()


    def checkOnline():

        def show():
            cursor.execute("SELECT * FROM Guest WHERE BookingSource = 'Online'"
                        )  #executes SQL query
            records = cursor.fetchall()

            for i, (GuestID, GuestName, RoomType, CheckinDate, CheckoutDate,
                    RoomNo, BookingSource,
                    NetPayment) in enumerate(records, start=1):  #adds values
                tree.insert("",
                            "end",
                            values=(GuestID, GuestName, RoomType, CheckinDate,
                                    CheckoutDate, RoomNo, BookingSource,
                                    NetPayment))  #to TreeView

        root2 = tkinter.Toplevel(root)  #things required
        root2.title("Checkin/Checkout Details")  #for the
        root2.resizable(False, False)  #frame
        root2.focus_set()
        label = ttk.Label(root2,
                        text="Online Checkin/Checkout",
                        font=("Segoe UI Variable Display",
                                15)).grid(row=0, columnspan=1)
        cols = ('Guest ID', 'Guest Name', 'Room Type', 'Checkin Date',
                'Checkout Date', 'Room Number', 'Booking Source', 'Net Payment')

        tree = ttk.Treeview(root2, columns=cols, show='headings')
        tree.column("#1", width=100)
        tree.column("#2", width=100)
        tree.column("#3", width=100)
        tree.column("#4", width=100)
        tree.column("#5", width=100)
        tree.column("#6", width=100)
        tree.column("#7", width=100)
        tree.column("#8", width=100)
        for col in cols:
            tree.heading(col, text=col)
            tree.grid(row=1, column=0,
                    columnspan=1)  #slap that treeview into a grid
        show()
        root2.mainloop()


    def checkOffline():

        def show():
            cursor.execute("SELECT * FROM Guest WHERE BookingSource = 'Offline'")
            records = cursor.fetchall()

            for i, (GuestID, GuestName, RoomType, CheckinDate, CheckoutDate,
                    RoomNo, BookingSource, NetPayment) in enumerate(records,
                                                                    start=1):
                tree.insert("",
                            "end",
                            values=(GuestID, GuestName, RoomType, CheckinDate,
                                    CheckoutDate, RoomNo, BookingSource,
                                    NetPayment))

        root2 = tkinter.Toplevel(root)
        root2.title("Checkin/Checkout Details")
        root2.resizable(False, False)
        root2.focus_set()
        label = ttk.Label(root2,
                        text="Offline Checkin/Checkout",
                        font=("Segoe UI Variable Display",
                                15)).grid(row=0, columnspan=1)

        cols = ('Guest ID', 'Guest Name', 'Room Type', 'Checkin Date',
                'Checkout Date', 'Room Number', 'Booking Source', 'Net Payment')

        tree = ttk.Treeview(root2, columns=cols, show='headings')
        tree.column("#1", width=100)
        tree.column("#2", width=100)
        tree.column("#3", width=100)
        tree.column("#4", width=100)
        tree.column("#5", width=100)
        tree.column("#6", width=100)
        tree.column("#7", width=100)
        tree.column("#8", width=100)
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

            for i, (GuestName, NetPayment) in enumerate(records, start=1):
                tree.insert("", "end", values=(GuestName, NetPayment))

        root2 = tkinter.Toplevel(root)
        root2.title("Payment")
        root2.resizable(False, False)
        root2.focus_set()
        label = ttk.Label(root2,
                        text="Payment Details",
                        font=("Segoe UI Variable Display",
                                15)).grid(row=0, columnspan=1)
        cols = ('Guest Name', 'Net Payment')
        tree = ttk.Treeview(root2, columns=cols, show='headings')
        tree.column("#1", width=100)
        tree.column("#2", width=100)
        for col in cols:
            tree.heading(col, text=col)
            tree.grid(row=1, column=0, columnspan=1)
        show()
        sv.use_dark_theme()
        root2.mainloop()


    def roomNo():
        root2 = tkinter.Toplevel(root)  #UI for updating data
        root2.title("Update")
        root2.resizable(False, False)
        root2.geometry("300x220")
        root2.focus_set()

        def update():
            lab = updEntry.get()
            name = nameEntry.get()
            data = []
            data.append(lab)
            data.append(name)
            query = "UPDATE guest SET RoomNo  = %s WHERE GuestName = %s"
            val = (data)
            cursor.execute(query, val)  #executes query
            connect.commit()  #commits to database
            messagebox.showinfo('Yay', 'Update Successful')
            root2.destroy()

        ttk.Label(root2,
                text="Update Room Number",
                font=('Segoe UI Variable Display', 20),
                background="#000000").place(x=15, y=10)
        ttk.Label(root2,
                text="Room Number",
                font=('Segoe UI Variable Display', 12),
                background="#000000").place(x=15, y=120)
        ttk.Label(root2,
                text='Guest Name',
                font=('Segoe UI Variable Display', 12),
                background="#000000").place(x=15, y=75)

        updEntry = ttk.Entry(root2)
        updEntry.place(x=125, y=120, width= 145)
        nameEntry = ttk.Entry(root2)
        nameEntry.place(x=125, y=75, width= 145)

        updButton = ttk.Button(root2,
                            text='Update',
                            style='Accent.TButton',
                            command=update)
        updButton.place(x=115, y=175)

        root2.configure(bg='#000000')
        root2.wm_attributes("-transparent", "#000000")
        root2.update()
        HWND = root2.frame()
        win32mica.ApplyMica(HWND, ColorMode=MICAMODE.DARK)

        sv.use_dark_theme()


    def updCheckout():
        root2 = tkinter.Toplevel(root)
        root2.title("Update")
        root2.resizable(False, False)
        root2.geometry("300x260")
        root2.focus_set()

        def update():
            lab = updEntry.get()
            name = nameEntry.get()
            pay = payEntry.get()
            data = []
            data.append(lab)
            data.append(pay)
            data.append(name)
            query = "UPDATE guest SET CheckoutDate  = %s, NetPayment = %s WHERE GuestName = %s"
            val = (data)
            cursor.execute(query, val)
            connect.commit()
            messagebox.showinfo('Yay', 'Update Successful')
            root2.destroy()

        ttk.Label(root2,
                text="Update Checkout Date",
                font=('Segoe UI Variable Display', 20),
                background="#000000").place(x=15, y=10)
        ttk.Label(root2,
                text="Checkout Date",
                font=('Segoe UI Variable Display', 12),
                background="#000000").place(x=15, y=120)
        ttk.Label(root2,
                text='Guest Name',
                font=('Segoe UI Variable Display', 12),
                background="#000000").place(x=15, y=75)
        ttk.Label(root2,
                text='New Payment',
                font=('Segoe UI Variable Display', 12),
                background="#000000").place(x=15, y=165)

        updEntry = ttk.Entry(root2)
        updEntry.place(x=125, y=120, width= 145)
        nameEntry = ttk.Entry(root2)
        nameEntry.place(x=125, y=75)
        payEntry = ttk.Entry(root2)
        payEntry.place(x=125, y=165, width= 145)

        updButton = ttk.Button(root2,
                            text='Update',
                            style='Accent.TButton',
                            command=update)
        updButton.place(x=115, y=220)

        root2.configure(bg='#000000')
        root2.wm_attributes("-transparent", "#000000")
        root2.update()
        HWND = root2.frame()
        win32mica.ApplyMica(HWND, ColorMode=MICAMODE.DARK)

        sv.use_dark_theme()


    def cmdLine():

        def adminLogin():  #Administrator login function
            uname1 = user1.get()
            pw1 = pwd1.get()

            quer = 'SELECT * FROM Admin WHERE Username = %s AND Password = %s'
            cursor.execute(quer, [(uname1), (pw1)])
            result = cursor.fetchall()
            if result:
                root1.withdraw()
                root2.withdraw()
                if sys.platform == "win32":
                    os.startfile('Assets\command line.py')
                else:
                    opener = "open" if sys.platform == "darwin" else "xdg-open"
                    subprocess.call([opener, 'Assets\command line.py'])
                #os.startfile("Assets\command line.py")
            else:
                messagebox.showerror('Error', 'Username/Password is incorrect')

        root2 = tkinter.Toplevel()  #UI for Administrator login
        root2.title("Update")
        root2.resizable(False, False)
        root2.geometry("300x220")
        root2.focus_set()

        ttk.Label(root2,
                text="Administrator Login",
                font=('Segoe UI Variable Display', 20),
                background="#000000").place(x=10, y=10)
        ttk.Label(root2,
                text="Username",
                font=('Segoe UI Variable Display', 12),
                background="#000000").place(x=15, y=75)
        ttk.Label(root2,
                text='Password',
                font=('Segoe UI Variable Display', 12),
                background="#000000").place(x=15, y=120)

        root2.configure(bg='#000000')
        root2.wm_attributes("-transparent", "#000000")
        root2.update()
        HWND = root2.frame()
        win32mica.ApplyMica(HWND, ColorMode=MICAMODE.DARK)

        user1 = ttk.Entry(root2)
        user1.place(x=125, y=75, width= 145)
        pwd1 = ttk.Entry(root2, show="●")
        pwd1.place(x=125, y=120, width= 145)

        admin = ttk.Button(root2,
                        text='Login',
                        style='Accent.TButton',
                        command=adminLogin)
        admin.place(x=115, y=175)

        sv.use_dark_theme()


    #to login or not to login


    def funcLogin():  #checks your usernames and passwords
        global root1
        uname = user.get()  #fetches username
        pw = pwd.get()  #fetches password

        quer = 'SELECT * FROM Login WHERE Username = %s AND Password = %s'
        cursor.execute(quer, [(uname), (pw)])
        result = cursor.fetchall()

        if result:
            root.withdraw()
            root1 = tkinter.Toplevel(
                root)  #creates another window with same Tcl interpreter
            root1.title("Hotely")
            root1.geometry("800x450")
            root1.resizable(False, False)
            root1.focus_force()

            #spaghetti code begins
            ttk.Label(root1,
                    text="Welcome,",
                    font=('Segoe UI Variable Display', 35),
                    background="#000000").place(x=25, y=10)  #Opening
            ttk.Label(
                root1,  #Text
                text=uname,
                font=('Segoe UI Variable Display', 35, 'bold'),
                background="#000000").place(x=240, y=10)

            ttk.Label(root1,
                    text='Guest Data',
                    font=('Segoe UI Variable Display', 15),
                    background="#000000").place(x=35, y=80)

            gRecord = ttk.Button(root1,
                                text="Show Guest Records",
                                command=gRecords)
            gRecord.place(x=35, y=120, width=230, height=42)

            gDelete = ttk.Button(root1,
                                text='Delete Guest Record',
                                command=guestDelete)
            gDelete.place(x=35, y=175, width=230, height=42)

            ttk.Label(root1,
                    text='Checkin/Checkout',
                    font=('Segoe UI Variable Display', 15),
                    background="#000000").place(x=35, y=240)

            online = ttk.Button(root1,
                                text='Online Checkin/Checkout',
                                command=checkOnline)
            online.place(x=35, y=280, width=230, height=42)

            offline = ttk.Button(root1,
                                text='Offline Checkin/Checkout',
                                command=checkOffline)
            offline.place(x=35, y=335, width=230, height=42)

            ttk.Label(root1,
                    text="Payments",
                    font=("Segoe UI Variable Display", 15),
                    background="#000000").place(x=450, y=80)

            payment = ttk.Button(root1, text='Payment Details', command=netPayment)
            payment.place(x=450, y=120, width=230, height=42)

            ttk.Label(root1,
                    text='Update Data',
                    font=('Segoe UI Variable Display', 15),
                    background="#000000").place(x=450, y=240)

            roomNO = ttk.Button(root1, text='Update Room Number', command=roomNo)
            dateCheckout = ttk.Button(root1,
                                    text='Update Checkout Date',
                                    command=updCheckout)
            roomNO.place(x=450, y=280, width=230, height=42)
            dateCheckout.place(x=450, y=335, width=230, height=42)

            cmdline = ttk.Button(root1,
                                text='Use command-line tools',
                                style='Accent.TButton',
                                command=cmdLine)
            cmdline.place(x=565, y=400, width=230, height=42)

            ttk.Separator(root1, orient="horizontal").place(x=360,
                                                            y=100,
                                                            height=300,
                                                            width=3)

            sv.use_dark_theme()

            root1.configure(bg='#000000')
            root1.wm_attributes("-transparent", "#000000")
            root1.update()
            HWND = ctypes.windll.user32.GetParent(root1.winfo_id())
            win32mica.ApplyMica(HWND, ColorMode=MICAMODE.DARK)
            #sv.use_dark_theme()

            mainloop()
            return True

        elif uname == '':  #no username
            messagebox.showerror('Oh no :(', "Please enter a username")
        elif pw == '':  #no password
            messagebox.showerror('Oh no :(', "Please enter a password")
        else:  #wrong username/password
            messagebox.showerror(
                "Oh no :(", "Your username or password is incorrect, try again")
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
    global user
    global pwd

    img = ImageTk.PhotoImage(Image.open("Assets\logo.png"))
    lab = ttk.Label(root, image=img, background="#000000")
    lab.place(x=63, y=10)

    u = ttk.Label(root,
                text='Username',
                font=('Segoe UI Variable Display', 10),
                background="#000000")
    u.place(x=142, y=225)
    p = ttk.Label(root,
                text='Password',
                font=('Segoe UI Variable Display', 10),
                background="#000000")
    p.place(x=142, y=275)

    user = ttk.Entry(root)
    user.place(x=217, y=220, width= 135)

    pwd = ttk.Entry(root, show="●")
    pwd.place(x=217, y=270, width= 135)

    login = ttk.Button(root,
                    text='Login',
                    style='Accent.TButton',
                    command=funcLogin)
    login.place(x=225, y=320)

    root.configure(bg='#000000')
    root.wm_attributes("-transparent", "#000000")
    root.update()
    HWND = root.frame()
    win32mica.ApplyMica(HWND, ColorMode=MICAMODE.DARK)

    sv.use_dark_theme()
    root.mainloop()

if __name__== "__main__":
    main()