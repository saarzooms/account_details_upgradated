import cx_Oracle
from account import *
from customer import customer
import datetime
from fileinput import close
now = datetime.datetime.now()
# global cust
# global acc
def printClosedAccountHistory():
    con = cx_Oracle.connect('system/sys123@127.0.0.1/XE')
    cur = con.cursor()
    
    cur.execute("SELECT * FROM account where status='Deactive' ")
    results = cur.fetchall()
    if(int(cur.rowcount)>0):
        print('Closed account History')
        for row in results:
            acc_no = row[1]
            closedt = row[6]
            print(acc_no," ",closedt)
    con.commit()
    con.close()
def printFDReport():
    cust_id = input("Enter Customer_id")
    con = cx_Oracle.connect('system/sys123@127.0.0.1/XE')
    cur = con.cursor()
    
    cur.execute("select acc_no,amount,terms from fixed_deposit where customer_no = :cust_id",(cust_id))
    results = cur.fetchall()
    if(int(cur.rowcount)>0):
        print('FD Report for customer :',cust_id)
        print("acc_no"," ","amount"," ","terms")
        for row in results:
            acc_no = row[1]
            amount = row[2]
            terms = row[3]
            print(acc_no," ",amount," ",terms)
    else:
        print("N.A")
    con.commit()
    con.close()
def  printFDReportwithAnotherCustomer():
    cust_id = input("Enter Customer_id")
    con = cx_Oracle.connect('system/sys123@127.0.0.1/XE')
    cur = con.cursor()
    
    cur.execute("select * from fixed_deposit where amount > (select sum(amount) from fixed_deposit where customer_no =:cust_id)",(cust_id))
    results = cur.fetchall()
    if(int(cur.rowcount)>0):
        print('FD Report with respect to  customer :',cust_id)
        print("customer_no"," ","acc_no"," ","amount"," ","terms")
        for row in results:
            cust_no = row[4]
            acc_no = row[1]
            amount = row[2]
            terms = row[3]
            print(cust_no," ",acc_no," ",amount," ",terms)
    else:
        print("NA")
    con.commit()
    con.close()
def  printFDReportwithamount():
    amnt = input("Enter amount")
    con = cx_Oracle.connect('system/sys123@127.0.0.1/XE')
    cur = con.cursor()
    
    cur.execute("select fd.customer_no as cust_id, cd.cust_fname,cust_lname,fd.amount from fixed_deposit fd inner join customer_details cd on fd.customer_no=cd.customer_no where amount > :amnt)",(amnt))
    results = cur.fetchall()
    if(int(cur.rowcount)>0):
        print('FD Report with amount :',amnt)
        print("customer_no"," ","First Name"," ","Last Name"," ","amount")
        for row in results:
            cust_no = row[1]
            fname = row[2]
            lname = row[3]
            amount = row[4]
            print(cust_no," ",fname," ",lname," ",amount)
    else:
        print("NA")
    con.commit()
    con.close()
def printLoanReport():
    cust_id = input("Enter Customer_id")
    con = cx_Oracle.connect('system/sys123@127.0.0.1/XE')
    cur = con.cursor()
    
    cur.execute("select acc_no,amount,terms from loan where customer_no = :cust_id",(cust_id))
    results = cur.fetchall()
    if(int(cur.rowcount)>0):
        print('loan Report for customer :',cust_id)
        print("acc_no"," ","amount"," ","terms")
        for row in results:
            acc_no = row[1]
            amount = row[2]
            terms = row[3]
            print(acc_no," ",amount," ",terms)
    else:
        print("N.A")
    con.commit()
    con.close()
