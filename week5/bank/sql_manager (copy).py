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
block_min = 5
block_sec = 3000
wr_times_in = 5


def create_clients_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                last_log TEXT,
                failed_logs INTEGER DEFAULT 0,
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


def block_conditions(result_obj):
    wr_pass_input_times = int(result_obj[0])
    date = datetime.datetime.now() + datetime.timedelta(minutes=block_min)
    cur_time = calendar.timegm(date.utctimetuple())

    last_log = result_obj[1]
    if last_log is None:
        last_log = cur_time
    else:
        last_log = int(result_obj[1])
    print('cur_time:{}'.format(cur_time))
    print('last_log:{}'.format(last_log))
    more_wr_inputs = wr_pass_input_times >= wr_times_in
    block_time_passed = cur_time - last_log >= block_sec
    print("time passed: {}".format(last_log - cur_time))
    if more_wr_inputs and block_time_passed:
        return True
    elif wr_pass_input_times >= block_min:
        return False


def increase_failed_logs(username):
    date = datetime.datetime.now()
    cur_time = calendar.timegm(date.utctimetuple())
    cursor.execute('''UPDATE clients SET last_log = ?,
                        failed_logs = failed_logs + 1
                        WHERE username = ? ''', (cur_time, username))
    conn.commit()


def login(username):
    result = cursor.execute('''SELECT failed_logs, last_log
                                FROM clients WHERE username = ?
                                LIMIT 1''', (username, )).fetchone()
    if block_conditions(result):
        cursor.execute('''UPDATE clients SET failed_logs = 0
                          WHERE username = ?''', (username, ))
        conn.commit()
    elif block_conditions(result) is False:
        print('You have 5 wrong passwords in a row')
        return False
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
