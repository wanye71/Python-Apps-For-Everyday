import requests
from bs4 import BeautifulSoup

class RecipeData:
    def __init__(self, url):
        self.url = url
    
    def fetch_page(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.text
        except requests.RequestException as e:
            print("Error fetching page:", e)
            return None
    
    def scrape_recipe(self, html):
        if html is None:
            return None
        try:
            soup = BeautifulSoup(html, 'html.parser')
            # Extract recipe title
            recipe_title = soup.find('h1', class_='article-heading').text.strip()
            # Extract ingredients
            ingredients = soup.find_all('li', class_='mntl-structured-ingredients__list-item')
            ingredient_list = [ingredient.text.strip() for ingredient in ingredients]
            # Extract instructions
            # instructions = soup.find_all('li', class_='mntl-sc-block-group--LI')
            instruction_list = []
            instruction_number = 1
            for instruction_tag in soup.find_all('li', class_='mntl-sc-block-group--LI'):
                instruction_text = instruction_tag.find('p').text.strip()
                instruction_list.append(f"Step {instruction_number}. {instruction_text}")
                instruction_number += 1
            return {'title': recipe_title, 'ingredients': ingredient_list, 'instructions': instruction_list}
        except Exception as e:
            print("Error scraping recipe:", e)
            return None