def  printLoanReportwithAnotherCustomer():
    cust_id = input("Enter Customer_id")
    con = cx_Oracle.connect('system/sys123@127.0.0.1/XE')
    cur = con.cursor()
    
    cur.execute("select * from loan where amount > (select sum(amount) from loan where customer_no =:cust_id)",(cust_id))
    results = cur.fetchall()
    if(int(cur.rowcount)>0):
        print('Loan Report with respect to  customer :',cust_id)
        print("customer_no"," ","acc_no"," ","amount"," ","terms")
        for row in results:
            cust_no = row[4]
            acc_no = row[1]
            amount = row[2]
            terms = row[3]
            print(cust_no," ",acc_no," ",amount," ",terms)
    else:
        print("NA")
    con.commit()
    con.close()
def  printLoanReportwithamount():
    amnt = input("Enter amount")
    con = cx_Oracle.connect('system/sys123@127.0.0.1/XE')
    cur = con.cursor()
    
    cur.execute("select l.customer_no as cust_id, cd.cust_fname,cust_lname,l.amount from loan l inner join customer_details cd on l.customer_no=cd.customer_no where amount > :amnt)",(amnt))
    results = cur.fetchall()
    if(int(cur.rowcount)>0):
        print('Loan Report with amount :',amnt)
        print("customer_no"," ","First Name"," ","Last Name"," ","amount")
        for row in results:
            cust_no = row[1]
            fname = row[2]
            lname = row[3]
            amount = row[4]
            print(cust_no," ",fname," ",lname," ",amount)
    else:
        print("NA")
    con.commit()
    con.close()
def printFDLoanReportwithamount():
    con = cx_Oracle.connect('system/sys123@127.0.0.1/XE')
    cur = con.cursor()
    
    cur.execute("select cd.customer_no,cd.cust_fname,cd.cust_lname,fd.sum_fixed, l.sum_loan from customer_details cd inner join (select sum(amount) as sum_fixed, customer_no from fixed_deposit group by customer_no) fd on fd.customer_no = cd.customer_no inner join (select sum(amount) as sum_loan, customer_no from loan group by customer_no) l on l.customer_no = cd.customer_no")
    results = cur.fetchall()
    if(int(cur.rowcount)>0):
        print('FD Loan Report with amount ')
        print("customer_no"," ","First Name"," ","Last Name"," ","sum fixed deposit amount"," ","sum loan amount")
        for row in results:
            cust_no = row[1]
            fname = row[2]
            lname = row[3]
            famount = row[4]
            lamount = row[5]
            if(lamount>famount):
                print(cust_no," ",fname," ",lname," ",famount," ",lamount)
    else:
        print("NA")
    con.commit()
    con.close()
def printNoFDReport():
    con = cx_Oracle.connect('system/sys123@127.0.0.1/XE')
    cur = con.cursor()
    
    cur.execute("select customer_no,cust_fname,cust_lname from customer_details where customer_no not in (select distinct(customer_no) from fixed_deposit)")
    results = cur.fetchall()
    if(int(cur.rowcount)>0):
        print('No FD Report')
        print("customer_no"," ","First Name"," ","Last Name")
        for row in results:
            cust_no = row[1]
            fname = row[2]
            lname = row[3]
            
            if(lamount>famount):
                print(cust_no," ",fname," ",lname)
    else:
        print("NA")
    con.commit()
    con.close()
def printNoLoanReport():
    con = cx_Oracle.connect('system/sys123@127.0.0.1/XE')
    cur = con.cursor()
    
    cur.execute("select customer_no,cust_fname,cust_lname from customer_details where customer_no not in (select distinct(customer_no) from  loan)")
    results = cur.fetchall()
    if(int(cur.rowcount)>0):
        print('No Loan Report')
        print("customer_no"," ","First Name"," ","Last Name")
        for row in results:
            cust_no = row[1]
            fname = row[2]
            lname = row[3]
            
            if(lamount>famount):
                print(cust_no," ",fname," ",lname)
    else:
        print("NA")
    con.commit()
    con.close()
