from datetime import datetime


#register
# username, password, and email address
#generate user account


# login
#username or email and password

#bank operations

#initialize the System

database = {} #dictionary
import random

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
  accountNumFromUser = int(input ("What is your account number? To go back, press 0 \n"))
  if (accountNumFromUser == 0):
    init()
  passwordUser = input ("What is your password?\n")
  
  for accountNumber, password in database.items():
    if (accountNumber == accountNumFromUser):
      if (password[3] == passwordUser):
        bankOp(password)
    
    else:
      print ("Invalid password")
      login()


def register():

  print ("***Please Register***")
  email = input ("What is your email address?\n")
  fName = input ("What is your first name? \n")
  lName = input ("What is your last name?\n")
  password = input ("Create a password for yourself \n" )

  accountNumber = genAccount() 
  database[accountNumber] = [fName, lName, email, password]

  print("Your account has been created")
  print("=== ==== ==== ==== ==== ==== ===")
  print("Your account number is %d " %accountNumber)
  print("=== ==== ==== ==== ==== ==== ===")
  print("Keep this information safe")
  print("=== ==== ==== ==== ==== ==== ===")

  login()

def bankOp(database):
  print ("Welcome %s %s!" %(database[0], database[1]))
 
  print("These are the available options: ")
  print("1. Withdrawal ")
  print("2. Cash Deposit ")
  print("3. Complaint ")
  print("4. Logout")
  
  choice = int(input("What option number would you like to do today? "))

  if (choice ==1):
    withdrawal()
  elif (choice ==2):
    deposit()
  elif (choice ==3):
    complaint()
  elif (choice ==4):
    logout()
    init()
  else:
    print("Invalid option)")
    bankOp(database) 


def withdrawal():
  draw = float (input("How much would you like to withdraw? $"))
  print ("Please take your cash")
  check = True
  while check == True:
    anyMore = int(input ("Is that all for today? 1 for yes and 2 for no \n"))
    if (anyMore ==1):
      check = False
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