import tkinter as tk
from tkinter import messagebox
from get_recipes import RecipeScraper
from recipe_db_operations import RecipeDatabase

class RecipeDBUI:
    def __init__(self, master):
        self.master = master
        master.title("Recipe Database UI")
        master.geometry("400x300")

        self.url_label = tk.Label(master, text="Enter Recipe URL:")
        self.url_label.pack(pady=5)

        self.url_entry = tk.Entry(master, width=40)
        self.url_entry.pack(pady=5)

        self.store_button = tk.Button(master, text="Store Recipe Data", command=self.store_recipe)
        self.store_button.pack(pady=10)

        self.delete_button = tk.Button(master, text="Delete All Recipes", command=self.delete_all_recipes)
        self.delete_button.pack(pady=10)

        self.get_button = tk.Button(master, text="Get All Recipes", command=self.get_all_recipes)
        self.get_button.pack(pady=10)

        # Initialize RecipeDatabase
        self.db_name = 'recipes.db'
        self.recipe_db = RecipeDatabase(self.db_name)

    def store_recipe(self):
        # Call to store recipe data
        url = self.url_entry.get()
        if url:
            scraper = RecipeScraper(url)  # Initialize RecipeScraper with the URL
            recipe_data = scraper.scrape()
            self.recipe_db.store_recipe_data(recipe_data)
            messagebox.showinfo("Store Recipe Data", "Recipe data stored successfully.")
            self.url_entry.delete(0, tk.END)  # Clear the input field
        else:
            messagebox.showwarning("No URL", "Please enter a URL.")

    def delete_all_recipes(self):
        # Call to delete all recipes
        self.recipe_db.delete_all_recipes()
        messagebox.showinfo("Delete All Recipes", "All recipes deleted successfully.")

    def get_all_recipes(self):
        # Call to get all recipes
        recipes = self.recipe_db.get_all_recipes()
        print(recipes)
        messagebox.showinfo("Get All Recipes", "All recipes retrieved successfully.")
        