def printNoLoanFD():
    con = cx_Oracle.connect('system/sys123@127.0.0.1/XE')
    cur = con.cursor()
    
    cur.execute("select customer_no,cust_fname,cust_lname from customer_details where customer_no not in (select distinct(fd.customer_no) from fixed_deposit fd inner join loan on fd.customer_no = loan.customer_no)")
    results = cur.fetchall()
    if(int(cur.rowcount)>0):
        print('No FD Loan Report ')
        print("customer_no"," ","First Name"," ","Last Name")
        for row in results:
            cust_no = row[1]
            fname = row[2]
            lname = row[3]
            
            if(lamount>famount):
                print(cust_no," ",fname," ",lname)
    else:
        print("NA")
    con.commit()
    con.close()
def signUp():
    print('in sign up')
    First_name = input("Enter First name")
    Last_name = input("Enter Last name")
    Address_line1 = input("Enter Your Address line 1")
    Address_line2 = input("Enter Your Address line 2")
    City = input("Enter your city")
    Pincode = input("Enter Pin code")
    Pincode = int(Pincode)
     # State = raw_input("Enter state")
   # Account_type = input("Enter account type 'saving / current / fixed deposit/ loan'")
    password = input("Enter password")
    cust = customer("0",First_name,Last_name,Address_line1,Address_line2,Pincode,City,password)
    cust_id = cust.signUp()
#     if(Account_type=='saving'):
#         acc = savingaccount(now.strftime("%Y-%m-%d"),'0',0,cust_id,0)
#     else:
#         acc = currentaccount(now.strftime("%Y-%m-%d"),'0',5000,cust_id)
#     acc.openAccount()
def openAccount():
    print("1.Saving account")
    print("2.Current account")
    print("3.Fixed Deposit account")
    type = input("Enter your new account type")
    if(type=='1'):
        acc = savingaccount(now.strftime("%Y-%m-%d"),'0',0,cust_id,0)
    elif(type=='2'):
        acc = currentaccount(now.strftime("%Y-%m-%d"),'0',5000,cust_id)
    elif(type=='3 '):
        terms = int(input("Enter terms"))
        while True:
            amnt = int(input("Enter amount"))
            if amnt%1000 == 0:
                break
        acc = fixedaccount(now.strftime("%Y-%m-%d"),'0',0,cust_id,amnt,terms)
    acc.openAccount()
def getAccount():
    global acc
    acc_no = input("Enter Account number")
    con = cx_Oracle.connect('system/sys123@127.0.0.1/XE')
    cur = con.cursor()
    cur.execute("SELECT * FROM account where customer_no=:custid and acc_no=:accno",(cust_id,acc_no))
    results = cur.fetchall()
    if int(cur.rowcount)>0:
        for row in results:
            acc_type = row[1]
            openDt = row[2]
            
def login():
    global cust
    global cust_id
    returnvalue  = True
    cust_id = input("Enter Customer ID")
    password = input("Enter Password")
    con = cx_Oracle.connect('system/sys123@127.0.0.1/XE')
    cur = con.cursor()
    cur.execute("SELECT * FROM customer_details where customer_no=:custid and cust_pass=:cust_pass",(cust_id,password))
    results = cur.fetchall()
    if(int(cur.rowcount)>0):
        for row in results:
            f_name = row[1]
            l_name = row[2]
            addrline1 = row[3]
            addrline2 = row[4]
            pincode = row[5]
            city = row[6]
            
            cust = customer(cust_id,f_name,l_name,addrline1,addrline2,pincode,city,password)
        print("Successfully login ")
        print("welcome "+f_name+" "+l_name)
        cur.execute("SELECT * FROM account where customer_no=:custid",(cust_id))
        results = cur.fetchall()
        if(int(cur.rowcount)>0):
            for row in results:
                acc_no = row[0]
                acc_type = row[1]
                openedDate = row[2]
                balance = row[3]
                closedDate = row[5]
                status = row[6]
            if status == 'Active':
                if acc_type=='saving':
                    cur.execute("SELECT * FROM saving_account where acc_no=:accno",(acc_no))
                    results = cur.fetchall()
                    if(int(cur.rowcount)>0):
                        for row in results:
                            withdrawcount = row[1]
                        acc = savingaccount(openedDate,acc_no,balance,cust_id,withdrawcount)
                else:
                    acc = currentaccount(openedDate,acc_no,balance,cust_id)
            else:
                print('Your account is not active')
                returnvalue = False
    else:
        returnvalue = False
        print('wrong user name or password')
    con.commit()
    con.close()
    return returnvalue
