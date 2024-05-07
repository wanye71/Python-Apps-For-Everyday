# from recipedata import RecipeData
# from db_operations import  DatabaseOperations

# from functools import partial
# import tkinter as tk
# from tkinter import messagebox

# def insert_recipe(url_entry):
#     url = url_entry.get()
#     url_entry.delete(0, tk.END)  # Clear the input field
#     recipe_scraper = RecipeData(url)
#     html = recipe_scraper.fetch_page()

#     if html:
#         recipe_data = recipe_scraper.scrape_recipe(html)
#         if recipe_data:
#             title = recipe_data['title']
#             ingredients = '\n'.join(recipe_data['ingredients'])
#             instructions = '\n'.join(recipe_data['instructions'])

#             db_ops = DatabaseOperations('recipes.db')
#             db_ops.create_database()
#             db_ops.create_table()

#             db_ops.insert_row(title, ingredients, instructions)

#             messagebox.showinfo("Success", "Recipe inserted successfully!")

# def select_all_rows():
#     db_ops = DatabaseOperations('recipes.db')
#     rows = db_ops.select_all_rows()
#     if rows:
#         print("All Rows", "\n".join([str(row) for row in rows]))
#     else:
#         messagebox.showinfo("All Rows", "No rows found.")

# def main():
#     root = tk.Tk()
#     root.title("Recipe Scraper GUI")
#     root.geometry("200x200")
#     custom_font = ("Arial", 13)

#     url_label = tk.Label(root, text="Enter Recipe URL:")
#     url_label.pack()

#     url_entry = tk.Entry(root)
#     url_entry.pack()

#     insert_button = tk.Button(root, text="Insert Recipe", width=15, font=custom_font,
#                               command=partial(insert_recipe, url_entry))
#     insert_button.pack()
    
#     select_button = tk.Button(root, text="Select All Rows", width=15, font=custom_font,
#                               command=select_all_rows)
#     select_button.pack()

#     root.mainloop()

# if __name__ == "__main__":
#     main()



import tkinter as tk
from tkinter import messagebox
from functools import partial
from recipedata import RecipeData
from db_operations import DatabaseOperations

def create_database(database_entry):
    db_name = database_entry.get() + '.db'
    db_ops = DatabaseOperations(db_name)
    db_ops.create_database()
    database_entry.config(state=tk.DISABLED)
    messagebox.showinfo("Database Created", f"Database '{db_name}' created successfully.")

def create_table(table_entry):
    table_name = table_entry.get()
    db_ops = DatabaseOperations('recipes.db')
    db_ops.create_table(table_name)
    messagebox.showinfo("Table Created", f"Table '{table_name}' created successfully.")

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
            db_ops.insert_row(title, ingredients, instructions)
            messagebox.showinfo("Success", "Recipe inserted successfully!")

def select_all_rows():
    db_ops = DatabaseOperations('recipes.db')
    rows = db_ops.select_all_rows()
    if rows:
        print("All Rows", "\n".join([str(row) for row in rows]))
    else:
        messagebox.showinfo("All Rows", "No rows found.")

def delete_all_rows():
    db_ops = DatabaseOperations('recipes.db')
    db_ops.delete_all_rows()
    messagebox.showinfo("Rows Deleted", "All rows deleted successfully.")

def main():
    root = tk.Tk()
    root.title("Recipe Scraper GUI")
    root.geometry("400x400")
    custom_font = ("Arial", 13)

    # Frame for creating database
    db_frame = tk.Frame(root)
    db_frame.pack(pady=10)

    create_db_label = tk.Label(db_frame, text="Create Database:")
    create_db_label.pack(side=tk.LEFT, padx=5)

    database_entry = tk.Entry(db_frame)
    database_entry.pack(side=tk.LEFT, padx=5)

    create_db_button = tk.Button(db_frame, text="Create", font=custom_font,
                                 command=partial(create_database, database_entry))
    create_db_button.pack(side=tk.LEFT, padx=5)

    # Frame for creating table
    table_frame = tk.Frame(root)
    table_frame.pack(pady=10)

    create_table_label = tk.Label(table_frame, text="Create Table:")
    create_table_label.pack(side=tk.LEFT, padx=5)

    table_entry = tk.Entry(table_frame)
    table_entry.pack(side=tk.LEFT, padx=5)

    create_table_button = tk.Button(table_frame, text="Create", font=custom_font,
                                    command=partial(create_table, table_entry))
    create_table_button.pack(side=tk.LEFT, padx=5)

    # Frame for inserting recipe URLs
    insert_frame = tk.Frame(root)
    insert_frame.pack(pady=10)

    insert_url_label = tk.Label(insert_frame, text="Insert Recipe URL:")
    insert_url_label.pack(side=tk.LEFT, padx=5)

    url_entry = tk.Entry(insert_frame)
    url_entry.pack(side=tk.LEFT, padx=5)

    insert_button = tk.Button(insert_frame, text="Insert", font=custom_font,
                              command=partial(insert_recipe, url_entry))
    insert_button.pack(side=tk.LEFT, padx=5)

    # Frame for buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    select_button = tk.Button(button_frame, text="Select All Rows", font=custom_font,
                              command=select_all_rows)
    select_button.pack(side=tk.LEFT, padx=5)

    delete_button = tk.Button(button_frame, text="Delete All Rows", font=custom_font,
                              command=delete_all_rows)
    delete_button.pack(side=tk.LEFT, padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()
