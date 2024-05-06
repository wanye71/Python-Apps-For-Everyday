import tkinter as tk
from get_recipes import RecipeScraper
from recipe_db_operations import RecipeDatabase
from recipe_db_ui import RecipeDBUI

if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeDBUI(root)
    root.mainloop()

