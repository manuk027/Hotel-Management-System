"""
Project Name: Hotel Management System

Authors: MANU KRISHNA

Date: 01-02-2022"""


import csv,os

#function to add a new room to the hotel
def addroom():
    f=open('rooms.csv', 'a')
    cw=csv.writer(f)
    
    while True:
        rno=input('Enter Room number:')
        print()
        rfloor=input('Enter Room floor:')
        print()
        rbed=input('Enter number of beds:')
        print()
        rbathroom=input('Enter number of bathrooms:')
        print()
        rcode=input('Enter room code:')
        room_issued='YES'
        L=[rno,rfloor,rbed,rbathroom,rcode,room_issued]
        print()
        cw.writerow(L) 
        ch=input('Enter another (Yes/No) : ')
        if ch=='No':
            break
    f.flush()
    os.fsync(f.fileno())
    os.close(f.fileno())
#    f.close()
    

    
#function to edit the details of an existing room
def editroom():
    f1=open('rooms.csv', 'r', newline='\r\n')
    f2=open('temp.csv', 'w')
    cr=csv.reader(f1)
    cw=csv.writer(f2)
    s=input('Enter the room number to be updated:')
    counter = False
    for i in cr:
#        print(i[0])
        if i[0]==s:
            counter=True
            i[1]=input('Enter new room Floor:')
            i[2]=input('Enter new number of beds:')
            i[3]=input('Enter new number of bathrooms:')
            i[4]=input('Enter new roomcode:')
            cw.writerow(i)
            ch=input('Enter annother(Yes/No):')
            if ch=='No':
            	break
        else:
            cw.writerow(i)
    f2.flush()
    os.fsync(f2.fileno())
    os.close(f1.fileno())
    os.close(f2.fileno())
#    f1.close()
#    f2.close()
    
    if counter == False:
        print('Room not found')
        os.remove('temp.csv')
    else:
        os.remove('rooms.csv')
        os.rename('temp.csv', 'rooms.csv')
        print('Room updating....')
        print('Room updated!')
        
#function to delete the details of a room
def deleteroom():
    f1=open('rooms.csv', 'r', newline='\r\n')
    f2=open('temp.csv', 'w')
    cr=csv.reader(f1)
    cw=csv.writer(f2)
    s=input('Enter the room number to be deleted:')
    counter = False
    for i in cr:
    	if i and i[0]==s:
    		counter=True
    	elif i:
    		cw.writerow(i)
    f2.flush()
    os.fsync(f2.fileno())
    os.close(f1.fileno())
    os.close(f2.fileno())
#    f1.close()
#    f2.close()
    if counter ==False:
        print('room', s, 'not found')
        os.remove('temp.csv')
    else:
        os.remove('rooms.csv')
        os.rename('temp.csv', 'rooms.csv')
        print('room deleting...')
        print('room deleted!')

    
#function to view the details of all the rooms
def viewrooms():
    f1=open('rooms.csv', 'r',newline='\r\n')
    cr=csv.reader(f1)
    print('''List of rooms are/
Room no, floor no, no of beds, no of bathroom, Room issued (Yes/No)''')
    for i in cr:
        print(i,)
    f1.close()
  
#function to add a new customer to the hotel
def addcustomer():
    
    f=open('customers.csv', 'a')
    cw=csv.writer(f)
    
    while True:
        #accept the details of the new room from the user
        custno=input('Enter the customer number:')
        name=input('Enter the name:')
        address=input('Enter the address:')
        phoneno=input('Enter the phone number:')
        joining_date=input('Enter the date when customer join (dd/mm/yyyy): ')
        customertype=input('Enter the customer type (student/adult): ')
        roomfee=input('Enter the room fees: ')
        
        L=[custno,name,address,phoneno,joining_date,customertype,roomfee]
    
        cw.writerow(L) 
        ch=input('Enter another (Yes/No) : ')
        if ch=='No':
            break
        
    f.flush()
    os.fsync(f.fileno())
    os.close(f.fileno())
    
    return
    
