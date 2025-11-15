"""
Basic Web Scraping Example
This script demonstrates how to fetch a webpage and parse its HTML content
using requests and BeautifulSoup libraries.
"""

import requests
from bs4 import BeautifulSoup


def scrape_basic_html(url):
    """
    Fetch and parse HTML content from a given URL.
    
    Args:
        url (str): The URL to scrape
        
    Returns:
        BeautifulSoup: Parsed HTML content
    """
    try:
        # Send GET request to the URL
        response = requests.get(url, timeout=10)
        
        # Check if request was successful
        response.raise_for_status()
        
        # Parse HTML content
        soup = BeautifulSoup(response.content, 'lxml')
        
        return soup
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None


def extract_title(soup):
    """
    Extract the title from the parsed HTML.
    
    Args:
        soup (BeautifulSoup): Parsed HTML content
        
    Returns:
        str: Page title or None if not found
    """
    if soup:
        title = soup.find('title')
        return title.text if title else None
    return None


def extract_all_paragraphs(soup):
    """
    Extract all paragraph texts from the parsed HTML.
    
    Args:
        soup (BeautifulSoup): Parsed HTML content
        
    Returns:
        list: List of paragraph texts
    """
    if soup:
        paragraphs = soup.find_all('p')
        return [p.text.strip() for p in paragraphs if p.text.strip()]
    return []


def extract_all_headings(soup):
    """
    Extract all headings (h1-h6) from the parsed HTML.
    
    Args:
        soup (BeautifulSoup): Parsed HTML content
        
    Returns:
        dict: Dictionary with heading level as key and list of texts as value
    """
    if soup:
        headings = {}
        for i in range(1, 7):
            heading_tags = soup.find_all(f'h{i}')
            if heading_tags:
                headings[f'h{i}'] = [h.text.strip() for h in heading_tags]
        return headings
    return {}


def main():
    """
    Main function to demonstrate basic web scraping.
    """
    # Example URL (using a simple example site)
    url = "https://example.com"
    
    print(f"Scraping URL: {url}\n")
    
    # Fetch and parse the webpage
    soup = scrape_basic_html(url)
    
    if soup:
        # Extract and display title
        title = extract_title(soup)
        print(f"Page Title: {title}\n")
        
        # Extract and display headings
        headings = extract_all_headings(soup)
        print("Headings:")
        for level, texts in headings.items():
            print(f"  {level}: {texts}")
        print()
        
        # Extract and display first few paragraphs
        paragraphs = extract_all_paragraphs(soup)
        print(f"Found {len(paragraphs)} paragraphs")
        print("First paragraph:")
        if paragraphs:
            print(f"  {paragraphs[0]}")
    else:
        print("Failed to scrape the webpage.")


if __name__ == "__main__":
    main()
