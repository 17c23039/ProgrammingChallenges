from time import sleep   #Please note this is only a prototype and will be improved and perfected over time.

def sg () :
  print("Hi! I am ShoppingGuru and I will create a shopping list for you. If you would like to add anything after, please just say Y to the question.")
  sl = str(input("What do you want to add to your shopping list? ")) #Asks for shopping list.
  print("Thanks. Adding..")
  slanswer = input("Would you like to add any more item(s) to your shopping list? Y/N/END. Please write the answer as we did. Y or N or END. ") #Asks if you would like to add more items.
  if slanswer == "N" :
    print("Okay, your shopping list consists of these items so far:")
    print(sl) #Gives the original shopping list.
  elif slanswer == "Y" :
    sladd1 = str(input("Okay, please make sure you write everything down so we can give you your shopping list. "))
    print("Thanks, adding and printing your shopping list..")
    sleep(2.5)
    print("Okay, your shopping list consists of " + sl + ", " + sladd1 + ". Thanks for using ShoppingGuru.") #Adds the extras to the shopping list
    sleep(3)
    print("Thanks! Use our service again soon!")    
  elif slanswer == "END" :
    print("Okay, shutting off...")
  else :
    print("That is an invalid option! Re-running the code...")
    sleep(3)
    sg ()

sg ()