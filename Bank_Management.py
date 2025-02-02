MAX_ACCOUNTS = 50

def create_account():
    print("Creating an Account.🏦😀")
def balance_checking():
    print("Checking Balance.💰🙄")
def deposit():
    print("Deposit Money.💰😄")
def withdraw():
    print("Withdraw Money.🤑")
def delete_account():
    print("Deleting an account.😒🏦")
def exit_program():
    print("Thanks for using ABC Bank Management System, Bye👋.")


def display():
    print("1- Create Account")
    print("2- Balance Inquery")
    print("3- Deposit")
    print("4- Withdraw")
    print("5- Delete Account")
    print("6- Exit")

    choice = int(input("Enter choice : "))
    
    if(choice == 1):
        create_account()
    elif(choice == 2):
        balance_checking()
    elif(choice == 3):
        deposit()
    elif(choice == 4):
        withdraw()
    elif(choice == 5):
        delete_account()
    elif(choice == 6):
        exit_program()
        return 6
        return
    else:
        print("Invalid choice!")
    return choice
choice = 0
while(choice != 6):
    choice = display()
