from helpers import *


class Employee:
    """
    A class to represent an employee.

    Attributes
    ----------
    first_name : str
        first name of employee
    last_name : str
        family name of employee
    start_date : str
        starting date of employee
    title : str
        position title of employee
    end_date : date
        termination date of employee
    active : bool
        employment status of employee

    Methods
    -------
    change_title(title):
        Changes position title of employee.
    deactivate_user():
        Changes active status of employee to false.
    """

    def __init__(self, first_name, last_name, start_date, title, end_date=None, active=True):
        """
        Constructs all necessary attributes for the employee object.

        Parameters
        ----------
        first_name : str
            first name of employee
        last_name : str
            family name of employee
        start_date : date
            starting date of employee
        title : str
            position title of employee
        end_date : date
            termination date of employee
        active : bool
            employment status of employee
        """
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.start_date = start_date
        self.end_date = end_date
        self.title = title
        self.active = active

    def change_title(self, title):
        """
        Changes employee's title.

        Parameters
        ----------
        title : str
            Desired employee title

        Returns
        -------
        None
        """
        self.title = title

    def deactivate_user(self):
        """
        Changes active parameter to false for employee.

        Returns
        -------
        None
        """
        if self.active:
            self.active = False
        else:
            print(f"Employee {self.first_name} {self.last_name} is already inactive.")


class BankAccount:
    """
    A class to represent a bank account.

    Attributes
    ----------
    account_number : str
        Unique string of numbers that identifies the owner of the account
    balance : int
        Amount of money held in a bank account at a given moment

    Methods
    -------
    get_account_number():
        Prints the account number.
    get_balance():
        Prints the current balance.
    deposit(amount):
        Adds amount to current balance.
    withdrawal(amount):
        Subtracts amount to current balance.
    """

    def __init__(self, account_number, balance):
        """
        Constructs all necessary attributes for the BankAccount object.

        Parameters
        ----------
        account_number : str
            Unique string of numbers that identifies the owner of the account
        balance : int
            Amount of money held in a bank account at a given moment
        """
        self.account_number = account_number
        self.balance = check_int(balance)

    def get_account_number(self):
        """
        Prints and returns the account number.

        Returns
        -------
        account_number : str
            Unique string of numbers that identifies the owner of the account
        """
        print(f"Account number: {self.account_number}")
        return self.account_number

    def get_balance(self):
        """
        Prints and returns current balance.

        Returns
        -------
        balance : int
            Integer depicting current amount in bank account.

        """
        print(f"Current balance is ${self.balance}")
        return self.balance

    def deposit(self, amount):
        """
        Adds integer amount to current balance.

        Parameters
        ----------
        amount : int
            Integer to add to current balance

        Returns
        -------
        None
        """
        amount_check = check_int(amount)
        if amount_check:
            self.balance = self.balance + amount
            self.get_balance()

    def withdrawal(self, amount):
        """
        Subtracts integer amount from current balance.

        Parameters
        ----------
        amount : int
            Integer to subtract to current balance

        Returns
        -------
        None
        """

        amount_check = check_int(amount)
        if amount_check:
            if amount > self.balance:
                print('Insufficient Funds')
            else:
                self.balance = self.balance - amount
                self.get_balance()


