#import requests
import sqlite3
from Client import Client
#import hashlib
import datetime
import calendar
import uuid
import smtplib
import getpass


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
                email TEXT)''')
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


def send_mail_user(username):
    email = cursor.execute('''SELECT email
                                FROM clients WHERE username = ?
                                LIMIT 1''', (username, )).fetchone()
    email = email[0]
    hash_code = uuid.uuid4().hex
    to = email
    gmail_user = 'mihailynikolov@gmail.com'
    gmail_pwd = getpass.getpass('Pass for company email:')
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(gmail_user, gmail_pwd)
    smtpserver.sendmail(gmail_user, to, hash_code)
    smtpserver.close()
    return hash_code


#send_mail_user("misho")
