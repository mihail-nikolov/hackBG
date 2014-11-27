import sqlite3
from Client import Client
import datetime
import calendar
import uuid
import smtplib
import getpass
TAN_len = 32
TAN_use = 10

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                is_blocked BOOLEAN DEFAULT False,
                blocked_at INTEGER DEFAULT 0,
                email TEXT,
                TANs TEXT,
                TAN_use_count INTEGER DEFAULT 0)''')
    conn.commit()


def change_message(new_message, logged_user):
    cursor.execute('''UPDATE clients SET message = ?
                     WHERE id = ?''', (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    cursor.execute('''UPDATE clients SET password = ?
                    WHERE id = ?''', (new_pass, logged_user.get_id()))
    conn.commit()


def register(username, password, email):
    cursor.execute('''INSERT INTO clients (username, email, password)
                        VALUES (?, ?, ?)''', (username, email, password))
    conn.commit()


def get_user_pass(username):
    result = cursor.execute('''SELECT password FROM
                    clients WHERE username = ?
                    LIMIT 1''', (username,)).fetchone()
    return result[0]


def check_password(existing_pass, entered_pass):
    return existing_pass == entered_pass


def block_user(username):
    date = datetime.datetime.now()
    time_blocked = calendar.timegm(date.utctimetuple())
    cursor.execute('''UPDATE clients SET blocked_at = ?, is_blocked = ?
                    WHERE username = ? ''', (time_blocked, 'True', username))
    conn.commit()


def unbclock_user(username):
    time_blocked = 0
    cursor.execute('''UPDATE clients SET blocked_at = ?, is_blocked = ?
                    WHERE username = ? ''', (time_blocked, 'False', username))
    conn.commit()


def get_user_bl_time(username):
    result = cursor.execute('''SELECT blocked_at FROM
                    clients WHERE username = ?
                    LIMIT 1''', (username,)).fetchone()
    return result[0]


def is_blocked(username):
    result = cursor.execute('''SELECT is_blocked FROM
                    clients WHERE username = ?
                    LIMIT 1''', (username,)).fetchone()
    return result[0]


def login(username):
    cursor.execute('''SELECT id, username, balance, message FROM
                    clients WHERE username = ? LIMIT 1''', (username, ))
    user = cursor.fetchone()
    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False


def get_hashcode():
    hash_code = uuid.uuid4().hex
    return hash_code


def send_mail_user(username, message):
    email = cursor.execute('''SELECT email
                                FROM clients WHERE username = ?
                                LIMIT 1''', (username, )).fetchone()
    email = email[0]

    to = email
    gmail_user = 'mihailynikolov@gmail.com'
    gmail_pwd = getpass.getpass('Pass for company email:')
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    smtpserver.sendmail(gmail_user, to, message)
    smtpserver.close()
    return message


def get_ran_str(str_len=32):
    random = str(uuid.uuid4())
    random = random.replace("-", "")
    return random[:str_len]


def is_TAN_used(username, TAN):
    TANs = cursor.execute('''SELECT TANs
                            FROM clients WHERE username = ?
                            LIMIT 1''', (username, )).fetchone()
    TANs = TANs[0]
    TANs = str(TANs)
    arr_TAN = TANs.split(", ")
    if TAN in arr_TAN:
        return True
    return False


def increase_TAN_counter(username):
    cursor.execute('''UPDATE clients SET TAN_use_count = TAN_use_count + 1
                    WHERE username = ? ''', (username, ))
    conn.commit()


def make_TAN_changes(username, new_TAN):
    TANs = cursor.execute('''SELECT TANs
                            FROM clients WHERE username = ?
                            LIMIT 1''', (username, )).fetchone()
    TANs = TANs[0]
    TANs = str(TANs)
    content_to_add = TANs + ", " + new_TAN
    cursor.execute('''UPDATE clients SET TAN_use_count = 0,
                    TANs = ?
                    WHERE username = ? ''', (content_to_add, username))
    conn.commit()


def is_curr_TAN(username, TAN):
    TANs = cursor.execute('''SELECT TANs
                            FROM clients WHERE username = ?
                            LIMIT 1''', (username, )).fetchone()
    TANs = str(TANs[0])
    arr_TAN = TANs.split(", ")
    if TAN == arr_TAN[- 1]:
        return True
    return False


def is_TAN_usable(username):
    counter = cursor.execute('''SELECT TAN_use_count
                            FROM clients WHERE username = ?
                            LIMIT 1''', (username, )).fetchone()
    counter = counter[0]
    if counter >= TAN_use:
        return False
    return True


def deposit_money(username, money):
    cursor.execute('''UPDATE clients SET balance = balance + ?
                    WHERE username = ? ''', (money, username))
    conn.commit()


def withdraw_money(username, money):
    cursor.execute('''UPDATE clients SET balance = balance - ?
                    WHERE username = ? ''', (money, username))
    conn.commit()


def get_balance(username):
    balance = cursor.execute('''SELECT balance
                            FROM clients WHERE username = ?
                            LIMIT 1''', (username, )).fetchone()
    balance = balance[0]
    return balance
