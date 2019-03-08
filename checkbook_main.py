
def welcome_statement():
    print('Welcome Customer!')

def action_statement():
    prompt = int(input('''
    Would you like to:
    1) View current balance
    2) Make a withdrawal (debit)
    3) Make a deposit (credit)
    4) Exit
    '''))
    # make any other choice invalid and then promt the user
    # for another action.
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
        action_statement()

def make_deposit():
    #asks the user how much they would like to deposit
    deposit_amount = float(input('''
    How much would you like to deposit?\n
    $'''))

    with open("transaction_hitory.txt", "a") as th:
        th.write("\n{}".format(deposit_amount))

    print('''
    You deposited ${}'''.format(deposit_amount))

def make_withdrawal():
    #asks the user how much they would like to withdrawal    
    withdrawal_amount = float(input('''
    How much would you like to withdraw?\n
    $'''))

    with open("transaction_hitory.txt", "a") as th:
        th.write("\n{}".format(withdrawal_amount* -1)) 

    print('''
    You withdrew ${}'''.format(withdrawal_amount))

def current_balance():
    #displays the current balance of the account
    print('''
    Your current balance is {}
    '''.format(a_file_will_go_here.txt))

def exit_program():
    #exits out of the application
    print('''
    Thanks for your business, have a great day!
    ''')

# transaction_history.txt needs to take in all the deposits and withdrawals and return 
# the new balance on the following line in the txt. the newest balance that is listed in 
# the transaction history will be the value that is taken as the current_balance()