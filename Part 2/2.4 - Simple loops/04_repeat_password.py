# Write your solution here

password = input("Password:")
password2 = ""
    
while password != password2:
    password2 = input("Repeat password") 
    if password2 != password:
            print("They do not match!")
    elif password2 == password:
            print("User account created!")
            break