#function to update the customer details of existing customer
def updatecustomer():
    f1=open('customers.csv', 'r', newline='\r\n')
    f2=open('temp.csv', 'w')
    cr=csv.reader(f1)
    cw=csv.writer(f2)
    m=input('Enter the customer number to be updated:')
    counter = False
    for i in cr:
#        print(i[0])
        if i[0]==m:
            counter=True
            i[1]=input('Enter new name:')
            i[2]=input('Enter new address:')
            i[3]=input('Enter new phone number:')
            i[4]=input('Enter new date when customer join (dd/mm/yyyy):')
            i[5]=input('Enter new customer type (student/adult):')
            i[6]=input('Enter new room fees: ')
            cw.writerow(i)
        else:
            cw.writerow(i)
    f2.flush()
    os.fsync(f2.fileno())
    os.close(f1.fileno())
    os.close(f2.fileno())
    
    if counter == False:
        print('Customer not found')
        os.remove('temp.csv')
    else:
        os.remove('customers.csv')
        os.rename('temp.csv', 'customers.csv')
        print('Customer updating...')
        print('Customer updated!')
    
#function to remove the customer details
def removecustomer():
    f1=open('customers.csv', 'r', newline='\r\n')
    f2=open('temp.csv', 'w')
    cr=csv.reader(f1)
    cw=csv.writer(f2)
    c=input('Enter the customer number to be removed:')
    counter = False
    for i in cr:
    	if i and i[0]==c:
    		counter=True
    	elif i:
    		cw.writerow(i)
    f2.flush()
    os.fsync(f2.fileno())
    os.close(f1.fileno())
    os.close(f2.fileno())
#    f1.close()
#    f2.close()
    if counter ==False:
        print('customer', c, 'not found')
        os.remove('temp.csv')
    else:
        os.remove('customers.csv')
        os.rename('temp.csv', 'customers.csv')
        print('customer removing.....')
        print('customer removed!')

    return

#function to view the details of all the customers   
def viewcustomers():
    f1=open('customers.csv', 'r',newline='\r\n')
    cr=csv.reader(f1)
    print('List of Customers are:')
    for i in cr:
        print(i)
    f1.close()
    
    return

#function to issue a room to a customer    
def issueroom():
    custno=input('Enter customer number:')   
    f1=open('members.csv', 'r',newline='\r\n')
    cr=csv.reader(f1)
    found=False
    for i in cr:
        if i[0]==custno:
            found=True
            break
    f1.close()
    
    if found==False:
        print('Customer not found')
        return
    
    rno=input('Enter room number to be issued:')
    f2=open('rooms.csv','r',newline='\r\n')
    cr=csv.reader(f2)
    found=False
    for i in cr:
        if i[0]==rno:
            found=True
            if int(i[3]) == int(i[4]):
                print('All room issued.Cannot issue room.')
                return
    f2.close()
    if found == False:
        print('Room Number not found')
        return
    
    idt=input('Enter date of issue(dd/mm/yyyy):')
    
    #add a record in the room_issue.csv file
    L=[rno,custno,idt]
    f=open('room_issue.csv','a')
    cw=csv.writer(f)
    cw.writerow(L)
    f.flush()
    os.fsync(f.fileno())
    os.close(f.fileno())
    
    #increase the number of copies issued in rooms.csv file
    f3=open('rooms.csv','r',newline='\r\n')
    f4=open('temp.csv', 'w')
    cr=csv.reader(f3)
    cw=csv.writer(f4)
    for i in cr:
        if i[0]==rno:
            i[4]= str(int(i[4]) + 1)
        cw.writerow(i)
    
    f4.flush()
    os.fsync(f4.fileno())
    os.close(f3.fileno())
    os.close(f4.fileno())
    
    os.remove('rooms.csv')
    os.rename('temp.csv','rooms.csv')
    
    print('Room issued!')
    return

