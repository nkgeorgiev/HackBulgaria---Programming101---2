class Client():
    def __init__(self, id, username, email, balance, message):
        self.__username = username
        self.__balance = balance
        self.__id = id
        self.__message = message
        self.email = email

    def get_username(self):
        return self.__username

    def get_balance(self):
        return self.__balance

    def get_id(self):
        return self.__id

    def get_message(self):
        return self.__message

    def get_email(self):
        return self.email

    def set_message(self, new_message):
        self.__message = new_message

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            return False
        else:
            self.__balance -= amount
        return True
