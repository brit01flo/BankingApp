from Register.Register import Register
import datetime
import random
import time
import stdiomask
from Common.Common import addNewAccount, user_details, userExist, isEmail, logged_in_user, update, updateUserInfor, getUserBeingPaid, addTransaction, getTransactions
import os
from finances.finance_calculators import main

def homePage():
    print('Welcome to The Big Five Bank\n')


def not_logged_in_message():
    print(
        'Choose the any of the following service by entering a number😊\n\n'
        '1. Create Account\n'
        '2. Login\n'
        '3. Financial Calculator\n'
        '4. Exit App\n'
    )


def generateRandomPassword():
    s = "!#$%&()*+-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_abcdefghijklmnopqrstuvwxyz{|}~"
    l = [i for i in s]
    generated_password = ""
    for i in range(13):
        index = random.randint( 0, len(l)-1)
        generated_password += l[index]
    return generated_password


def inputNames(query):
    name = input(query).split(" ")[0].lower()
    if(name == 'exit'):
            return name
    while not isBlank(name):
        name = input(query).split(" ")[0].lower()
        if(name == 'exit'):
            return name
    return name


def inputEmail(query):
    email = input(query).split(" ")[0].lower()
    if(email == 'exit' ):
            return email
    while not isBlank(email) or not isemail(email):
        email = input(query).split(" ")[0].lower()
        if(email == 'exit' ):
            return email
    return email


def inputPassword(query="Enter the password: ", _query='Enter your password again to confirm: '): 

    generated_password = ''
    q = input("Would you like to generate password: (y or n or exit)").lower()
    if(q == 'exit'):
        return q
    
    if(q == "y" or q =='yes'):
        generated_password = generateRandomPassword()
        time.sleep(2)
        print(f'Generated password: {generated_password}')
        time.sleep(3)
        yes = input("Enter \'y\' to use it or \'n\' to set yours: ")
        if(yes == 'y'):
            return generated_password
    
    password = input(query).split(" ")[0].lower()
    if(q == 'exit'):
        return q
    confirm_password = input(_query).split(" ")[0].lower()
    if(q == 'exit'):
        return q
    while not isBlank(password) or not isBlank(confirm_password) or not equal(password, confirm_password):
        password = input(query).split(" ")[0].lower()
        if(q == 'exit'):
            return q
        confirm_password = input(_query).split(" ")[0].lower()
        if(q == 'exit'):
            return q
    return password


def createAccount():

    print('You creating a new account...\n')
    name = inputNames("Enter your name: ").lower()
    if(name == 'exit'):
        return False
    surname = inputNames("Enter your surname: ").lower()
    if(surname == 'exit'):
        return False
    email = inputEmail("Enter your email: ").lower()
    if(email == 'exit'):
        return False
    password = inputPassword()
    if(password == 'exit'):
        return False

    print("Proccessing...\n")
    time.sleep(5)
    if(userExist_(email) == False):
        time.sleep(4)
        return False
    
    new_account = Register(name, surname, email, password)
    addNewAccount(new_account.__str__())
    
    print(
        '\n*********************************************'
        "\n  You successfully created a new account✅\n"
        '*********************************************\n')
    time.sleep(10)
    
    return True


def isBlank(name):
    if(name == ""):
        print(
            '\n*********************************************'
            "\n====>  Fill all the spaces 🤦🏾‍♂️\n\n"
            '*********************************************\n'
        )
        print("")
        return False
    return True


def isemail(email):
    if(not isEmail(email)):
        
        print(
            '\n*********************************************'
            "\n====>  Invalid email ❌\n\n"
            '*********************************************\n'
        )
        return False
    return True


def equal(password, confirm_password):
     if(password != confirm_password):
        print(
            '\n*********************************************'
            "\n====>  Password dont match 🙅🏾‍♂️\n\n"
            '*********************************************\n'
        )
        return False
     return True


def userExist_(email):
    
    if(userExist(email)):
        print(
            '\n*********************************************'
            "\n====>  Account with this email address exist.🙆🏾‍♂️\n\n"
            '*********************************************\n'
        )
        return False
    
    
    return True


def login():
    username = input("Enter username: ").strip().lower()
    password = stdiomask.getpass("Enter password: ").strip()
    print("verifying user input...")
    time.sleep(3)
    return verifyLogin(username, password), username


def incorrectCredentials():
    print('Incorrect username or password')


def verifyLogin(username, password):

    userDetails = logged_in_user(username)

    if(userDetails is None):
        incorrectCredentials()
        return False
    
    if(userDetails[3].strip() == username and userDetails[4].strip() == password):
        print('Successfully logged...')
        return True
    
    incorrectCredentials()
    return False


def balance (email):
    user = user_details(email)
    print(f'{user[1].capitalize()} your current balance is R{user[-1]}')


