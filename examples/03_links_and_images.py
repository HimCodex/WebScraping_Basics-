"""
Scraping Links and Images Example
This script demonstrates how to extract all links and images from a webpage
and organize them properly using BeautifulSoup.
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


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


def extract_all_links(soup, base_url):
    """
    Extract all links from the webpage and convert relative URLs to absolute.
    
    Args:
        soup (BeautifulSoup): Parsed HTML content
        base_url (str): Base URL for resolving relative links
        
    Returns:
        list: List of dictionaries containing link text and URL
    """
    links = []
    
    for link in soup.find_all('a'):
        href = link.get('href')
        text = link.text.strip()
        
        if href:
            # Convert relative URLs to absolute
            absolute_url = urljoin(base_url, href)
            links.append({
                'text': text if text else 'No text',
                'url': absolute_url
            })
    
    return links


def extract_all_images(soup, base_url):
    """
    Extract all images from the webpage.
    
    Args:
        soup (BeautifulSoup): Parsed HTML content
        base_url (str): Base URL for resolving relative image paths
        
    Returns:
        list: List of dictionaries containing image details
    """
    images = []
    
    for img in soup.find_all('img'):
        src = img.get('src')
        alt = img.get('alt', 'No alt text')
        title = img.get('title', 'No title')
        
        if src:
            # Convert relative URLs to absolute
            absolute_url = urljoin(base_url, src)
            images.append({
                'src': absolute_url,
                'alt': alt,
                'title': title
            })
    
    return images


def categorize_links(links):
    """
    Categorize links into internal and external.
    
    Args:
        links (list): List of link dictionaries
        
    Returns:
        dict: Dictionary with 'internal' and 'external' lists
    """
    categorized = {
        'internal': [],
        'external': []
    }
    
    if not links:
        return categorized
    
    # Get base domain from first link
    base_domain = urlparse(links[0]['url']).netloc
    
    for link in links:
        parsed = urlparse(link['url'])
        
        if parsed.netloc == base_domain or not parsed.netloc:
            categorized['internal'].append(link)
        else:
            categorized['external'].append(link)
    
    return categorized


def main():
    """
    Main function to demonstrate link and image scraping.
    """
    url = "https://example.com"
    
    print(f"Scraping links and images from: {url}\n")
    
    soup = scrape_page(url)
    
    if soup:
        # Extract all links
        links = extract_all_links(soup, url)
        print(f"Total Links Found: {len(links)}")
        
        if links:
            # Show first few links
            print("\nFirst 5 links:")
            for i, link in enumerate(links[:5], 1):
                print(f"  {i}. Text: {link['text']}")
                print(f"     URL: {link['url']}")
            
            # Categorize links
            categorized = categorize_links(links)
            print(f"\nInternal Links: {len(categorized['internal'])}")
            print(f"External Links: {len(categorized['external'])}")
        
        # Extract all images
        images = extract_all_images(soup, url)
        print(f"\nTotal Images Found: {len(images)}")
        
        if images:
            print("\nImage details:")
            for i, img in enumerate(images, 1):
                print(f"  {i}. Source: {img['src']}")
                print(f"     Alt: {img['alt']}")
                if img['title'] != 'No title':
                    print(f"     Title: {img['title']}")
    else:
        print("Failed to scrape the webpage.")


if __name__ == "__main__":
    main()
