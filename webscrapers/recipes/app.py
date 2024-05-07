from recipedata import RecipeData
from db_operations import  DatabaseOperations

from functools import partial
import tkinter as tk
from tkinter import messagebox

def insert_recipe(url_entry):
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
            db_ops.create_database()
            db_ops.create_table()

            db_ops.insert_row(title, ingredients, instructions)

            messagebox.showinfo("Success", "Recipe inserted successfully!")

def select_all_rows():
    db_ops = DatabaseOperations('recipes.db')
    rows = db_ops.select_all_rows()
    if rows:
        print("All Rows", "\n".join([str(row) for row in rows]))
    else:
        messagebox.showinfo("All Rows", "No rows found.")

def main():
    root = tk.Tk()
    root.title("Recipe Scraper GUI")
    root.geometry("400x300")

    url_label = tk.Label(root, text="Enter Recipe URL:")
    url_label.pack()

    url_entry = tk.Entry(root)
    url_entry.pack()

    insert_button = tk.Button(root, text="Insert Recipe", command=partial(insert_recipe, url_entry))
    insert_button.pack()
    
    select_button = tk.Button(root, text="Select All Rows", command=select_all_rows)
    select_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()