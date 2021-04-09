from datetime import datetime
allowedUser = ["Mekhi", "Jelani"]
allowedPass = ["Alpha", "gorilla"]
condition = True
while condition == True:
  user = input("What is your name? ")

  if (user in allowedUser):
      passWord = input("What is your password? ")
      
      userPositioninList = allowedUser.index(user)

      if (passWord == allowedPass[userPositioninList]):
          condition = False
          update = True
          now = datetime.now()
          print (now)
          print("Welcome %s!" % user)
          while update == True:
            print("These are the available options: ")

            print("1. Withdrawal ")
            print("2. Cash Deposit ")
            print("3. Complaint ")
            print("4. Logout")

            choice = int(input("What option number would you like to do today? "))

            if (choice == 1):
              print("You selected: %s" %choice)
              draw = float (input("How much would you like to withdraw? $"))
              print ("Please take your cash")
            elif (choice == 2):
              print("You selected: %s" %choice)
              depo = float (input("How much would you like to deposit? $"))
              print("Your current balance is $%.2f" %depo)
            elif (choice == 3):
              print("You selected: %s" %choice)
              issue = input ("What issue would you like to report? ")
              print ("Thank you for contacting us")
            elif (choice == 4):
              print("You selected: %s" %choice)
              print("Goodbye")
              update = False
            else:
              print ("Invalid input")
 
      else:
          print("Password inccorect. Please try again")
          condition = True
  else:
      print("Name not found. Please try again.")
      condition = True