#function to return a room back to the hotel
def leaveroom():
    custno=input('Enter customer number:')
    rno=input('Enter room number:')
    idt=input('Enter issue date(dd/mm/yyyy):')
    f1=open('room_issue.csv','r',newline='\r\n')
    f2=open('temp.csv','w')
    found=False
    
    cr=csv.reader(f1)
    cw=csv.writer(f2)
    
    for i in cr:
        if i[0]==custno and i[1]==rno and i[2]==idt:
            found=True
        cw.writerow(i)
    
    if found==False:
        print('Please check customer number/room number/issue date')
        f2.flush()
        os.fsync(f2.fileno())
        os.close(f1.fileno())
        os.close(f2.fileno())
        os.remove('temp.csv')
        return
    else:
        f2.flush()
        os.fsync(f2.fileno())
        os.close(f1.fileno())
        os.close(f2.fileno())
        os.remove('room_issue.csv')
        os.rename('temp.csv', 'room_issue.csv')
        
        #decrease the number of rooms issued in hotel.csv file
        f3=open('rooms.csv','r',newline='\r\n')
        f4=open('temp.csv', 'w')
        cr=csv.reader(f3)
        cw=csv.writer(f4)
        for i in cr:
            if i[0]==rno:
                i[4]= str(int(i[4]) - 1)
            cw.writerow(i)
        
        f4.flush()
        os.fsync(f4.fileno())
        os.close(f3.fileno())
        os.close(f4.fileno())
        
        os.remove('rooms.csv')
        os.rename('temp.csv','rooms.csv')
        print('Left room!')
        
    return
    

#start of main program

#Display the main menu
while True:
    print('\nWELCOME TO HOTEL MANAGEMENT SYSTEM')
    print("••••••••••••••••••••••••••••••••••")
    print()
    print()
    print()
    
   
    print(" ——————————————————————————————————————")
    print("|  ——————————————————————————————————  |")
    print('| |              MENU                | |')
    print("|  ——————————————————————————————————  |")
    print(" ——————————————————————————————————————")
    print()
    print()
    print(" ——————————————————————————————————————")
    print('| 01. | Add a Room                     |')
    print(" ——————————————————————————————————————")
    print()
    print(" ——————————————————————————————————————")
    print('| 02. | Edit Room Details              |')
    print(" ——————————————————————————————————————")
    print()
    print(" ——————————————————————————————————————")
    print('| 03. | Delete the details of the room |')
    print(" ——————————————————————————————————————")
    print()
    print(" ——————————————————————————————————————")
    print('| 04. | View the list of Rooms         |')
    print(" ——————————————————————————————————————")
    print()
    print(" ——————————————————————————————————————")
    print('| 05. | Add a new customer             |')
    print(" ——————————————————————————————————————")
    print()
    print(" ——————————————————————————————————————")
    print('| 06. | Update customer Details        |')
    print(" ——————————————————————————————————————")
    print()
    print(" ——————————————————————————————————————")
    print('| 07. | Remove customer                |')
    print(" ——————————————————————————————————————")
    print()
    print(" ——————————————————————————————————————")
    print('| 08. | View all Customer Details      |')
    print(" ——————————————————————————————————————")
    print()
    print(" ——————————————————————————————————————")
    print('| 09. | Issue a room                   |')
    print(" ——————————————————————————————————————")
    print()
    print(" ——————————————————————————————————————")
    print('| 10. | Leave a room                   |')
    print(" ——————————————————————————————————————")
    print()
    print(" ——————————————————————————————————————")
    print('| 11. | Exit                           |')
    print(" ——————————————————————————————————————")
    print()
    print()
    
    print(" ————————————————————————")
    ch=int(input('| Enter a choice (1-11): | '))
    print()
    
    
    #depending on choice selected call the function
    if ch==1:
        addroom()
    elif ch==2:
        editroom()
    elif ch==3:
        deleteroom()
    elif ch==4:
        viewrooms()
    elif ch==5:
        addcustomer()
    elif ch==6:
        updatecustomer()
    elif ch==7:
        removecustomer()
    elif ch==8:
        viewcustomers()
    elif ch==9:
        issueroom()
    elif ch==10:
        leaveroom()
    elif ch==11:
        print('Bye')
        break
