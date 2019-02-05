#importing modules that will be used
import datetime
import libfunc as func

id = input("ID: ")
password = input("Password: ")

access_granted = False

#Password input needs to match to access program
if password == "islington":
    access_granted = True   
else:
    print("Incorrect Password")

#Initializing the usable variables   
books = func.storedList()
bookdict = {str(books[0][0]):0,str(books[1][0]):1,str(books[2][0]):2,str(books[3][0]):3}
rate = func.getRate()
uniqueid = func.getUniqeID()

#main loop
while access_granted:
    print("User: "+ id +"\n")

    print("Status: \n")
    func.display()       

    #main action input
    action = int(input("Loan Book[1], Return Book[2], Display All Books[3], Log Out[4]"))

    if action == 1:
        bookname = input("Which book? ")
        if func.chkBookname(bookname):            
            name = input("What is borrowers' Name? ")
            quantity = int(input("How many books? "))
            for i in bookdict:
                if bookname == i:
                    bookname = bookdict[i]          
            if func.chkStock(bookname,quantity):
                func.loan(bookname,quantity)
                func.reciept(name,bookname,quantity,rate,uniqueid)
                #Code for visual cue on the UI
                print("-----------------------------------------|LOAN|---------------------------------------------")
                print("Name: " + name)
                print("Book: " + str(books[bookname][0]))
                print("Quantity: " + str(quantity))
                print("Amount: $" + str(func.transcation(bookname,quantity))+ "0")
                print("Librarian: "+ id)
                print("--------------------------------------------------------------------------------------------")
            else:
                #Code for visual cue on the UI
                print("--------------------------------------------------------------------------------------------")
                print("Invaild Transcation!")
                print("")
                print("Copies available: " + str(books[bookname][2]))
                print("")
                quantity = int(input("How many books? "))
                print("--------------------------------------------------------------------------------------------")
                if (quantity <= int(books[bookname][2])):
                    func.loan(bookname,quantity)
                    func.reciept(name,bookname,quantity,rate,uniqueid)
                    #Code for visual cue on the UI
                    print("-----------------------------------------|LOAN|---------------------------------------------")
                    print("Name: " + name)
                    print("Book: " + str(books[bookname][0]))
                    print("Quantity: " + str(quantity))
                    print("Amount: $" + str(func.transcation(bookname,quantity) + "0"))
                    print("Librarian: "+ id)
                    print("--------------------------------------------------------------------------------------------")
        
            uniqueid += 1 
            func.UpdateUniqueID(uniqueid)
        else:
            print("Book not in the Library")    

    if action == 2:
        bookname = input("Which book? ")
        if func.chkBookname(bookname):
            name = input("What is borrowers' Name? ")
            quantity = int(input("How many books? "))
            days = int(input("Number of days borrowed? "))
            for i in bookdict:
                if bookname == i:
                    bookname = bookdict[i]
            func.returnBook(name,bookname,quantity)
            amount = func.transcation(bookname,quantity)
            func.recieptstudent(name,bookname,quantity,rate,uniqueid,days)
            #Code for visual cue on the UI
            print("-----------------------------------------|RETURN|-------------------------------------------")
            print("Name: " + name)
            print("Book: " + str(books[bookname][0]))
            print("Quantity: " + str(quantity))
            print("Amount: $" + str(func.transcation(bookname,quantity)+func.overdued(days,quantity))+"0")
            print("Librarian: "+ id)
            print("--------------------------------------------------------------------------------------------")
        else:
            print("Book not from this Library")

    #Extra Feature to view books
    if action == 3:
        func.display()

    #Exit from the program
    if action ==4:
        print("Good Bye " + id)
        access_granted = False

    print("")
    
        
         
