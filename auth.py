#register
# username, password, email
#  generate account number


#Login
# (username or email)) and password
 
# bank operations

#Initializing the system
import random
database = {}

def init():

    print('Welcome to Apex Bank')
 
    haveaccount = int(input('Do you have account with us: 1 (yes) 2 (No) \n'))
        
    if(haveaccount == 1):
        login()

    elif(haveaccount == 2):
        register()

    else:
        print("You have selected an Invalid option")
        init()


def login():


    print('########## Login ##########')

    userAccountNumber = int(input("Enter your account number? \n"))
    password = input("Enter your password? \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == userAccountNumber):
            if(userDetails[3] == password):
                bankoperation(userDetails)
    
    print("Invalid account or password")
    login()

def register():

    print("********* Register *********")

    email = input("Enter your email address? \n")
    first_name = input("Enter your first name? \n")
    last_name = input("Enter your last name? \n")
    password = input("Create a strong password \n")

    accountNumber = generateaccountnumber()

    database[accountNumber] = [ first_name, last_name, email, password ]
    
    print("Your account has been created")
    print("= ==== ========== ==== =")
    print("Your account number is: %d" % accountNumber)
    print("Please keep it safe")
    print("= ==== ========== ==== =")

    login()

def bankoperation(user):

    print("Welcome %s %s " % ( user[0], user[1]))
    selectedOption = int(input("What would you like to do? (1) Deposit (2) Withdraw (3) Transfer (4) Logout (5) Exit \n"))

    if (selectedOption == 1):
            depositOperation()

    elif(selectedOption == 2):
            withdrawalOperation()

    elif(selectedOption == 3):
        transferOperations()

    elif(selectedOption == 4):
            logout()

    elif(selectedOption == 5):
            exit()

    else:
            print("Invalid option selected!")
            bankoperation(user)


def withdrawalOperation():
    print("Withdrawal")

def depositOperation():
    print("Deposit Operations")

def transferOperations():
    print("Transfer Operations")

def generateaccountnumber():

    return random.randrange(1111111111,9999999999)

def logout():
    login()


####### Actual Banking System ########
#print(generateaccountnumber())

init()