# Dutch Fuel Price Tracker

import requests
import re
from bs4 import BeautifulSoup

class FuelPriceTracker:
    def __init__(self):
        self.url = 'https://www.anwb.nl/brandstofprijzen'

    def fetch_prices(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return self.parse_prices(response.text)
        return None

    def parse_prices(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        price_table = soup.find('table', {'class': 'prices'})  # Adjust according to actual class
        prices = []

        for row in price_table.find_all('tr')[1:]:  # Skip header row
            columns = row.find_all('td')
            if len(columns) >= 2:
                fuel_type = columns[0].get_text(strip=True)
                price_raw = columns[1].get_text(strip=True)
                price = self.clean_price(price_raw)
                prices.append({'fuel_type': fuel_type, 'price': price})

        return prices

    def clean_price(self, price_str):
        price_match = re.search(r'\d+\.\d+', price_str)  # Get price with decimal
        return float(price_match.group(0)) if price_match else None

# Example of how to use the FuelPriceTracker
if __name__ == '__main__':
    tracker = FuelPriceTracker()
    prices = tracker.fetch_prices()
    print(prices)
