#Functions for library
import datetime

todaysDate = str(datetime.date.today())
now =datetime.datetime.now()
time = str(now.strftime("%Y-%m-%d %H: %M: %S"))
x = 0

def read():
    file = open(".//resource//stock.txt","r")
    for line in file:
        print(line.strip("\n"))
    file.close()    

def storedList():
    books = []
    file = open(".//resource//stock.txt","r")
    for line in file:
        books.append(line.strip("\n").split(","))
    file.close()    
    return books

def chkStock(bookname,quantity):
    books = storedList()
    if int(books[bookname][2]) > quantity-1: 
            return True 

def loan(bookname,quantity):
    books = storedList()
    q = int(books[bookname][2])
    r = q - quantity
    books[bookname][2] = r
    
    file = open(".//resource//stock.txt","w")
    for i in books:
        file.writelines(str(i[0]) +","+ str(i[1])+ "," + str(i[2]) + ","+ str(i[3])+"\n")
    file.close()

def reciept(name,bookname,quantity,rate,uniqueid):
    books = storedList()
    book = books[bookname][0]

    file = open(name+str(uniqueid)+".txt","w")
    file.write("-----------------------------------------|LOAN|---------------------------------------------" +"\n")
    file.write("Time: " + time + "\n")
    file.write("--------------------------------------------------------------------------------------------"+"\n")
    file.write("Name: " + name +"\n")
    file.write("Borrowed: ")
    file.write(str(book) + ", " + str(quantity) + "," + rate+"\n")
    file.write("Amount: $" + str(transcation(bookname,quantity))+"0 \n")
    file.write("--------------------------------------------------------------------------------------------")
    file.close()

def recieptstudent(name,bookname,quantity,rate,uniqueid,days):
    books = storedList()
    book = books[bookname][0]

    file = open("Return_"+name+str(uniqueid)+".txt","w")
    file.write("-----------------------------------------|RETURN|-------------------------------------------"+"\n")
    file.write("Time: " +time + "\n")
    file.write("--------------------------------------------------------------------------------------------"+"\n")
    file.write("Name: " + name +"\n")
    file.write("Returned: ")
    file.write(str(book) + ", " + str(quantity) + "," + rate +"\n")
    file.write("Amount: $"+str(transcation(bookname,quantity) + overdued(days,quantity))+"0 \n")
    file.write("--------------------------------------------------------------------------------------------")
    file.close()

def getRate(bookname=0):
    return storedList()[bookname][3]   

def returnBook(name,bookname,quantity):
    books = storedList()
    book = books[bookname][0]
    
    q = int(books[bookname][2])
    r = q + quantity
    books[bookname][2] = r

    file= open(".//resource//stock.txt","w")
    for i in books:
        file.writelines(str(i[0]) +","+ str(i[1])+ "," + str(i[2]) + ","+ str(i[3])+"\n")
    file.close()   

def transcation(bookname,quantity):
    rate = float(getRate(bookname).replace("$",""))
    total = quantity * rate
    return total

def display():
    print("--------------------------------------------------------------------------------------------")
    print("Book Name         Author               Quantity   Price(per 10 day)")
    print("--------------------------------------------------------------------------------------------")

    file = open(".//resource//stock.txt","r")
    for line in file:
        print(line.replace(",","  \t  "))

    print("--------------------------------------------------------------------------------------------")

def getUniqeID():
    file = open(".//resource//uniqueid.txt","r")
    uniqueid = int(file.readline())
    file.close
    return uniqueid

def UpdateUniqueID(uniqueid):
    file = open(".//resource//uniqueid.txt","w")
    file.write(str(uniqueid))
    file.close

def chkBookname(bookname):
    books = storedList()
    for i in books:
        if bookname in i[0]:
            return True
    else:
        return False

def overdued(days,quantity):
    if days > 10:        
        return int(0.50*(days - 10)*quantity) 
    else:
        return int(0)
