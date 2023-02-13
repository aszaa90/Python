admin_usernames = ["Tony", "Adam", "Mark"]

your_username = input("Please enter your username")

if your_username not in admin_usernames:
    print("access denied")
else:
    print("Access granted")
    
