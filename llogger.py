#!/home/julivanespi/anaconda3/bin/python

import sqlite3
import time
import datetime
import os
import socket

PATH_TO_DB = '/home/julivanespi/my_dbs/myLoginInfo.db'


def create_table():
    c.execute(
        'CREATE TABLE IF NOT EXISTS logins(datestamp TEXT, user TEXT, hostname TEXT)')


def log_it():
    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(
        unix).strftime('%Y-%m-%d %H:%M:%S'))
    user = os.getenv('USER')
    hostname = socket.gethostname()

    c.execute('INSERT INTO logins(datestamp, user, hostname) VALUES (?, ?, ?)',
              (date, user, hostname))

    conn.commit()


if __name__ == "__main__":
    conn = sqlite3.connect(PATH_TO_DB)
    c = conn.cursor()

    create_table()
    log_it()
    # print(socket.gethostname())
