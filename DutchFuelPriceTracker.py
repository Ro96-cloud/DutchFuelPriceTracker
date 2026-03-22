import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_nl_fuel_prices():
    """Scrape current fuel prices from ANWB or similar Dutch source"""
    try:
        # Example: Using a simple API endpoint or web scrape
        # You could also use RapidAPI for European fuel prices
        
        url = "https://www.anwb.nl/auto/brandstof/benzineprijs"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find price tables (you'd need to inspect the HTML to find exact selectors)
        prices = {
            'Euro 95 (E10)': None,
            'Super Plus 98 (E5)': None,
            'Diesel (B7)': None,
            'LPG': None
        }
        
        return prices
        
    except Exception as e:
        print(f"Error fetching prices: {e}")
        return None

def display_prices(prices):
    """Display fuel prices nicely"""
    print(f"\n{'='*50}")
    print(f"Nederlands Brandstofprijzen - {datetime.now().strftime('%d-%m-%Y %H:%M')}")
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