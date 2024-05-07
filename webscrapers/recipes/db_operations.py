import sqlite3

class DatabaseOperations:
    def __init__(self, db_name='recipes.db'):
        self.db_name = db_name
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cur = self.conn.cursor()
        except sqlite3.Error as e:
            print("Error connecting to database:", e)
    
    def create_database(self):
        try:
            self.connect()
            # Create the soups table
            self.cur.execute('''CREATE TABLE IF NOT EXISTS soups (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT UNIQUE,
                                ingredients TEXT,
                                instructions TEXT
                                )''')

            self.conn.commit()
            print("Database created successfully and table 'soups' created.")
        except sqlite3.Error as e:
            print("Error creating database or table:", e)
        finally:
            if self.conn:
                self.conn.close()

    def create_table(self, table_name):
        try:
            self.connect()
            self.cur.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT UNIQUE,
                                ingredients TEXT,
                                instructions TEXT
                                )''')
            self.conn.commit()
            print(f"Table '{table_name}' created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating table '{table_name}':", e)
        finally:
            self.close()

    def insert_row(self, table_name, title, ingredients, instructions):
        self.connect()
        try:
            self.cur.execute('''INSERT INTO {} (title, ingredients, instructions)
                                VALUES (?, ?, ?)'''.format(table_name), (title, ingredients, instructions))
            self.conn.commit()
        except sqlite3.Error as e:
            print("Error inserting row:", e)
        finally:
            self.close()
        print('data insert successful')
        
    def recipe_exists(self, title):
        """
        Check if a recipe with the given title already exists in the database.
        :param title: Title of the recipe to check.
        :return: True if the recipe exists, False otherwise.
        """
        self.connect()
        try:
            self.cur.execute('''SELECT COUNT(*) FROM soups WHERE title = ?''', (title,))
            count = self.cur.fetchone()[0]
            return count > 0
        except sqlite3.Error as e:
            print("Error checking if recipe exists:", e)
            return False
        finally:
            self.close()

    def select_all_rows(self, table_name):
        self.connect()
        rows = None
        try:
            self.cur.execute('''SELECT * FROM {}'''.format(table_name))
            rows = self.cur.fetchall()
        except sqlite3.Error as e:
            print("Error selecting all rows:", e)
        finally:
            self.close()
            print(rows)
            
    def delete_all_rows(self, table_name):
        self.connect()
        try:
            self.cur.execute('''DELETE FROM {}'''.format(table_name))
            self.conn.commit()
        except sqlite3.Error as e:
            print("Error deleting all rows:", e)
        finally:
            self.close()

    def close(self):
        if self.conn:
            self.conn.close()
