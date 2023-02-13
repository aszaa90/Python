your_bank_balance = input("Enter your bank balance")

if int(your_bank_balance) <50:
    print("You won't get any interests")
elif int(your_bank_balance) <100:
    print ("You will get 1% interests")
elif int(your_bank_balance) <150:
    print("You will get 2% interests")
else:
    print("You will get 4%")
          
    
    
