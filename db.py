import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect('./members.db')  # Provide the correct path to your database file
        print(sqlite3.version)
    except Error as e:
        print(e)
 
    if conn:
        create_members_table(conn)  # Creates the table if it doesn't exist
        return conn

def create_members_table(conn):
    try:
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS members (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        age INTEGER,
                        sex TEXT,
                        goal TEXT,
                        time_availability TEXT,
                        contact_method TEXT,
                        phone_number TEXT,
                        email TEXT,
                        contact_address TEXT,
                        hear_about_us TEXT);
                    """)
    except Error as e:
        print(e)

def insert_member(conn, member):
    try:
        cur = conn.cursor()
        sql = '''INSERT INTO members(first_name, last_name, age, sex, goal, time_availability, contact_method, phone_number, email, contact_address, hear_about_us) 
                 VALUES(?,?,?,?,?,?,?,?,?,?,?)'''
        cur.execute(sql, member)
        return cur.lastrowid
    except Error as e:
        print(e)

def select_all_members(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM members")

    rows = cur.fetchall()

    for row in rows:
        print(row)
