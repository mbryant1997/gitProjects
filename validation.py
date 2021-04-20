def accountNumValidate (accountNumber): 
  #check if accountNumber is not empty
  #if accountNumber is 10 digits
  #if accountNumber is an integer
  if (accountNumber):
    try:
      int(accountNumber)
      if (len(str(accountNumber)) ==10):
        return True
    except ValueError: 
      #print("Invalid account number, account number should be integer")
      return False
    except TypeError:
      #print("Invalid account type")
      return False
  
    return False 