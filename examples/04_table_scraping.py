"""
Scraping HTML Tables Example
This script demonstrates how to extract and parse HTML tables from webpages
using BeautifulSoup and organize data into structured format.
"""

import requests
from bs4 import BeautifulSoup


def scrape_page(url):
    """
    Fetch and parse a webpage.
    
    Args:
        url (str): The URL to scrape
        
    Returns:
        BeautifulSoup: Parsed HTML content
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'lxml')
        return soup
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def extract_table_data(table):
    """
    Extract data from an HTML table element.
    
    Args:
        table: BeautifulSoup table element
        
    Returns:
        dict: Dictionary containing headers and rows
    """
    # Extract headers
    headers = []
    header_row = table.find('thead')
    
    if header_row:
        headers = [th.text.strip() for th in header_row.find_all('th')]
    else:
        # Try to get headers from first row
        first_row = table.find('tr')
        if first_row:
            headers = [th.text.strip() for th in first_row.find_all('th')]
    
    # Extract rows
    rows = []
    tbody = table.find('tbody')
    
    if tbody:
        table_rows = tbody.find_all('tr')
    else:
        table_rows = table.find_all('tr')
        # Skip header row if headers were found
        if headers:
            table_rows = table_rows[1:]
    
    for row in table_rows:
        cells = row.find_all(['td', 'th'])
        row_data = [cell.text.strip() for cell in cells]
        if row_data:  # Only add non-empty rows
            rows.append(row_data)
    
    return {
        'headers': headers,
        'rows': rows
    }


def extract_all_tables(soup):
    """
    Extract all tables from the webpage.
    
    Args:
        soup (BeautifulSoup): Parsed HTML content
        
    Returns:
        list: List of dictionaries containing table data
    """
    tables = soup.find_all('table')
    all_table_data = []
    
    for i, table in enumerate(tables, 1):
        table_data = extract_table_data(table)
        table_data['table_number'] = i
        all_table_data.append(table_data)
    
    return all_table_data


def display_table(table_data):
    """
    Display table data in a formatted way.
    
    Args:
        table_data (dict): Dictionary containing table headers and rows
    """
    print(f"\n--- Table {table_data['table_number']} ---")
    
    # Display headers
    if table_data['headers']:
        print("Headers:", " | ".join(table_data['headers']))
        print("-" * 80)
    
    # Display rows
    if table_data['rows']:
        for i, row in enumerate(table_data['rows'], 1):
            print(f"Row {i}: {' | '.join(row)}")
    else:
        print("No rows found in this table")


def table_to_dict_list(table_data):
    """
    Convert table data to a list of dictionaries (one dict per row).
    
    Args:
        table_data (dict): Dictionary containing table headers and rows
        
    Returns:
        list: List of dictionaries with header names as keys
    """
    if not table_data['headers'] or not table_data['rows']:
        return []
    
    dict_list = []
    headers = table_data['headers']
    
    for row in table_data['rows']:
        # Create a dictionary for each row
        row_dict = {}
        for i, value in enumerate(row):
            # Use header as key, or generate a key if more columns than headers
            key = headers[i] if i < len(headers) else f"Column_{i+1}"
            row_dict[key] = value
        dict_list.append(row_dict)
    
    return dict_list


def main():
    """
    Main function to demonstrate table scraping.
    Note: This example shows the structure. For a working demo,
    you would need a URL with actual HTML tables.
    """
    # Example URL - replace with a URL containing tables
    url = "https://example.com"
    
    print(f"Scraping tables from: {url}\n")
    print("Note: This is a demonstration of table scraping functionality.")
    print("To see actual results, use a URL with HTML tables.\n")
    
    soup = scrape_page(url)
    
    if soup:
        # Extract all tables
        tables = extract_all_tables(soup)
        
        print(f"Total Tables Found: {len(tables)}")
        
        if tables:
            for table_data in tables:
                display_table(table_data)
                
                # Convert to list of dictionaries
                dict_list = table_to_dict_list(table_data)
                if dict_list:
                    print(f"\nFirst row as dictionary:")
                    print(dict_list[0])
        else:
            print("\nNo tables found on this page.")
            print("\nExample of how to use this script:")
            print("1. Find a webpage with HTML tables")
            print("2. Replace the URL variable with that webpage")
            print("3. Run the script to extract and parse the tables")
    else:
        print("Failed to scrape the webpage.")


if __name__ == "__main__":
    main()
