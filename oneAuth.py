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

  isValidOption = False
  print("Welcome to bank Rob")
  
  while isValidOption == False:
    haveAccount = int(input("Do you have an account with us? 1 for yes, and 2 for no "))

 
    if (haveAccount == 1):
      isValidOption = True
      login()
    elif (haveAccount == 2):
      isValidOption = True
      register()

    else: 
      print("You have selected an invalid option")
      isValidOption = False
    

def login():

  print("Login to your account")
  loginSuccess = False

  while loginSuccess == False:
    accountNumFromUser = int(input ("What is your account number?\n"))
    passwordUser = input ("What is you password?\n")
    
    for accountNumber, userDeatils in database.items():
      if (accountNumber == accountNumFromUser):
        if (userDetails[3] == passwordUser):
          loginSuccess = True
    print ("Invalid password")

    bankOp(userDetails)

def register():
  print ("***Please Register***")

  email = input ("What is your email address?\n")
  fName = input ("What is your first name? \n")
  lName = input ("What is your last name?\n")
  password = input ("Create a password for yourself \n" )

  accountNumber = genAccount()

  userDetails = [fName, lName, email, password]
 

  database[accountNumber] = [fName, lName, email, password]

  print("Your account has been created")
  print("=== ==== ==== ==== ==== ==== ===")
  print("Your account number is %d " %accountNumber)
  print("=== ==== ==== ==== ==== ==== ===")
  print("Keep this information safe")
  print("=== ==== ==== ==== ==== ==== ===")


  login()

def bankOp(user):
  #print ("Welcome %s %s" %(user[0], user[1])
  
  check = True
 
  print("These are the available options: ")

  print("1. Withdrawal ")
  print("2. Cash Deposit ")
  print("3. Complaint ")
  print("4. Logout")
  
  while (check == True):
    choice = int(input("What option number would you like to do today? "))

    if (choice ==1):
      withdrawal()
    elif (choice ==2):
      deposit()
    elif (choice ==3):
      complaint()
    elif (choice ==4):
      login()
    else:
      print("Invalid option)")
      check = True


def withdrawal():
  draw = float (input("How much would you like to withdraw? $"))
  print ("Please take your cash")

def deposit():
  depo = float (input("How much would you like to deposit? $"))
  print("Your current balance is $%.2f" %depo)

def complaint():
  issue = input ("What issue would you like to report? ")
  print ("Thank you for contacting us")

def logout():
  print("Goodbye")


def genAccount():
  return random.randrange(1111111111,9999999999)

#print (genAccount())

init()


