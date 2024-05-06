import tkinter as tk
from tkinter import messagebox
from functools import partial
import sqlite3


class RecipeDatabase:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.c = self.conn.cursor()

        # Create table if not exists
        self.c.execute('''CREATE TABLE IF NOT EXISTS recipes
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, ingredients TEXT, instructions TEXT)''')

    def recipe_exists(self, title, ingredients, instructions):
        # Check if a recipe with the same title, ingredients, and instructions already exists
        self.c.execute("SELECT * FROM recipes WHERE title=? AND ingredients=? AND instructions=?",
                       (title, "\n".join(ingredients), "\n".join(instructions)))
        return bool(self.c.fetchone())

    def store_recipe_data(self, recipe_data):
        title = recipe_data['title']
        ingredients = recipe_data['ingredients']
        instructions = recipe_data['instructions']

        # Check if the recipe already exists
        if self.recipe_exists(title, ingredients, instructions):
            print("Recipe already exists.")
            return

        # Insert recipe data into the table
        self.c.execute("INSERT INTO recipes (title, ingredients, instructions) VALUES (?, ?, ?)",
                       (title, "\n".join(ingredients), "\n".join(instructions)))

        # Commit changes
        self.conn.commit()
        print("Recipe data stored successfully.")

    def get_all_recipes(self):
        # Execute SELECT statement to retrieve all recipes
        self.c.execute("SELECT * FROM recipes")
        recipes = self.c.fetchall()

        return recipes
    
    def delete_all_recipes(self):
        # Delete all rows from the recipes table
        self.c.execute("DELETE FROM recipes")

        # Commit changes
        self.conn.commit()

    def close_connection(self):
        # Close connection
        self.conn.close()

