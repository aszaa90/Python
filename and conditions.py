#Multiple conditions
#and condition
Username = input( "Please enter your username")
Password =  input("Please enter your password")

if Username != "Tony" and Password != "lol1234":
    print("Access denied")
else:
    print("Welcome on board")

#or condition

your_age = input("How old are you?")
friends_age = input("How old is your friend?")

if int(your_age) >= 18 or int(friends_age) >= 18:
    print("You or your friend can vote")
else:
    print("Sorry, you or your friend can't vote")
#Sprawdzanie wartości z listy

registered_usernames = ['Tony', 'Mark', 'Sonia']
username = input("Please enter the username you would like to have.")

if username in registered_usernames:
    print("Sorry, this one is already taken")
else:
    print("Congrats, you can use that username")

#Sprawdzanie czy coś jest na liście

admin = ["Asia", "Ania", "Gosia"]
your_username= input("Please enter your username")

if your_username not in admin:
    print("Sorry, you don't have access")
else:
    print("You have access to enter this page")

#Conditioning z więcej niż jednym warunkiem

balance = input("What is your bank balance?")

if int(balance) <= 50:
    print("You don't get any intrests")
elif int(balance) <100:
    print("You get 1%")
else:
    print("You will get 2%")

    
