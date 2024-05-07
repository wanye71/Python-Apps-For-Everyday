import tkinter as tk
from tkinter import messagebox
from functools import partial
from recipedata import RecipeData
from db_operations import DatabaseOperations

class UI:
    def create_database(self, database_entry):
        db_name = database_entry.get() + '.db'
        db_ops = DatabaseOperations(db_name)
        db_ops.create_database()
        database_entry.config(state=tk.DISABLED)
        messagebox.showinfo("Database Created", f"Database '{db_name}' created successfully.")

    def insert_recipe(self, url_entry):
        url = url_entry.get()
        url_entry.delete(0, tk.END)  # Clear the input field
        recipe_scraper = RecipeData(url)
        html = recipe_scraper.fetch_page()

        if html:
            recipe_data = recipe_scraper.scrape_recipe(html)
            if recipe_data:
                title = recipe_data['title']
                ingredients = '\n'.join(recipe_data['ingredients'])
                instructions = '\n'.join(recipe_data['instructions'])

                db_ops = DatabaseOperations('recipes.db')
                db_ops.insert_row('soups', title, ingredients, instructions)  # assuming 'soups' is the table name
                messagebox.showinfo("Success", "Recipe inserted successfully!")

    def select_all_rows(self):
        db_ops = DatabaseOperations('recipes.db')
        rows = db_ops.select_all_rows('soups')
        if rows:
            messagebox.showinfo("All Rows", "\n".join([str(row) for row in rows]))
        else:
            messagebox.showinfo("All Rows", "No rows found.")

    def delete_all_rows(self):
        db_ops = DatabaseOperations('recipes.db')
        db_ops.delete_all_rows('soups')
        messagebox.showinfo("Rows Deleted", "All rows deleted successfully.")

    def create_ui(self):
        root = tk.Tk()
        root.title("Recipe Scraper GUI")
        root.geometry("600x400+1000+100")
        custom_font = ("Arial", 13)

        # Frame for creating database
        db_frame = tk.Frame(root)
        db_frame.pack(pady=10)

        create_db_label = tk.Label(db_frame, text="Create Database:")
        create_db_label.grid(row=0, column=0, padx=5)

        database_entry = tk.Entry(db_frame)
        database_entry.grid(row=0, column=1, padx=5)

        create_db_button = tk.Button(db_frame, text="Create", font=custom_font,
                                     command=partial(self.create_database, database_entry))
        create_db_button.grid(row=0, column=2, padx=5)

        # Frame for inserting recipe URLs
        insert_frame = tk.Frame(root)
        insert_frame.pack(pady=10)

        insert_url_label = tk.Label(insert_frame, text="Insert Recipe URL:")
        insert_url_label.grid(row=0, column=0, padx=5)

        url_entry = tk.Entry(insert_frame)
        url_entry.grid(row=0, column=1, padx=5)

        insert_button = tk.Button(insert_frame, text="Insert", font=custom_font,
                          command=lambda: self.insert_recipe(url_entry))
        insert_button.grid(row=0, column=2, padx=5)

        # Frame for buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        select_button = tk.Button(button_frame, text="Select All Rows", font=custom_font,
                                  command=self.select_all_rows)
        select_button.grid(row=0, column=0, padx=5)

        delete_button = tk.Button(button_frame, text="Delete All Rows", font=custom_font,
                                  command=self.delete_all_rows)
        delete_button.grid(row=0, column=1, padx=5)

        root.mainloop()
# https://www.allrecipes.com/recipe/236187/german-potato-bacon-soup/