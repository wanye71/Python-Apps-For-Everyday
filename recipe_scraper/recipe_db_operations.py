import tkinter as tk
from tkinter import messagebox
from functools import partial
import sqlite3
import csv
from openpyxl import Workbook


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
        print(recipes)

        # Write recipes to CSV file
        with open('recipes.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'title', 'ingredients', 'instructions']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for recipe in recipes:
                writer.writerow({'id': recipe[0], 'title': recipe[1], 'ingredients': recipe[2], 'instructions': recipe[3]})

        print("All recipes saved to recipes.csv")
        
        # Write recipes to Excel file
        wb = Workbook()
        ws = wb.active
        ws.append(['id', 'title', 'ingredients', 'instructions'])
        for recipe in recipes:
            ws.append(recipe)
        
        wb.save('recipes.xlsx')
        print("All recipes saved to recipes.xlsx")
    
    def delete_all_recipes(self):
        # Delete all rows from the recipes table
        self.c.execute("DELETE FROM recipes")

        # Commit changes
        self.conn.commit()

    def close_connection(self):
        # Close connection
        self.conn.close()

