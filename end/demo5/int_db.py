# Charlie
# date:2020/3/17 14:38
# file_name:int_db

import sqlite3

try:
    con = sqlite3.connect('demo5.db')
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS user；')
    cur.execute(
        "CREATE TABLE user (  id INTEGER PRIMARY KEY AUTOINCREMENT,  email TEXT UNIQUE NOT NULL,  password TEXT NOT NULL, create_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, is_admin INTEGER DEFAULT 0, is_active INTEGER DEFAULT 1 )")
    con.commit()
    cur.close()
    con.close()
except Exception as e:
    print(e)
