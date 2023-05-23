import math

def simple(deposit, interest_rate, years):
    return deposit*(1+(interest_rate/100) * years)


def compound(deposit, interest_rate, years):
    return deposit * math.pow((1 + interest_rate/100), years)


def user_input(query):
    while True:
        amount = input(query)

        if(not isNumber(amount)):
            print("Please provide the numeric input.")
            continue
        return amount
    

def isNumber(string=""):
    count = 0
    for index, char in enumerate(string):
        if (char.isdigit()):
            continue

        if(char == "." and count == 0):
            count += 1
            continue
    
        return False

    return True
        

def user_query(query):
    amount = user_input(query)
    interest_rate = user_input('Please enter the interest rate: ( e.g 8 or 8.8) ')
    years = user_input('How many years would you like to invest: (e.g 20) ')
    return float(amount), float(interest_rate), int(years)


def investment():
    amount, interest_rate, years = user_query('How much would you like to deposit: ')
    while True:        
        interest = input("Would you like \"simple\" or \"compound\" interest? ").lower()
        if(interest == 'simple'):
            future_value = simple(amount, interest_rate, years)
            print(f"\nYour simple interest investment after {years} years will be R{future_value:.2f}")
            break

        if(interest == 'compound'):
            future_value = compound(amount, interest_rate, years)
            print(f"\nYour compound interest investment after {years} years will be R{future_value:.2f}.")
            break


def monthly_bond_repayment_formula(present_value, interest_rate, years):
    return ((interest_rate/100)*present_value)/(1 - math.pow(1+interest_rate/100, -years*12 ))


def bond():
    present_value, interest_rate, years = user_query("Enter present value: ")
    print(f"Your monthly bond repayment will be: R{monthly_bond_repayment_formula(present_value, interest_rate, years):.2f}\n")
    

def main():
    while True:
        print('Choose either \'investment\' or \'bond\' from the menu below to proceed:\n'
            '\n'
            'investment   - to calculate the amount of interest you\'ll earn on interest\n'
            'bond         - to calculate the amount you\'ll have to pay on a home loan')

        choice = input('Enter here (investment or bond): ').lower()
        if(choice == 'exit'):
            break

        if(choice == "investment"):
            investment()
            print("==========================================================================>\n\n")
            continue

        if(choice == "bond"):
            bond()
            print("==========================================================================>\n\n")
            continue

        print("  Please enter bond or invesment.\n")


if __name__ == '__main__':
    main()
    # number ="0000"

    # if(number.isdigit()):
    #     print("is digit")

    # if(number.isnumeric()):
    #     print('is numeric')
    
    # if(isDecimal(number)):
    #     print("is decimal")
    #     number = float(number)
    #     print(type(number))