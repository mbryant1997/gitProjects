#create record
#update record
#read record
#delete record
import os
import validation

userDbPath = "data/user_record/"
currentPath = "data/auth_session/"

def create(userAccountNum, fName, lName, email, password):
  #create a FileExistsError
  #name of file is accountNumber.txt
  #add user details to filter
  #return true
  #if saving to file fails, then delete created file

  userDataInfo = fName + "," + lName + "," + email + "," + password+ "," + str(0)

  if (doesAccountNumExist(userAccountNum)):
    return False
  
  if (doesEmailExist(email)):
    print("user already exists")
    return False

  completionState = False
  try:
    f = open(userDbPath + str(userAccountNum) + ".txt", "x")
  except FileExistsError:
    #delete the already created file, and print out error, then return false
    #check contents of file before deleting 
    doesFileContainData = read(userDbPath + str(userAccountNum) + ".txt")   
    if not (doesFileContainData):
      delete(userAccountNum)
  else: 
    f.write(str(userDataInfo))
    completionState = True
  finally:
    f.close()
    return completionState

def read(userAccountNum):
  #find user with account number
  #fetch content of the file
  isValidAccountNum = validation.accountNumValidate(userAccountNum)
  try: 
    if isValidAccountNum:
      f = open(userDbPath + str(userAccountNum) + ".txt", "r")
    else: 
      f = open(userDbPath + userAccountNum, "r")
  except FileNotFoundError:
    print("user not found")
  except FileExistsError:
    print("file doesn't exist")
  except TypeError:
    print("invalid account number format")
  else:
    return f.readline()


def update(userAccountNum): 
  #find user with account number
  #search content of file
  #update content
  #save file 
  #return true
  pass


def newAmountTotal(userAccountNum, user):
      #updateBalance = database.update(balance)
  newAmount = user[0] + "," + user[1] + "," + user[2] + "," + user[3] + "," + str(user[4])
  try: 
    f = open(userDbPath + str(userAccountNum) + ".txt", "w")
  except AttributeError:
    print("please try again")
  else: 
    f.write(newAmount)
  finally: 
    f.close()
    return True


def delete (userAccountNum):
  #find user with account number
  #delete the user record (file)
  #return true
  isDeleteSuccess = False

  if os.path.exists(userDbPath + str(userAccountNum) + ".txt"):
    try:
      os.remove(userDbPath + str(userAccountNum) + ".txt")
      isDeleteSuccess = True
    except FileNotFoundError:
      print("file not found")
    finally:
      return isDeleteSuccess

def doesAccountNumExist(userAccountNum):
#find user with the data record
  allUsers = os.listdir(userDbPath)
  for user in allUsers:
    #userList = str.split(read(user), ",")
    if (str(userAccountNum) + ".txt" in user):
      return True

  return False

def doesEmailExist(email):
#find user with the data record
  allUsers = os.listdir(userDbPath)
  for user in allUsers:
    userList = str.split(read(user), ",")
    if (email in userList):
      return True

  return False


def authenticateUser(accountNumber, password):
  if (doesAccountNumExist(accountNumber)):
    user = str.split(read(accountNumber), ",")
    if (password == user[3]):
      return user

  return False

def createCurrentSesh(userAccountNum, user):
  #userDataInfo = fName + "," + lName + "," + email + "," + password+ "," + balance
  f = ""
  completionState = False
  try: 
    f = open(currentPath + str(userAccountNum) + ".txt", 'x')
  except FileExistsError:
    #delete the already created file, and print out error, then return false
    return completionState
  else: 
    f.write(str(user))
    completionState = True
    print( "You have logged in")
    f.close()
  finally: 
    return completionState


def deleteCurrentSesh(userAccountNum):
  isDeleteSuccess = False

  if os.path.exists(currentPath + str(userAccountNum) + ".txt"):
    try:
      os.remove(currentPath + str(userAccountNum) + ".txt")
      isDeleteSuccess = True
    except FileNotFoundError:
      print("file not found")
    finally:
      return isDeleteSuccess

#create(6663712892, ['Mekhi', 'Bryant', 'mekhibryant97@gmail.com', 'password', 302])
#delete (6663712892)
#print(read (1493712892))
#print(doesEmailExist("lauren@gmail.com"))
#print(doesAccountNumExist(8311729528))
#print(doesAccountNumExist(5425108243))
#authenticateUser(2078135735, "password")
#create(5243951234, "Naomi", "Bryant", "nai@gmail.com", "yessir")
#update(2078135735)
#createCurrentSesh(2078135735)
#deleteCurrentSesh(2078135735)
