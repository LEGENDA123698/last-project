import sqlite3

conn = sqlite3.connect('sign.db')
cs = conn.cursor()

def create_db_table():
    cs.execute('''
              CREATE TABLE IF NOT EXISTS user
              (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                type_user TEXT,
                password INTEGER,
                nickname TEXT
              )
              ''')
create_db_table()


def add_user():
    user = [('LEGENDA'),('123456789'),('slavik.doronin@gmail.com')]
    cs.execute('INSERT INTO user (type_user,password,nickname) VALUES (?,?,?)', user)

add_user()
conn.commit()