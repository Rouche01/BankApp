import string
import random
import os

home_menu = ["Staff Login", "Close App"]
login_menu = ["Create new bank account", "Check Account Details", "Logout"]


def show_menu(menu):
    option_num = 1
    for i in menu:
        print(f'Press {option_num} for {i}')
        option_num = option_num + 1
    menu_input = input('Choose an option: ')
    while not menu_input.isnumeric() or int(menu_input) > len(menu) or int(menu_input) == 0:
        menu_input = input('You are entering in a wrong value, try again with the options available: ')
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
            f.flush()
            os.fsync(f.fileno())
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


def home_menu_exec(menu_choice):
    if menu_choice == 1:
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        return {
            "username": username,
            "password": password
        }
    elif menu_choice == 2:
        print('App ending')


def login_menu_exec(menu_choice):
    login_menu_choice = ''
    if menu_choice == 1:
        create_account()
        login_menu_choice = int(show_menu(login_menu))
    elif menu_choice == 2:
        check_account_details()
        login_menu_choice = int(show_menu(login_menu))
    while menu_choice == 3:
        os.remove("session.txt")
        app_run()
    if menu_choice != 3:
        login_menu_exec(login_menu_choice)


def app_run():
    home_choice = int(show_menu(home_menu))
    if home_choice == 1:
        current_user = home_menu_exec(home_choice)
        login_status = login(current_user['username'], current_user['password'])
        while not login_status:
            print('You have entered wrong user credentials, please try again')
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            login_status = login(username, password)
        if login_status:
            login_menu_choice = int(show_menu(login_menu))
            login_menu_exec(login_menu_choice)
    elif home_choice == 2:
        quit()


app_run()
