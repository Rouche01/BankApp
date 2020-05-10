import string
import random

home_menu = ["Staff Login", "Close App"]
login_menu = ["Create new bank account", "Check Account Details", "Logout"]


def show_menu(menu):
    option_num = 1
    for i in menu:
        print(f'Press {option_num} for {i}')
        option_num = option_num + 1
    menu_input = input('Choose an option: ')
    return menu_input


def login(username, password):
    f = open("staff.txt", "r")
    for x in f:
        loop_line = x
        user_data = loop_line.split("|")
        if username == user_data[0] and password == user_data[1]:
            f = open("session.txt", "w")
            f.write(f'''
username: {user_data[0]}
password: {user_data[1]}
email: {user_data[2]}
name: {user_data[3]}
            ''')
            return True
    return False


def create_account():
    account_number = ''
    account_name = input('Enter account name: ')
    opening_balance = input('Enter opening balance: ')
    account_type = input('Enter account type: ')
    account_email = input('Enter account email: ')
    global_digits = string.digits
    for i in range(10):
        account_number += random.choice(global_digits)
    f = open("customer.txt", "a")
    f.write(f'{account_number}|{account_name}|{opening_balance}|{account_type}|{account_email}|\n')
    f.close()
    print(f'This is your account number: {account_number}')


def check_account_details():
    check_account_number = input('Enter account number: ')
    f = open("customer.txt", "r")
    for x in f:
        loop_line = x
        customer_data = loop_line.split("|")
        if check_account_number == customer_data[0]:
            print(f'''
Account Number: {customer_data[0]}
Account Name: {customer_data[1]}
Opening Balance: {customer_data[2]}
Account Type: {customer_data[3]}
Account Email: {customer_data[4]}
            ''')


def app_run():
    home_choice = int(show_menu(home_menu))
    if home_choice == 1:
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        login_status = login(username, password)
        while not login_status:
            print('You have entered wrong user credentials, please try again')
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            login_status = login(username, password)
        if login_status:
            login_menu_choice = int(show_menu(login_menu))
            while login_menu_choice == 1:
                create_account()
                login_menu_choice = int(show_menu(login_menu))
            if login_menu_choice == 2:
                check_account_details();


app_run()
