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
                email TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                reset_hash TEXT)'''

    cursor.execute(create_query)


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = ? WHERE id = ?"
    cursor.execute(update_sql, ((new_message, logged_user.get_id())))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    m = hashlib.sha1(new_pass.encode())
    new_pass = m.hexdigest()
    update_sql = "UPDATE clients SET password = ? WHERE id = ?"
    cursor.execute(update_sql, (new_pass, logged_user.get_id()))
    conn.commit()


def register(username, password, email):
    m = hashlib.sha1(password.encode())
    password = m.hexdigest()
    insert_sql = "insert into clients (username, password, email) values (?, ?, ?)"
    cursor.execute(insert_sql, (username, password, email))
    conn.commit()


def login(username, password):
    m = hashlib.sha1(password.encode())
    password = m.hexdigest()
    select_query = "SELECT id, username, email, balance, message FROM clients WHERE username = ? AND password = ? LIMIT 1"
    cursor.execute(select_query, (username, password))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3], user[4])
    else:
        return False

def login_with_hash(username, reset_hash):
    select_query = "SELECT id, username, email, balance, message FROM clients WHERE username = ? AND reset_hash = ? LIMIT 1"
    cursor.execute(select_query, (username, reset_hash))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3], user[4])
    else:
        return False

    cursor.execute("UPDATE clients SET reset_hash = ''")
    conn.commit()

def update_reset_hash(username, hash):
    update_reset_hash = "UPDATE clients SET reset_hash = ? WHERE username = ?"
    cursor.execute(update_reset_hash, (hash, username))
    conn.commit()

def get_email(username):
    cursor.execute("SELECT email from clients WHERE username = ?", (username, ))
    email = cursor.fetchone()
    if(email):
        return email[0]
    return False

def get_reset_hash(username):
    cursor.execute("SELECT reset_hash from clients WHERE username = ?", (username, ))
    reset_hash = cursor.fetchone()
    if(reset_hash):
        return reset_hash[0]
    return False

def deposit(username, amount):
    cursor.execute("SELECT balance from clients WHERE username = ?", (username, ))
    balance = cursor.fetchone()
    balance = balance[0]
    if(balance):
        balance += amount
        cursor.execute("UPDATE clients SET balance = ? WHERE username = ?", (balance, username))
        conn.commit()

def withdraw(username, amount):
    cursor.execute("SELECT balance from clients WHERE username = ?", (username, ))
    balance = cursor.fetchone()
    balance = balance[0]
    if(balance):
        balance -= amount
        cursor.execute("UPDATE clients SET balance = ? WHERE username = ?", (balance, username))
        conn.commit()

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
