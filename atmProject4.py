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

def init():

  now = datetime.now()
  print (now)
  print("Welcome to Bank Py")
  try: 
    haveAccount = int(input("Do you have an account with us? 1 for yes and 2 for no: "))

    if (haveAccount == 1):
      login()
    elif (haveAccount == 2):
      register()
  except ValueError:
    print("Please enter a number")
    init()
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
      database.createCurrentSesh(accountNumFromUser, user)
      bankOp(user)
      
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

  isUserCreated = database.create(accountNumber,fName,lName,email,password)
  
  
  if isUserCreated:
    print("Your account has been created")
    print("=== ==== ==== ==== ==== ==== ===")
    print("Your account number is %d " %accountNumber)
    print("=== ==== ==== ==== ==== ==== ===")
    print("Keep this information safe")
    print("=== ==== ==== ==== ==== ==== ===")

    login()

  else:
    print("Something went wrong. Please try again")
    register()




def bankOp(user):
  print ("Welcome %s %s!" %(user[0], user[1]))
 
  print("These are the available options: ")
  print("1. Withdrawal ")
  print("2. Cash Deposit ")
  print("3. Complaint ")
  print("4. Logout")
  
  choice = int(input("What option number would you like to do today? "))

  if (choice ==1):
    withdrawal(user)
  elif (choice ==2):
    deposit(user)
  elif (choice ==3):
    complaint()
  elif (choice ==4):
    logout()
    init()
  else:
    print("Invalid option)")
    bankOp(user) 


def withdrawal(user):
  currentAmount = float(user[4])
  print ("Your current balance is $%.2f" %currentAmount)
  withdraw = float (input("How much would you like to withdraw? $"))
  try: 
    if (withdraw <= currentAmount):
      balance = currentAmount - withdraw
      #updateBalance = database.update(balance)
      #newAmount = user[0] + "," + user[1] + "," + user[2] + "," + user[3] + "," + str(balance)
      isNewAmount = database.newAmountTotal(accountNumFromUser, user) 
      if (isNewAmount): 
        print("Your new balance is $%.2f" %balance)
        print ("Please take your cash")
      else: 
        print("Not enough funds in your account")

  except AttributeError:
    print("Please try again")
    withdrawal(database)

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
 

def deposit(user):
  currentAmount = float(user[4])
  print ("Your current balance is $%.2f" %currentAmount)
  depo = float (input("How much would you like to deposit? $"))

  try: 
    balance = currentAmount + depo
    #newAmount = user[0] + "," + user[1] + "," + user[2] + "," + user[3] + "," + str(balance)
    isNewAmount = database.newAmountTotal(accountNumFromUser, user) 
    if (isNewAmount): 
      print ("Please insert your cash")
      print("Your new balance is $%.2f" %balance)

  except AttributeError:
    print("Please try again")
    deposit(user)
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
  database.deleteCurrentSesh(accountNumFromUser)
  print("Goodbye")


def genAccount():
  return random.randrange(1111111111,9999999999)

#print (genAccount())

init()