def commandHandler(command, logout, cred = ''):

    if command == "1":
        createAccount()

    elif command == "2":
        logout[1], cred = login()
        
        if(logout[1] == False):
            print()
            print("Incorrect credentials.")
            cred = ''
        else:
            print("Welcome to The Big Five Terminal Banking app")
        time.sleep(5)
    elif command == "3":
        main()

    elif command == '4': 
        logout[0] = False
        logout[1] = False

    return logout, cred


def withdraw(email):

    while True:
        withdrawedAmount = input("How much would you like to withdraw: ").strip()
        if(withdrawedAmount.isdigit() and withdrawedAmount.isnumeric()):
            user, index, users = update(email)
            if(int(user[5].strip()) < int(withdrawedAmount)):
                print('You have insufficient funds.')
            else:
                print('You successfully withdrawn -R' +  withdrawedAmount + "  ✅")
                newAmount = str(int(user[5].strip()) - int(withdrawedAmount))
                print("Your new amount is R" + newAmount)
                user[5] =  " " + newAmount + '\n'
                users[index] = ",".join(user)
                updateUserInfor(users)
                
                addTransaction(transaction(email, "Withdrew", withdrawedAmount))
                time.sleep(10)
                break
        else:
            print("Please enter numerics: ")  


def transaction(email, transaction_message, depositedAmount):
    current_date = datetime.datetime.now()
    return email + ", You "+ transaction_message + " R"+depositedAmount +"; "+ str(current_date) +'\n'
    

def deposit(email):
    while True:
        depositedAmount = input("How much would you like to deposit: ").strip()

        if(depositedAmount.isdigit() and depositedAmount.isnumeric()):
            user, index, users = update(email)
            newAmount = str(int(user[5].strip()) + int(depositedAmount))
            user[5] =  " " + newAmount + '\n'
            users[index] = ",".join(user)

            print('You successfully deposited +R' +  depositedAmount + "  ✅")
            print("Your new amount is R" + newAmount)

            updateUserInfor(users)
            addTransaction(transaction(email, "Deposited", depositedAmount))
            break
        else:
            print("Please enter numerics: ")


def pay_someone(email):
    while True:
        account_no = input("Enter the account no of the person you want to transfer money to: ")

        if(account_no == ""):
            print('Please provide the account no')
            continue

        user_being_paid, index_ = getUserBeingPaid(account_no)

        if(user_being_paid is None or user_being_paid[0].strip() != account_no):
            print(f"The account no {account_no} does not exist. Please provide the correct account no.")
            continue
        
        while True:
            amount_to_transfer = input("Enter the amount you would like to transfer: ")

            user, index, users = update(email)
            if(amount_to_transfer.isdigit() == False and amount_to_transfer.isnumeric() == False ):
                print("Please enter numerics: ")
                continue

            if((int(user[5].strip()) - int(amount_to_transfer) < 0)):
                print('You have insufficient funds.')
                return
            
            my_new_balance = int(user[5].strip()) - int(amount_to_transfer)
            user[5] =  " " + str(my_new_balance) + '\n'
            users[index] = ",".join(user)

            print(f"You have succefully transfered -R{amount_to_transfer} ✅ to the account {user_being_paid[0][:2]}*******{user_being_paid[0][9:]}")
            print(f"Your new balance is: R{my_new_balance}")

            their_new_balance = int(user_being_paid[5].strip()) + int(amount_to_transfer)
            user_being_paid[5] =  " " + str(their_new_balance) + '\n'
            users[index_] = ",".join(user_being_paid)

            updateUserInfor(users)
            break


def transactions(email):
    print("Transactions")
    for i, transaction in enumerate(getTransactions()):
        if(email in transaction):
            print(" ".join(transaction.strip().split(",")[1:]))


def logged_in_command_handler(command, cred, logout):
    if(command == '1'):
        deposit(cred[0])
        time.sleep(5)
    if(command == '2'):
        withdraw(cred[0])
        time.sleep(5)
    if(command == '3'):
        pay_someone(cred[0])
        time.sleep(5)
    if(command == "4"):
        balance(cred[0])
        time.sleep(5)
    if(command == '5'):
        transactions(cred[0])
        time.sleep(10)
    if(command == '6'):
        print("Logout")
        logout[1] = False
 

def logout():
    return False


def service_():
    print(
        '1• Deposit\n'
        '2• Withdraw\n'
        '3• Pay someone\n'
        '4• Balance\n'
        '5• Transactions\n'
        '6• Logout\n'
    )


def BankingAppMain():
    logged_in = [True, False]
    cred = ['']
    homePage()

    while logged_in[0]:
        not_logged_in_message()
        command = input("Enter command: ")
        logged_in, cred[0] = commandHandler(command, logged_in)
        # time.sleep(3)

        os.system('cls||clear')
       
        while logged_in[1]:
            service_()
            command = input("Choose any of the service above by entering a number: ")
            logged_in_command_handler(command, cred, logged_in)
            time.sleep(3)
            os.system('cls||clear')
        cred[0] = ''


if __name__ == '__main__':
    BankingAppMain()