class SavingsAccount(BankAccount):
    """
    BankAccount(account_number, balance)

    A class to represent a savings account.

    Attributes
    ----------
    account_number : str
        Unique string of numbers that identifies the owner of the account
    balance : int
        Amount of money held in a bank account at a given moment
    monthly_withdrawal_number : int
        Number of withdrawals that occurred in the current month

    Methods
    -------
    get_withdrawal_number():
        Prints and returns the number of withdrawals for the current month.
    withdrawal(amount):
        Subtracts amount to current balance.
    increase_withdrawal_number():
        Increases the monthly_withdrawal number by 1.
    """

    def __init__(self, account_number, balance, monthly_withdrawal_number=0):
        """
        Constructs all necessary attributes for the SavingsAccount object.

        Parameters
        ----------
        account_number : str
            Unique string of numbers that identifies the owner of the account
        balance : int
            Amount of money held in a bank account at a given moment
        monthly_withdrawal_number : int
            Number of withdrawals that occurred in the current month
        """
        BankAccount.__init__(self, account_number, balance)
        self._monthly_withdrawal_number = monthly_withdrawal_number

    def get_withdrawal_number(self):
        """
        Prints and returns the number of withdrawals for the current month.

        Returns
        -------
        monthly_withdrawal_number : int
            Number of withdrawals that occurred in the current month
        """
        print(f"Withdrawals this month: {self._monthly_withdrawal_number}")
        return self._monthly_withdrawal_number

    def withdrawal(self, amount):
        """
        Subtracts amount to current balance.

        Parameters
        ----------
        amount : int
            Integer to subtract to current balance

        Returns
        -------
        None
        """

        amount_check = check_int(amount)
        if amount_check:
            if self._monthly_withdrawal_number >= 6:
                print('Maximum monthly withdrawals reached.')
            elif amount > self.balance:
                print('Insufficient Funds')
            else:
                self.balance = self.balance - amount
                self.get_balance()
                self.increase_withdrawal_number()

    def increase_withdrawal_number(self):
        """
        Increases the monthly_withdrawal number by 1.

        Returns
        -------
        None
        """
        self._monthly_withdrawal_number += 1


class Client:
    """
    A class to represent a client.

    Attributes
    ----------
    first_name : str
        first name of client
    last_name : str
        family name of client
    email : str
        email of client
    password : str
        password of client
    street : str
        primary street address of client
    city : str
        primary city of client
    state : str
        primary state of client
    postal : str
        postal code of client
    country : str
        country of client
    pin : str
        four digit string client chooses to access accounts

    Methods
    -------
    get_first_name():
        Returns first name of client
    get_last_name():
        Returns family name of client
    get_email():
        Returns email of client
    get_password():
        Returns password of client
    get_street():
        Returns primary street address of client
    get_city():
        Returns primary city of client
    get_state():
        Returns primary state of client
    get_postal():
        Returns postal code of client
    get_country():
        Returns country of client
    get_pin():
        Returns four digit string client chooses to access accounts
    set_pin(pin):
        Sets four digit string client chooses to access accounts
    """

    def __init__(self, first_name, last_name, email, password, street, city, state, postal, country, pin):
        """
        Constructs all necessary attributes for the Client object.

        Parameters
        ----------
        first_name : str
            first name of client
        last_name : str
            family name of client
        email : str
            email of client
        password : str
            password of client
        street : str
            primary street address of client
        city : str
            primary city of client
        state : str
            primary state of client
        postal : str
            postal code of client
        country : str
            country of client
        pin : str
            four digit string client chooses to access accounts
        """

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email.lower()
        self.password = password
        self.street = street.title()
        self.city = city.title()
        self.state = state
        self.postal = postal
        self.country = country
        self.pin = pin

    def get_first_name(self):
        """
        Returns first name of client.

        Returns
        -------
        String
        """
        return self.first_name

    def get_last_name(self):
        """
        Returns last name of client.

        Returns
        -------
        String
        """
        return self.last_name

    def get_street(self):
        """
        Returns street address of client.

        Returns
        -------
        String
        """
        return self.street

    def get_city(self):
        """
        Returns city of client.

        Returns
        -------
        String
        """
        return self.city

    def get_state(self):
        """
        Returns state of client.

        Returns
        -------
        String
        """
        return self.state

    def get_postal(self):
        """
        Returns postal code of client.

        Returns
        -------
        String
        """
        return self.postal

    def get_country(self):
        """
        Returns country of client.

        Returns
        -------
        String
        """
        return self.country

    def get_pin(self):
        """
        Returns 4 digit code of client.

        Returns
        -------
        String
        """
        return self.pin

    def set_pin(self, pin):
        """
        Sets 4 digit code for client to use to access accounts.

        Parameters
        ----------
        pin : str

        Returns
        -------
        None
        """
        self.pin = pin

