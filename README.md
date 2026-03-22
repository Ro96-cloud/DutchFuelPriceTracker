# DutchFuelPriceTracker
An application that shows fuel prices in the Netherlands.

## Overview
DutchFuelPriceTracker is a Python-based web scraper that retrieves current fuel prices from the ANWB (Royal Dutch Motorists' Association) website and displays them in a formatted manner.

## Features
- Scrapes real-time fuel prices from ANWB
- Tracks multiple fuel types:
  - Euro 95 (E10)
  - Super Plus 98 (E5)
  - Diesel (B7)
  - LPG
- Displays prices with timestamps
- Handles web scraping with proper error handling

## Dependencies
- `requests` - HTTP library for fetching web pages
- `BeautifulSoup` - HTML parsing library for extracting price data
- `datetime` - For timestamp formatting
- `re` - Regular expressions for price text processing

## Usage
Run the application with:
```bash
python DutchFuelPriceTracker.py
```

The application will fetch current fuel prices from ANWB and display them in the console with the current date and time.

## How It Works
1. Fetches the ANWB fuel price page
2. Parses the HTML table containing fuel prices
3. Extracts price data and fuel types using CSS classes
4. Cleans and converts price strings to float values
5. Displays all fuel prices formatted with € symbol and 3 decimal places