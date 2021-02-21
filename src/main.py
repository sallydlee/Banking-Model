from app_functions import *


def bank_demo():
    clear_withdrawal_number()
    while True:
        login_menu()

        selection = read_int("Select an option: ", "Please select an option 1-3.")

        if selection == 1:
            access = login_attempt()

            if access:
                print("Login successful!")
                returning_client_menu()
                selection_account = read_int("Select an option: ", "Please select an option 1-3.")

                if selection_account == 1:
                    account_number = input("Input account number: ")
                    pin = input("Input pin: ")
                    existing_account = verify_account(account_number, pin)

                    if existing_account:
                        bank_account_menu()
                        bank_account = create_account_class(existing_account)
                        selection_bank = read_int("Select an option: ", "Please select an option 1-4.")

                        while True:
                            if selection_bank == 1:
                                bank_account.get_balance()
                                selection_bank = read_int("Select an option: ", "Please select an option 1-4.")

                            elif selection_bank == 2:
                                deposit_amount = read_int("Insert deposit amount ($): ",
                                                          "Please insert a dollar amount.")
                                bank_account.deposit(deposit_amount)
                                selection_bank = read_int("Select an option: ", "Please select an option 1-4.")

                            elif selection_bank == 3:
                                withdraw_amount = read_int("Insert withdrawal amount ($): ",
                                                           "Please insert a dollar amount.")
                                bank_account.withdrawal(withdraw_amount)
                                selection_bank = read_int("Select an option: ", "Please select an option 1-4.")

                            elif selection_bank == 4:
                                update_account(bank_account)
                                break

                            else:
                                print("Please select an option 1-4.")

                    else:
                        break

                elif selection_account == 2:
                    create_account(access)

                elif selection_account == 3:
                    break

                else:
                    print("Please select an option 1-3.")

        elif selection == 2:
            new_client()

        elif selection == 3:
            break

        else:
            print('Please select an option 1-3.')


if __name__ == "__main__":
    bank_demo()