Quit = 1
while Quit==1:        
    print ("===========================================")
    print("1.Sign UP")
    print("2.Login")
    print("3.Admin Login")
    print("0.Quit")
    print ("===========================================")
    ch = input ("Enter your choice")
    if ch == '1':
        signUp()
    elif ch == '2':
        if(login()):
            option2 = 1
            while option2 == 1:
                print ("===========================================")
                print("1.Address Change")
                print("2.Open New Account")
                print("3.Money Deposit")
                print("4.Money Withdrawal")
                print("5.Print Statement")
                print("6.Transfer Money")
                print("7.Account Closure")
                print("8.Available Loan")
                print("0.Customer Logout")
                ch = input ("Enter your choice")
                print("==========================================")
                choice = input ("Enter your choice")
                if choice == '1':
                    print("in address change")
                    cust.changeAddress()
                elif choice == '2':
                    openAccount()
                elif choice == '3':
                    amnt = int(input("Enter deposit amount"))
                    acc.deposit(amnt)
                elif choice == '4':
                    amnt = int(input("Enter withdraw amount"))
                    acc.withdraw(amnt)
                elif choice == '5':
                    acc.printStatement()
                elif choice == '6':
                    amnt = int(input("Enter Transfer amount"))
                    acc_no = input("Enter Transfer account no")
                    acc.transfer(amnt,acc_no)
                elif choice == '7':
                    acc.accountClosure()
                elif choice == '8':
                    acc.accountClosure()
                elif choice == '0':
                    print('Successfully logout')
                    option2 = 0    
    elif ch == '3':
        username = input("Enter User name")
        upass = input("Enter Password")
        if(username=='admin' & upass=='admin'):
            Option2 = 1
            while option2 == 1:
                print ("===========================================")
                print("1.Print Closed Account History")
                print("2. FD Report of a customer")
                print("3.FD report of customer vis-a-vis another customer")
                print("4. FD report w.r.t. a particular FD amount")
                print("5. Loan Report of a customer")
                print("6.Loan report of customer vis-a-vis another customer")
                print("7. Loan report w.r.t. a particular Loan amount")
                print("8.Loan - FD Report of Customers")
                print("9.Report of customer who are yet to avail a loan")
                print("10.Report of customer who are yet to open an FD account")
                print("11.Report of customer who neither have a loan nor an FD account with bank")
                print("0.Admin logout")
                print ("===========================================")
                choice = input ("Enter your choice")
                if choice == '1':
                    printClosedAccountHistory()
                elif choice == '2':
                    printFDReport()
                elif choice == '3':
                    printFDReportwithAnotherCustomer()
                elif choice == '4':
                    printFDReportwithamount()
                elif choice == '5':
                    printLoanReport()
                elif choice == '6':
                    printLoanReportwithAnotherCustomer()
                elif choice == '7':
                    printLoanReportwithamount()
                elif choice == '8':
                    printFDLoanReportwithamount()
                elif choice == '9':
                    printNoLoanReport()
                elif choice == '10':
                    printNoFDReport()
                elif choice == '11':
                    printNoLoanFD()
                elif choice == '0':
                    print('Successfully logout')
                    option2 = 0  
        print("Thanks for using this system")               
    elif ch == '4':
        Quit = 0
        print("Thanks for using this system")
            




