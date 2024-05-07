import sqlite3

class DatabaseOperations:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()
        

    def create_database(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cur = self.conn.cursor()
        except sqlite3.Error as e:
            print("Error connecting to database:", e)

    def create_table(self):
        try:
            self.cur.execute('''CREATE TABLE IF NOT EXISTS soups (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT UNIQUE,
                                ingredients TEXT,
                                instructions TEXT
                                )''')
            self.conn.commit()
        except sqlite3.Error as e:
            print("Error creating table:", e)

    def insert_row(self, title, ingredients, instructions):
        try:
            self.cur.execute('''INSERT INTO soups (title, ingredients, instructions)
                                VALUES (?, ?, ?)''', (title, ingredients, instructions))
            self.conn.commit()
        except sqlite3.Error as e:
            print("Error inserting row:", e)

    def select_all_rows(self):
        try:
            self.cur.execute('''SELECT * FROM soups''')
            rows = self.cur.fetchall()
            return rows
        except sqlite3.Error as e:
            print("Error selecting all rows:", e)

    def __del__(self):
        if self.conn:
            self.conn.close()


