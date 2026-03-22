import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

def get_nl_fuel_prices():
    """Scrape current fuel prices from ANWB or similar Dutch source"""
    try:
        url = "https://www.anwb.nl/auto/brandstof/benzineprijs"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        prices = {
            'Euro 95 (E10)': None,
            'Super Plus 98 (E5)': None,
            'Diesel (B7)': None,
            'LPG': None
        }
        
        # Find all rows in the table
        rows = soup.find_all('tr')
        
        for row in rows:
            # Find fuel type (first td with specific class)
            fuel_type_td = row.find('td', class_='prose-labelMedium sbr-py-100 sbr-text-subtle')
            # Find price (second td with specific class)
            price_td = row.find('td', class_='prose-paragraphBodyMedium sbr-py-100 sbr-text-right')
            
            if fuel_type_td and price_td:
                fuel_type = fuel_type_td.get_text(strip=True)
                # Extract just the price number, removing <sup> tags and commas/dots
                price_text = price_td.get_text(strip=True)
                # Remove superscript numbers and convert comma to dot for float conversion
                price_clean = re.sub(r'[⁰-⁹]', '', price_text).replace(',', '.')
                
                try:
                    price = float(price_clean)
                    if fuel_type in prices:
                        prices[fuel_type] = price
                except ValueError:
                    pass
        
        return prices
        
    except Exception as e:
        print(f"Error fetching prices: {e}")
        return None

def display_prices(prices):
    """Display fuel prices nicely"""
    print(f"\n{'='*50}")
    print(f"Nederlandse Brandstofprijzen - {datetime.now().strftime('%d-%m-%Y %H:%M')}")
    print(f"{'='*50}\n")
    
    if prices:
        for fuel_type, price in prices.items():
            if price:
                print(f"  {fuel_type:12} € {price:.3f} / liter")
    else:
        print("  Could not fetch prices")
    
    print()

if __name__ == "__main__":
    prices = get_nl_fuel_prices()
    display_prices(prices)