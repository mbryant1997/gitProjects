from datetime import datetime
import random
import validation
import database
from getpass import getpass
#register
# username, password, and email address
#generate user account


# login
#username or email and password

#bank operations

#initialize the System


"""database = {
  1493712892 : ['Mekhi', 'Bryant', 'mekhibryant97@gmail.com', 'password', 302]
    } #dictionary
"""

def init():

  now = datetime.now()
  print (now)
  print("Welcome to Bank Py")
  haveAccount = int(input("Do you have an account with us? 1 for yes and 2 for no: "))

  if (haveAccount == 1):
    login()
  elif (haveAccount == 2):
    register()
  else: 
    print("You have selected an invalid option")
    init()
  

def login():

  print("Login to your account")
  global accountNumFromUser
  accountNumFromUser = (input ("What is your account number? To go back, press 0 \n"))
  if (accountNumFromUser == 0):
      init()
  isValidAccountNum = validation.accountNumValidate(accountNumFromUser)
  
  if isValidAccountNum:  

    #passwordUser = input ("What is your password?\n")
    passwordUser = getpass("What is your password?\n")
    user= database.authenticateUser(accountNumFromUser, passwordUser)

    if (user):
      bankOp(user)

    #for accountNumber, password in database.items():
     # if (accountNumber == int(accountNumFromUser)):
      #  if (password[3] == passwordUser)
          #bankOp(password)
      
    else:
      print ("Invalid password")
      login()

  else:
    print ("Account number invalid: check that you have 10 digits and only integers")
    init()



def register():

  print ("***Please Register***")
  email = input ("What is your email address?\n")
  fName = input ("What is your first name?\n")
  lName = input ("What is your last name?\n")
  #password = input ("Create a password for yourself \n" )
  password = getpass ("Create a password for yourself:\n" )

  accountNumber = genAccount()
  #preparedUserDetails = fName + ", " + lName + ", " + email + ", " + password+ ", " + str(0)
  #database[accountNumber] = [fName, lName, email, password]
  isUserCreated = database.create(accountNumber,fName,lName,email, password)
  
  
  if isUserCreated:
    print("Your account has been created")
    print("=== ==== ==== ==== ==== ==== ===")
    print("Your account number is %d " %accountNumber)
    print("=== ==== ==== ==== ==== ==== ===")
    print("Keep this information safe")
    print("=== ==== ==== ==== ==== ==== ===")

    login()

  else:
    print("something went wrong. please try again")
    register()




def bankOp(database):
  print ("Welcome %s %s!" %(database[0], database[1]))
 
  print("These are the available options: ")
  print("1. Withdrawal ")
  print("2. Cash Deposit ")
  print("3. Complaint ")
  print("4. Logout")
  
  choice = int(input("What option number would you like to do today? "))

  if (choice ==1):
    withdrawal(database)
  elif (choice ==2):
    deposit(database)
  elif (choice ==3):
    complaint()
  elif (choice ==4):
    logout()
    init()
  else:
    print("Invalid option)")
    bankOp(database) 


def withdrawal(database):
  withdraw = float (input("How much would you like to withdraw? $"))
  print ("withdraw is $%.2f" %withdraw)
  currentAmount = float(database[4])
  print ("current is $%.2f" %currentAmount)
  #try: 
  if (withdraw <= currentAmount):
    balance = currentAmount - withdraw
    #updateBalance = database.update(balance)
    newAmount = database[0] + "," + database[1] + "," + database[2] + "," + database[3] + "," + str(balance)
    print (newAmount) 
    isNewAmount = database.newWithdrawl(accountNumFromUser, database, newAmount) 
    print (isNewAmount)
    if (isNewAmount): 
      print("check 1")
      print("Your new balance is $%.2f" %balance)
      print ("Please take your cash")

      
  #except AttributeError:
   # print("attribute error")
    #withdrawal(database)

  else: 
      print("Not enough funds in your account")

  check = True
  while check == True:
    anyMore = int(input ("Is that all for today? 1 for yes and 2 for no \n"))
    if (anyMore ==1):
      check = False
      logout()
      init()
    elif (anyMore == 2):
      check=False
      login()
    else:
      print("Invalid option")
      check = True
 

def deposit():
  depo = float (input("How much would you like to deposit? $"))
  print("Your current balance is $%.2f" %depo)
  check = True
  while check == True:
    anyMore = int(input ("Is that all for today? 1 for yes and 2 for no \n"))
    if (anyMore ==1):
      check = False
      logout()
      init()
    elif (anyMore == 2):
      check=False
      login()
    else:
      print("Invalid option")
      check = True
  

def complaint():
  issue = input ("What issue would you like to report? ")
  print ("Thank you for contacting us")
  check = True
  while check == True:
    anyMore = int(input ("Is that all for today? 1 for yes and 2 for no \n"))
    if (anyMore ==1):
      check = False
      logout()
      init()
    elif (anyMore == 2):
      check=False
      login()
    else:
      print("Invalid option")
      check = True
  

def logout():
  print("Goodbye")


def genAccount():
  return random.randrange(1111111111,9999999999)

#print (genAccount())

init()