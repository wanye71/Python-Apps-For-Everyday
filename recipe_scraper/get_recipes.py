import requests
import csv
from bs4 import BeautifulSoup

class RecipeScraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        # Fetch the HTML content of the recipe page
        response = requests.get(self.url)
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            # Extract recipe title
            title = soup.find('h1').text.strip()

            # Extract ingredients
            ingredients = [ingredient.text.strip() for ingredient in soup.find_all('li', class_='mntl-structured-ingredients__list-item')]

            # Extract instructions
            instructions = [step.text.strip() for step in soup.find_all('li', class_='comp')]

            return {
                'title': title,
                'ingredients': ingredients,
                'instructions': instructions
            }
        else:
            print("Failed to fetch the page:", self.url)
            return None
        
