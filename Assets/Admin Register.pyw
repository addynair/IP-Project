def main():
    #import stuff here

    from tkinter import messagebox, ttk
    from PIL import ImageTk, Image
    import tkinter
    import sv_ttk as sv
    from mysql import connector as sql

    #make the mysql connection here

    connect = sql.connect(host='localhost',
                        user='root',
                        password='',
                        database="Hotel")
    cursor = connect.cursor()

    #to register or not to register


    def funcRegister():
        uname = user.get()
        pw = pwd.get()
        quer = "INSERT INTO Login VALUES(%s, %s)"
        cursor.execute(quer, [(uname), (pw)])
        connect.commit()
        messagebox.showinfo(
            "Yay", 'Yay, you have registered! Use the Login Page now to login')
        root.destroy()


    #main UI Code

    root = tkinter.Tk()
    root.title("Registration")
    root.geometry("500x400")
    root.resizable(False, False)
    photo = ImageTk.PhotoImage(Image.open("Assets\Register.png"))
    root.iconphoto(False, photo)

    global user
    global pwd

    img = ImageTk.PhotoImage(Image.open("Assets\logo.png"))
    lab = ttk.Label(root, image=img)
    lab.place(x=63, y=10)

    u = ttk.Label(root, text='Username', font=('Segoe UI Variable Display', 10))
    u.place(x=142, y=225)
    p = ttk.Label(root, text='Password', font=('Segoe UI Variable Display', 10))
    p.place(x=142, y=275)

    user = ttk.Entry(root)
    user.place(x=217, y=220, width= 135)

    pwd = ttk.Entry(root, show="●")
    pwd.place(x=217, y=270, width= 135)

    reg = ttk.Button(root,
                    text='Register',
                    style='Accent.TButton',
                    command=funcRegister)
    reg.place(x=225, y=320)

    sv.use_dark_theme()
    root.mainloop()

if __name__ == "__main__":
    main()