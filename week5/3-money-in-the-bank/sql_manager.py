import requests
import hashlib
import sqlite3
import string
from Client import Client

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT)'''

    cursor.execute(create_query)


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = '%s' WHERE id = '%s'" % (new_message, logged_user.get_id())
    cursor.execute(update_sql)
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    m = hashlib.sha1(new_pass.encode())
    new_pass = m.hexdigest()
    update_sql = "UPDATE clients SET password = '%s' WHERE id = '%s'" % (new_pass, logged_user.get_id())
    cursor.execute(update_sql)
    conn.commit()


def register(username, password):
    m = hashlib.sha1(password.encode())
    password = m.hexdigest()
    insert_sql = "insert into clients (username, password) values ('%s', '%s')" % (username, password)
    cursor.execute(insert_sql)
    conn.commit()


def login(username, password):
    m = hashlib.sha1(password.encode())
    password = m.hexdigest()
    select_query = "SELECT id, username, balance, message FROM clients WHERE username = '%s' AND password = '%s' LIMIT 1" % (username, password)

    cursor.execute(select_query)
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False


def is_strong(username, password):
    has_username = username in password
    has_length = len(password) >= 8
    has_capital_letter = False
    has_digit = False
    has_special_symbol = False
    for c in string.ascii_uppercase:
        if c in password:
            has_capital_letter = True
            break

    for digit in string.digits:
        if digit in password:
            has_digit = True
            break

    for symbol in string.punctuation:
        if symbol in password:
            has_special_symbol = True
            break

    return has_length and has_digit and has_capital_letter and\
        has_special_symbol and not has_username
