
def welcome_statement():
    format_print()
    print('''
    Welcome Customer!''')

def format_print():
    print('-'*50)

def action_statement():
    while True:
        try:
            prompt = int(input('''
    Would you like to:
    1) View current balance
    2) Make a withdrawal (debit)
    3) Make a deposit (credit)
    4) Exit
    
    Option: '''))
            format_print()
            # make any other choice invalid and then promt the user
            # for another action.
            break
        except ValueError:
            print('''
    Not a valid selection\n
    Please choose 1, 2, 3, or 4
            ''')
            format_print()
        action_statement()
    if prompt == 1:
        current_balance()
    elif prompt == 2:
        make_withdrawal()
    elif prompt == 3:
        make_deposit()
    elif prompt == 4:
        exit_program()
    else:
        print('''
    Not a valid selection\n
    Please choose 1, 2, 3, or 4
            ''')
        format_print()
        action_statement()

def make_deposit():
    #asks the user how much they would like to deposit
    while True:
        try:    
            deposit_amount = float(input('''
    How much would you like to deposit?\n
    $'''))
            break
        except ValueError:
            print('''
    Not a valid selection please use integers
            ''')
            format_print()
            make_deposit()

    with open("transaction_hitory.txt", "a") as th:
        th.write("\n{:0.2f}".format(deposit_amount))

    print('''
    You deposited ${:0.2f}'''.format(deposit_amount))

    continue_statement()

def make_withdrawal():
    #asks the user how much they would like to withdrawal    
    while True:
        try: 
            withdrawal_amount = float(input('''
    How much would you like to withdraw?\n
    $'''))
            break
        except ValueError:
            print('''
    Not a valid selection please use integers
            ''')
            format_print()
            make_withdrawal()

    with open("transaction_hitory.txt", "a") as th:
        th.write("\n{:0.2f}".format(withdrawal_amount* -1)) 

    print('''
    You withdrew ${:0.2f}'''.format(withdrawal_amount))

    continue_statement()

def current_balance():
    #displays the current balance of the account

    transaction_history = open("transaction_hitory.txt", 'r')  # location of the text file
    lines = transaction_history.readlines()  # i am reading lines here
    counter = 0  # counter update each time number is entered
    for line in lines:  # taking each line
        conv_float = float(line)  # converting string to float
        counter = counter + conv_float  # update counter
    print('''
    Your current balance is ${:0.2f}'''.format(counter))

    continue_statement()

def continue_statement():
    continue_program = input('''
    Would you like to continue? (Y/N)
    
    Decision: ''')
    format_print()
    if continue_program.lower() == 'y' or continue_program.lower() == 'yes':
        action_statement()
    elif continue_program.lower() == 'n' or continue_program.lower() == 'no':
        exit_program()
    else:
        print('''
    That is not a valid entry please choose (Y/N)''')
        format_print()
        continue_statement()

def exit_program():
    #exits out of the application
    print('''
    Thanks for your business, have a great day!
    ''')
    exit()

welcome_statement()
action_statement()
# transaction_history.txt needs to take in all the deposits and withdrawals and return 
# the new balance on the following line in the txt. the newest balance that is listed in 
# the transaction history will be the value that is taken as the current_balance()