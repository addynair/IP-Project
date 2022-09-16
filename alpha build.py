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

def ShowGuest(): 
    read = pd.read_sql('SELECT * FROM Guest', connect)
    print("\n", read, "\n")

def OnlineCheck():
    read = pd.read_sql("SELECT * FROM Guest WHERE BookingSource = 'Online'", connect)
    print("\n", read, "\n")

def OfflineCheck():
    read = pd.read_sql("SELECT * FROM Guest WHERE BookingSource = 'Offline'", connect)
    print("\n", read, "\n")

def Payments():
    read = pd.read_sql("SELECT GuestName, NetPayment FROM Guest", connect)
    print("\n", read, "\n")

def StaffDetails():
    read = pd.read_sql("SELECT * FROM Staff", connect)
    print("\n", read, "\n")

def StaffSalary():
    read = pd.read_sql("SELECT StaffID, Name, Salary FROM Staff", connect)
    print("\n", read, "\n")
   

def AddGuest():
    data=[]
    gid= input('Enter the new GuestID: ')
    data.append(gid)
    name= input('Enter the name of the Guest: ')
    data.append(name)
    rType=input('Enter the typr of room required (Single/Double): ' )
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
            ShowGuest()
        elif guestMenu == 2:
            AddGuest()    

    elif menu1 == 2:
        print("Select from one of these options (use numbers 1-2)")
        print("1. Online Check-in/Check-out")
        print("2. Reserved Check-in/Check-out")
        checkMenu = int(input("Enter the required selection: "))
        if checkMenu == 1:
            OnlineCheck()
        elif checkMenu == 2:
            OfflineCheck()

    elif menu1 == 3:
        Payments()

    elif menu1 == 4:
        print("Select from one of these options (use numbers 1-3)")
        print("1. Show all staff records")
        print("2. Add a staff record")
        print("3. Delete a staff record")
        staffMenu = int(input("Enter the requried selection: "))
        if staffMenu == 1:
            StaffDetails()
        elif staffMenu == 2:
            print("It's raining outputs!")       #it's raining placeholders!

    elif menu1 == 5: 
        StaffSalary()

    elif menu1 == 6:
        print("\n Select from one of these options (use numbers 1-) \n ")
        print("1. Update the Room type of a guest")
        print("2. Update the Check-out date of the guest")
        print('3. Update the Room number of the guest')
        upd1= int(input("Enter the required selection: "))
        if upd1 == 1:
            print("Yay output")        #you need to level up to access this part of the program xD
    else:
        print("Invalid option")
    
