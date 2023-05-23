import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def fethUserInfor():
    with open('DataBase/UserInfor.txt', "r") as f:    
        lines = f.readlines()
        return lines


def addNewAccount(newAccount=''):
        
    with open("DataBase/UserInfor.txt","a") as f:
        f.write(newAccount) 


def isEmail(email='mphelagtm@gmail.com'):
    
    if(re.fullmatch(regex, email)):
        return True
    return False


def userExist(email="mphela@gmail.com"):
    users = fethUserInfor()
    for user in users:
        if email in user:
            return True
    return False


def getUser(users, email):
    for i, user in enumerate(users):
        if email in user:
            return user.strip().split(','), i
    return None


def logged_in_user(email):
    users = fethUserInfor()
    for user in users:
        if email in user:
            return user.strip().split(',')
    return None


def getUserBeingPaid(account_no):
    users = fethUserInfor()
    for i, user in enumerate(users):
        if account_no in user:
            return user.strip().split(','), i
    return None


def update(email="mphela@gmail.com"):
    users = fethUserInfor()
    user, index = getUser(users, email)
    print()
    return user, index, users


def user_details(email):
    users = fethUserInfor()
    user, index = getUser(users, email)
    return user

def updateUserInfor(users):
    users = "".join(users)
    with open('DataBase/UserInfor.txt', "w") as f:    
        f.write(users)


def addTransaction(transaction):
    with open('DataBase\Transactions.txt', "a") as f:    
        f.write(transaction)


def getTransactions():
    with open("DataBase/Transactions.txt", "r") as f:
        list = f.readlines()
        return list


if __name__ == '__main__':
    print(update())