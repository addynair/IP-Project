#import stuff here 

import pandas as pd 
from matplotlib import pyplot as plt 
from mysql import connector as sql 
import warnings as w 
from tkinter import ttk 
from tkinter import *
import sv_ttk as sv

#make the connection here 
w.filterwarnings('ignore')                                                      #removes SQLAlchemy warning 
connect = df= sql.connect(host='localhost',user='root',password='',database='Hotel')
print(df)

mycursor=connect.cursor()

#define stuff here 

def showGuest(): 
    read = pd.read_sql('SELECT * FROM Guest', connect)
    print("\n", read, "\n")

def onlineCheck():
    read = pd.read_sql("SELECT * FROM Guest WHERE BookingSource = 'Online'", connect)
    print("\n", read, "\n")

def offlineCheck():
    read = pd.read_sql("SELECT * FROM Guest WHERE BookingSource = 'Offline'", connect)
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
    data=[]
    gid= input('Enter the new GuestID: ')
    data.append(gid)
    name= input('Enter the name of the guest to be added: ')
    data.append(name)
    rType=input('Enter the type of room required (Single/Double): ' )
    data.append(rType)
    cid=input('Enter the check-in date: ')
    data.append(cid)
    cod = input('Enter the check-out date: ')
    data.append(cod)
    noDay= int(input('Enter the number of days stayed: '))
    data.append(noDay)
    roomNo= int(input('Enter the assigned room number: '))
    data.append(roomNo)
    bookMode = input('Enter the mode of booking: ')
    data.append(bookMode)
    netAmount=int(input('Enter the net amount paid: '))
    data.append(netAmount)
    cust=(data)
    sq="INSERT INTO Guest(GuestID,GuestName,RoomType,CheckinDate,CheckoutDate,NoDays,RoomNo,BookingSource,NetPayment)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sq,cust)
    connect.commit()
    read = pd.read_sql('SELECT * FROM Guest', connect)
    print(read)

def deleteGuest():
    name = input("Enter the name of the guest to be deleted: ")
    sq = "DELETE FROM Guest WHERE GuestName = %s"
    cust = (name,)
    mycursor.execute(sq,cust)
    connect.commit()
    read = pd.read_sql("SELECT * FROM Guest", connect)
    print(read)

def addStaff():
    data=[]
    sid= input('Enter the new StaffID: ')
    data.append(sid)
    name= input('Enter the name of the employee to be added: ')
    data.append(name)
    dob = input("Enter the date of birth of the employee: ")
    data.append(dob)
    desig = input("Enter the designation of the employee: ")
    data.append(desig)
    salary = int(input("Enter the salary of the employee: "))
    data.append(salary)
    doh = input("Enter the employee's date of hire: ")
    data.append(doh)
    val=(data)
    sq="INSERT INTO Staff(StaffID, Name, DateOfBirth, Designation, Salary, DateOfHire)VALUES(%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sq,val)
    connect.commit()
    read = pd.read_sql('SELECT * FROM Staff', connect)
    print(read)

    
def deleteStaff():
    name = input("Enter the name of the staff to be deleted: ")
    sq = "DELETE FROM staff WHERE Name = %s"
    cust = (name,)
    mycursor.execute(sq,cust)
    connect.commit()
    read = pd.read_sql("SELECT * FROM staff", connect)
    print(read)

def UpdateRtype():
    newdata=[]
    rtype = input("Enter the new room type: ")
    newdata.append(rtype)
    name = input("Enter the name of the guest: ")
    newdata.append(name)
    sq = "UPDATE guest SET RoomType = %s WHERE GuestName = %s"
    val = (newdata)
    mycursor.execute(sq,val)
    connect.commit()
    read = pd.read_sql("SELECT * FROM guest", connect)
    print(read)

def Updatecod():
    newdata=[]
    newcod = input("Enter the updated check-out date: ")
    newdata.append(newcod)
    name = input("Enter the name of the guest: ")
    newdata.append(name)
    sq = "UPDATE guest SET CheckoutDate = %s WHERE GuestName = %s"
    val = (newdata)
    mycursor.execute(sq,val)
    connect.commit()
    read = pd.read_sql("SELECT * FROM guest", connect)
    print(read)

def UpdateRoomno():
    newdata=[]
    Roomno = input("Enter the new room no: ")
    newdata.append(Roomno)
    name = input("Enter the name of the guest: ")
    newdata.append(name)
    sq = "UPDATE guest SET RoomNo  = %s WHERE GuestName = %s"
    val = (newdata)
    mycursor.execute(sq,val)
    connect.commit()
    read = pd.read_sql("SELECT * FROM guest", connect)
    print(read)

def UpdateSalary():
    newdata=[]
    salary = input("Enter the new salary: ")
    newdata.append(salary)
    name = input("Enter the name of the staff: ")
    newdata.append(name)
    sq = "UPDATE staff SET Salary  = %s WHERE  Name = %s"
    val = (newdata)
    mycursor.execute(sq,val)
    connect.commit()
    read = pd.read_sql("SELECT * FROM staff", connect)
    print(read)
        

#write the login UI code here 


#write main code stuff here

while True:
    print("Use numbers 1-6 to select from any of these options. Press 0 to exit")
    print("1. Guest Data")
    print("2. Check-in/Check-out")
    print("3. Payment amounts")
    print("4. Staff Details ")
    print("5. Staff salary")
    print("6. Updates")
    menu1 = int(input("Enter the required selection: "))

    if menu1 == 0: 
        print("Bye")
        break 

    elif menu1 == 1:
        print("Select from one of these options (use numbers 1-4)")
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
            print("Stonks graph")        #stonks

    elif menu1 == 2:
        print("Select from one of these options (use numbers 1-2)")
        print("1. Online Check-in/Check-out")
        print("2. Reserved Check-in/Check-out")
        checkMenu = int(input("Enter the required selection: "))
        if checkMenu == 1:
            onlineCheck()
        elif checkMenu == 2:
            offlineCheck()

    elif menu1 == 3:
        payments()

    elif menu1 == 4:
        print("Select from one of these options (use numbers 1-3)")
        print("1. Show all staff records")
        print("2. Add a staff record")
        print("3. Delete a staff record")
        staffMenu = int(input("Enter the requried selection: "))
        if staffMenu == 1:
            staffDetails()
        elif staffMenu == 2:
            addStaff()
        elif staffMenu == 3:
            deleteStaff()       #it is raining placeholders!


    elif menu1 == 5: 
        staffSalary()

    elif menu1 == 6:
        print("\n Select from one of these options (use numbers 1-) \n ")
        print("1. Update the Room type of a guest")
        print("2. Update the Check-out date of the guest")
        print('3. Update the Room number of the guest')
        print("4. Update the salary of the staff")
        upd1= int(input("Enter the required selection: "))
        if upd1 == 1:
            UpdateRtype()
        elif upd1 == 2:
            Updatecod()
        elif upd1 == 3:
            UpdateRoomno()
        elif upd1 == 4:
            UpdateSalary()
        else:
            print("Invalid option")
    
        
            
                    
    
    
