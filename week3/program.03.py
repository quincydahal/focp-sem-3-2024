#1
greeting = input("Hello! What is you name: ")

if greeting == "":
    print("Hello, Stranger!")

else:
    print(f"Hello! {greeting}. How are you?")


#2
new_password = input("Enter a new password: ")
confirm_password = input("Confirm your password: ")

if new_password == confirm_password:
    print("Password Set")

else:
    print("Error Password do not match")


#3
new_password = input("Enter a new password: ")
confirm_password = input("Confirm your password: ")

if new_password == confirm_password and 8 < len(new_password) <= 12:
    print("Password Set")

elif len(new_password) < 8 or len(new_password) >= 12:
    print("Please use 8 to 12 characters for Password.")

elif new_password != confirm_password:
    print("Error Password do not match")


#4
new_password = input("Enter a new password: ")
confirm_password = input("Confirm your password: ")

if new_password == 'password' or 'letme' or 'same' or 'world' or 'Rihana':
        print("This is a weak Password")

elif new_password == confirm_password and 8 < len(new_password) <= 12:
    print("Password is Set")

elif len(new_password) <= 8 or len(new_password) >= 12:
    print("Please use 8 to 12 characters for Password.")

elif new_password != confirm_password:
    print("Error Password do not match")


#5
a = 1
while a == 1:
    new_password = input("Enter a new password: ")
    confirm_password = input("Confirm your password: ")

    if new_password == 'password' or 'letme' or 'same' or 'world' or 'Rihana':
            print("This is a weak Password")

    if new_password == confirm_password and 8 < len(new_password) <= 12:
        print("Password is Set")
        break

    if len(new_password) <= 8 or len(new_password) >= 12:
        print("Please use 8 to 12 characters for Password.")

    if new_password != confirm_password:
        print("Error Password do not match")

    confirmation = input("Do you want to redo it (Y/N): ")
    confirmation.upper()

    if confirmation == "Y":
         continue
    else:
         print("Thank You for your time!")
         break


#6
for i in range (0,13):
    multiplication = 7 * i
    print(f"7 x {i} = {multiplication} ")


#7
number = int(input("Enter a number: "))
for i in range (0,13):
    multiplication = number * i
    print(f"{number} x {i} = {multiplication} ")


#8
number = int(input("Enter a number: "))

if number > 0:
    for i in range (0,13):
        multiplication = number * i
        print(f"{number} x {i} = {multiplication} ")

elif number < 0:
    for i in range (13, 0, -1):
        multiplication = number * i
        print(f"{number} x {i} = {multiplication} ")
    