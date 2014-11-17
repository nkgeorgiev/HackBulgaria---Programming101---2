import sql_manager
import send_email
import getpass
import random
import hashlib


def main_menu():
    print("Welcome to our bank service. You are not logged in. \nPlease register or login")

    while True:
        command = input("$$$>").split(" ")

        if command[0] == 'register':
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")
            while not sql_manager.is_strong(username, password):
                print("Password is not strong enough!")
                password = getpass.getpass("Enter your password: ")
            email = input("Enter your email: ")
            sql_manager.register(username, password, email)

            print("Registration Successfull")

        elif command[0] == 'login':
            username = input("Enter your username: ")
            password = getpass.getpass("Enter your password: ")

            logged_user = sql_manager.login(username, password)

            if logged_user:
                logged_menu(logged_user)
            else:
                print("Login failed")

        elif command[0] == "reset-password" and len(command) >1:
            reset_hash = hashlib.sha1(str(random.random()).encode()).hexdigest()
            sql_manager.update_reset_hash(command[1], reset_hash)
            send_email.send_email(sql_manager.get_email(command[1]), reset_hash)
            print(command[1])


        elif command[0] == "send-reset-password" and len(command) > 1:
            reset_hash = input("Enter reset hash: ")
            if reset_hash == sql_manager.get_reset_hash(command[1]):
                logged_user = sql_manager.login_with_hash(command[1], reset_hash)
                if logged_user:
                    logged_menu(logged_user)
                else:
                    print("Login failed")


        elif command[0] == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")
            print("reset-password <name> - to reset password")
            print("send-reset-password <name> - to enter reset password")

        elif command[0] == 'exit':
            break
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>").split(" ")

        if command[0] == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')
        elif command[0] == 'changepass':
            new_pass = getpass.getpass("Enter your new password: ")
            while not sql_manager.is_strong(logged_user.get_username(), new_pass):
                print("Password is not strong enough!")
                new_pass = getpass.getpass("Enter your new password: ")
            sql_manager.change_pass(new_pass, logged_user)

        elif command[0] == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command[0] == 'show-message':
            print(logged_user.get_message())

        elif command[0] == "deposit" and len(command) > 1 and command[1].isdecimal():
            amount = int(command[1])
            sql_manager.deposit(logged_user.get_username(), amount)
            logged_user.deposit(amount)

        elif command[0] == "withdraw" and len(command) > 1 and command[1].isdecimal():
            amount = int(command[1])
            if amount >  logged_user.get_balance():
                print("Insufficient funds")
            else:
                logged_user.withdraw(amount)
                sql_manager.withdraw(logged_user.get_username(), amount)

        elif command[0] == "display-balance":
            print("Balance: {}".format(logged_user.get_balance()))

        elif command[0] == "logout":
            break

        elif command[0] == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")
            print("deposit <amount> - deposits <amount>")
            print("withdraw <amount> - withdraws <amount>")
            print("display-balance - displays balance")
            print("logout - to logout")


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()
