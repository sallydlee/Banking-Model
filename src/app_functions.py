from helpers import *
from BankModel import *
from connection import *


def login_menu():
    print("""
    ==== $$ Bank $$ ====
    1. Returning Client
    2. New Client
    3. Exit
    """)


def returning_client_menu():
    print("""
    ==== $$ Bank $$ ====
    1. Access Bank Account
    2. Open New Bank Account
    3. Exit
    """)


def bank_account_menu():
    print("""
    ==== $$ Bank $$ ====
    1. Check Balance
    2. Make a Deposit
    3. Make a Withdrawal
    4. Exit
    """)


def login_attempt():
    """
    Asks for email, password input and calls verify_user()

    Returns
    -------
    Dictionary of row in ClientTable matching email, password.
    """
    email = input("Email (this will be your login): ").lower()

    if check_user(email):
        password = input("Password: ")
        user = verify_user(email, password)
        return user
    else:
        print("User does not exist!")


def new_client():
    """
    Asks for user input for user details and returns Client object.

    Returns
    -------
    Client object
    """
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email (this will be your login): ").lower()
    if check_user(email):
        pass
    else:
        print("User already exists!")

    password = input("Password: ")
    street = input("Street Address: ")
    city = input("City: ")
    state = input("State: ")
    postal = input("Postal: ")
    country = input("Country: ")
    pin = input("Create 4 Digit Pin: ")

    client_row = ClientTable(first_name=first_name, last_name=last_name, email=email, password=password, street=street,
                             city=city, state=state, postal=postal, country=country, pin=pin)
    session.add(client_row)
    session.commit()
    return Client(first_name, last_name, email, password, street, city, state, postal, country, pin)


def create_account(record):
    """
    Returns SavingsAccount or BankAccount object depending on user input.

    Parameters
    ----------
    record : dict
        Dictionary of ClientTable row generated when creating new account.

    Returns
    -------
    BankAccount or SavingsAccount object

    """
    account_type = input("Select account type (Checking/Savings): ").title()
    account_number = random_number(9)
    initial_deposit = read_int("Submit initial deposit: ",
                               "Pass 0 if you do not want to make an initial deposit.")
    client_id = record['id']

    if account_type == 'Savings':
        account_row = AccountTable(account_number=account_number, balance=initial_deposit, client_id=client_id,
                                   account_type=account_type, monthly_withdrawal_number=0)
        session.add(account_row)
        session.commit()
        print(f"{account_type} account created. Account Number: {account_number}")
        return SavingsAccount(account_number, initial_deposit)

    elif account_type == 'Checking':
        account_row = AccountTable(account_number=account_number, balance=initial_deposit, client_id=client_id,
                                   account_type=account_type, monthly_withdrawal_number=None)
        session.add(account_row)
        session.commit()
        print(f"{account_type} account created. Account Number: {account_number}")
        return BankAccount(account_number, initial_deposit)

    else:
        print("Invalid Account Type.")


def clear_withdrawal_number():
    """Resets Monthly Withdrawal Column to 0 on AccountsTable if today is the first of the month.
    """
    day = datetime.today().strftime('%d')
    if day == '01':
        session.query(AccountTable).update({"monthly_withdrawal_number": 0})
        session.commit()


def verify_account(account_number, pin):
    """
    Returns dictionary of row in AccountTable if account number and pin match is found.

    Parameters
    ----------
    account_number : str
        9 digit random string generated when account was created.
    pin : str
        4 digit string generated from user input when user was created.

    Returns
    -------
    Dictionary
    """
    record = session.query(AccountTable).join(ClientTable).filter(AccountTable.account_number == account_number,
                                                                  ClientTable.pin == pin).first()
    try:
        return record.__dict__
    except AttributeError:
        print("Account does not exist.")


def update_account(bank_class):
    """
    Updates balance and monthly withdrawal number in row matching account number in AccountTable.

    Parameters
    ----------
    bank_class : BankAccount class, SavingsAccount class
    """
    account_number = bank_class.get_account_number()
    balance = bank_class.get_balance()
    try:
        withdrawal_number = bank_class.get_withdrawal_number()
    except AttributeError:
        withdrawal_number = None

    session.query(AccountTable).filter(AccountTable.account_number == account_number).update({
        "balance": balance,
        "monthly_withdrawal_number": withdrawal_number
    })
    session.commit()


def create_account_class(record):
    """
    Creates BankAccount or SavingsAccount object depending on account type.

    Parameters
    ----------
    record : dictionary
        Dictionary generated from row in AccountTable.

    Returns
    -------
    SavingsAccount or BankAccount object.
    """
    if record['account_type'] == 'Savings':
        return SavingsAccount(record['account_number'], record['balance'], record['monthly_withdrawal_number'])
    elif record['account_type'] == 'Checking':
        return BankAccount(record['account_number'], record['balance'])


def check_user(search_value):
    """
    Returns boolean indicating whether or not the user exists in the ClientTable given the search value.

    Parameters
    ----------
    search_value : str
        User's email.

    Returns
    -------
    Boolean
    """
    return bool(session.query(ClientTable).filter(ClientTable.email == search_value))


def verify_user(email, password):
    """
    Returns dictionary of row in ClientTable if the email, password filter finds a user.

    Parameters
    ----------
    email : str
    password : str

    Returns
    -------
    Dictionary
    """
    record = session.query(ClientTable).filter(ClientTable.email == email, ClientTable.password == password).first()
    try:
        return record.__dict__
    except AttributeError:
        print("Incorrect Username/Password.")