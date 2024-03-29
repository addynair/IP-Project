def main():
    #import stuff here

    import pandas as pd
    from matplotlib import pyplot as plt
    from mysql import connector as sql
    import warnings as w
    import os
    import sys 

    #make the connection here

    w.filterwarnings('ignore')  #removes SQLAlchemy warning
    connect = sql.connect(host='localhost',
                        user='root',
                        password='',
                        database='Hotel')

    cursor = connect.cursor()

    #define stuff here


    def showGuest():
        read = pd.read_sql('SELECT * FROM Guest', connect)
        print("\n", read, "\n")


    def onlineCheck():
        read = pd.read_sql("SELECT * FROM Guest WHERE BookingSource = 'Online'",
                        connect)
        print("\n", read, "\n")


    def offlineCheck():
        read = pd.read_sql("SELECT * FROM Guest WHERE BookingSource = 'Offline'",
                        connect)
        print("\n", read, "\n")


    def payments():
        read = pd.read_sql("SELECT GuestName, NetPayment FROM Guest", connect)
        print("\n", read, "\n")


    def staffDetails():
        read = pd.read_sql("SELECT * FROM Staff", connect)
        print("\n", read, "\n")


    def staffSalary():
        read = pd.read_sql("SELECT StaffID, Name, Salary FROM Staff", connect)
        print("\n", read, "\n")


    def addGuest():
        data = []
        gid = input('Enter the new GuestID: ')
        data.append(gid)
        name = input('Enter the name of the guest to be added: ')
        data.append(name)
        rType = input('Enter the type of room required (Single/Double): ')
        data.append(rType)
        cid = input('Enter the Checkin date: ')
        data.append(cid)
        cod = input('Enter the Checkout date: ')
        data.append(cod)
        roomNo = int(input('Enter the assigned room number: '))
        data.append(roomNo)
        bookMode = input('Enter the mode of booking: ')
        data.append(bookMode)
        netAmount = int(input('Enter the net amount paid: '))
        data.append(netAmount)
        cust = (data)
        sq = "INSERT INTO Guest(GuestID,GuestName,RoomType,CheckinDate,CheckoutDate,RoomNo,BookingSource,NetPayment)VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"

        cursor.execute(sq, cust)
        connect.commit()
        read = pd.read_sql('SELECT * FROM Guest', connect)
        print(read)


    def deleteGuest():
        name = input("Enter the name of the guest to be deleted: ")
        sq = "DELETE FROM Guest WHERE GuestName = %s"
        cust = (name, )
        cursor.execute(sq, cust)
        connect.commit()
        read = pd.read_sql("SELECT * FROM Guest", connect)
        print(read)


    def graphProfit():
        months = ['May', 'June', 'July', 'August', 'September', 'October']
        profit = [20000, 90000, 70000, 90000, 80000, 120000]
        plt.style.use('dark_background')
        plt.plot(months, profit)
        plt.title("Profits from June to October 1")
        plt.xlabel("Months")
        plt.ylabel("Profit")
        plt.show()


    def graphSalary():
        cursor.execute("select name,salary from staff")
        result = cursor.fetchall
        Name = []
        Salary = []

        for i in cursor:
            Name.append(i[0])
            Salary.append(i[1])

        plt.style.use('dark_background')
        plt.bar(Name, Salary)
        plt.ylim(0, 80000)
        plt.xlabel("Names of staff members")
        plt.ylabel("Salary")
        plt.title("Salary graph")
        plt.style.use('dark_background')
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        plt.show()


    def addStaff():
        data = []
        sid = input('Enter the new StaffID: ')
        data.append(sid)
        name = input('Enter the name of the employee to be added: ')
        data.append(name)
        dob = input("Enter the date of birth of the employee: ")
        data.append(dob)
        desig = input("Enter the designation of the employee: ")
        data.append(desig)
        salary = int(input("Enter the salary of the employee: "))
        data.append(salary)
        doh = input("Enter the employee's date of hire: ")
        data.append(doh)
        val = (data)
        sq = "INSERT INTO Staff(StaffID, Name, DateOfBirth, Designation, Salary, DateOfHire)VALUES(%s,%s,%s,%s,%s,%s)"
        cursor.execute(sq, val)
        connect.commit()
        read = pd.read_sql('SELECT * FROM Staff', connect)
        print(read)


    def deleteStaff():
        name = input("Enter the name of the staff to be deleted: ")
        sq = "DELETE FROM staff WHERE Name = %s"
        cust = (name, )
        cursor.execute(sq, cust)
        connect.commit()
        read = pd.read_sql("SELECT * FROM staff", connect)
        print(read)


    def updateRtype():
        newdata = []
        rtype = input("Enter the new room type: ")
        newdata.append(rtype)
        name = input("Enter the name of the guest: ")
        newdata.append(name)
        sq = "UPDATE guest SET RoomType = %s WHERE GuestName = %s"
        val = (newdata)
        cursor.execute(sq, val)
        connect.commit()
        read = pd.read_sql("SELECT * FROM guest", connect)
        print(read)


    def updateCOD():
        newdata = []
        newcod = input("Enter the updated Checkout date: ")
        newdata.append(newcod)
        newpay = int(input("Enter the updated Payment amount: "))
        newdata.append(newpay)
        name = input("Enter the name of the guest: ")
        newdata.append(name)
        sq = "UPDATE guest SET CheckoutDate = %s, NetPayment = %s WHERE GuestName = %s"
        val = (newdata)
        cursor.execute(sq, val)
        connect.commit()
        read = pd.read_sql("SELECT * FROM guest", connect)
        print(read)


    def updateRoomno():
        newdata = []
        Roomno = input("Enter the new room no: ")
        newdata.append(Roomno)
        name = input("Enter the name of the guest: ")
        newdata.append(name)
        sq = "UPDATE guest SET RoomNo  = %s WHERE GuestName = %s"
        val = (newdata)
        cursor.execute(sq, val)
        connect.commit()
        read = pd.read_sql("SELECT * FROM guest", connect)
        print(read)


    def updateSalary():
        newdata = []
        salary = input("Enter the new salary: ")
        newdata.append(salary)
        name = input("Enter the name of the staff: ")
        newdata.append(name)
        sq = "UPDATE staff SET Salary  = %s WHERE  Name = %s"
        val = (newdata)
        cursor.execute(sq, val)
        connect.commit()
        read = pd.read_sql("SELECT * FROM staff", connect)
        print(read)


    #write main code stuff here

    while True:
        print("\nUse numbers 1-6 to select from any of these options. Press 0 to exit\n")
        print("1. Guest Data")
        print("2. Checkin/Checkout")
        print("3. Payment amounts")
        print("4. Staff Details ")
        print("5. Staff salary")
        print("6. Update Data")
        print("7. Credits")
        menu = int(input("Enter the required selection: "))

        if menu == 0:
            print("Bye")
            break

        elif menu == 1:
            print("\nSelect from one of these options (use numbers 1-4)\n")
            print("1. Show all guest records")
            print("2. Add a guest record")
            print("3. Delete a guest record")
            print("4. Graphical Representation")
            guestMenu = int(input("Enter the required selection: "))
            if guestMenu == 1:
                showGuest()
            elif guestMenu == 2:
                addGuest()
            elif guestMenu == 3:
                deleteGuest()
            elif guestMenu == 4:
                print("Select from one of these options (use numbers 1 to  2 )")
                print("1. Profit graph")
                print("2. Salary graph")
                graphMenu = int(input("Enter the required selection: "))
                if graphMenu == 1:
                    graphProfit()
                elif graphMenu == 2:
                    graphSalary()

        elif menu == 2:
            print("\nSelect from one of these options (use numbers 1-2)\n")
            print("1. Online Checkin/Checkout")
            print("2. Reserved Checkin/Checkout")
            checkMenu = int(input("Enter the required selection: "))
            if checkMenu == 1:
                onlineCheck()
            elif checkMenu == 2:
                offlineCheck()

        elif menu == 3:
            payments()

        elif menu == 4:
            print("\nSelect from one of these options (use numbers 1-3)\n")
            print("1. Show all staff records")
            print("2. Add a staff record")
            print("3. Delete a staff record")
            staffMenu = int(input("Enter the requried selection: "))
            if staffMenu == 1:
                staffDetails()
            elif staffMenu == 2:
                addStaff()
            elif staffMenu == 3:
                deleteStaff()

        elif menu == 5:
            staffSalary()

        elif menu == 6:
            print("\nSelect from one of these options (use numbers 1-4)\n")
            print("1. Update the Room type of a guest")
            print("2. Update the Checkout date of the guest")
            print('3. Update the Room number of the guest')
            print("4. Update the salary of the staff")
            upd = int(input("Enter the required selection: "))
            if upd == 1:
                updateRtype()
            elif upd == 2:
                updateCOD()
            elif upd == 3:
                updateRoomno()
            elif upd == 4:
                updateSalary()
            
        elif menu == 7:
            if sys.platform == "win32":
                os.startfile('Assets\Credits.mp4')
            else:
                opener = "open" if sys.platform == "darwin" else "xdg-open"
                subprocess.call([opener, 'Assets\Admin Register.pyw'])

        else:
            print("\nInvalid option\n")

if __name__ == "__main__":
    main()