print("Welcome to ATM-Machine")
import time
user_pin = "2025"
pin_guess = ""
menu = ("1. Check Balance", "2. Withdraw Money", "3. Deposit Money", "4. Change Pin", "5. Exit")
options = ""
user_balance = 150000
yes = True
no = False

while pin_guess != user_pin:
    pin_guess = input("Enter your pin: ")

    if pin_guess != user_pin:
       print("Incorrect Pin")

    elif pin_guess == user_pin:
       print("Login successfully")
       print(menu[0])
       print(menu[1])
       print(menu[2])
       print(menu[3])
       print(menu[4])
       options = int(input("Select an option "))


if options == 1:
    print("Your new balance is " + "$" + "150" + "," + "000")
    print("new_transaction")

elif options == 2:
    amount_to_withdraw = int(input("Enter an amount to withdraw "))
    print("Processing...")
    time.sleep(2)
    print("Withdraw successful" "\n" + "Please take your cash.")
    print("Your new balance is " + "$" + str(user_balance - amount_to_withdraw))

new_transaction = input("Would you like another transaction? ")

if  no == new_transaction:
   print("Thank you for your cooperation")


elif yes == new_transaction:
    print(menu[0])
    print(menu[1])
    print(menu[2])
    print(menu[3])
    print(menu[4])
    options = int(input("Select an option "))


if options == 5:
    print("Thank you for using ATM-Machine" + "\n" + "Goodbye!")