"""
Advanced Web Scraping Techniques
This script demonstrates advanced techniques including:
- Custom headers and user agents
- Handling sessions and cookies
- Error handling and retries
- Rate limiting
"""

import requests
from bs4 import BeautifulSoup
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def create_session_with_retries():
    """
    Create a requests session with automatic retry logic.
    
    Returns:
        requests.Session: Configured session with retry strategy
    """
    session = requests.Session()
    
    # Define retry strategy
    retry_strategy = Retry(
        total=3,  # Total number of retries
        backoff_factor=1,  # Wait 1, 2, 4 seconds between retries
        status_forcelist=[429, 500, 502, 503, 504],  # Retry on these status codes
        allowed_methods=["HEAD", "GET", "OPTIONS"]
    )
    
    # Mount the retry strategy to the session
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    
    return session


def scrape_with_custom_headers(url, user_agent=None):
    """
    Scrape a webpage with custom headers including user agent.
    
    Args:
        url (str): The URL to scrape
        user_agent (str): Custom user agent string
        
    Returns:
        BeautifulSoup: Parsed HTML content
    """
    # Default user agent if none provided
    if not user_agent:
        user_agent = (
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) '
            'Chrome/91.0.4472.124 Safari/537.36'
        )
    
    headers = {
        'User-Agent': user_agent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
    }
    
    try:
        session = create_session_with_retries()
        response = session.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'lxml')
        return soup
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def scrape_with_rate_limiting(urls, delay=1):
    """
    Scrape multiple URLs with rate limiting to avoid overwhelming the server.
    
    Args:
        urls (list): List of URLs to scrape
        delay (float): Delay in seconds between requests
        
    Returns:
        list: List of parsed HTML content (BeautifulSoup objects)
    """
    results = []
    
    for i, url in enumerate(urls, 1):
        print(f"Scraping URL {i}/{len(urls)}: {url}")
        
        soup = scrape_with_custom_headers(url)
        results.append(soup)
        
        # Add delay between requests (except for the last one)
        if i < len(urls):
            time.sleep(delay)
    
    return results


def scrape_with_session(url):
    """
    Scrape using a session to maintain cookies and connection pooling.
    
    Args:
        url (str): The URL to scrape
        
    Returns:
        tuple: (BeautifulSoup object, cookies dict)
    """
    session = requests.Session()
    
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'lxml')
        cookies = session.cookies.get_dict()
        
        return soup, cookies
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None, None


def extract_metadata(soup):
    """
    Extract metadata from the webpage (title, description, keywords).
    
    Args:
        soup (BeautifulSoup): Parsed HTML content
        
    Returns:
        dict: Dictionary containing metadata
    """
    metadata = {
        'title': None,
        'description': None,
        'keywords': None,
        'author': None
    }
    
    if not soup:
        return metadata
    
    # Extract title
    title_tag = soup.find('title')
    if title_tag:
        metadata['title'] = title_tag.text.strip()
    
    # Extract meta tags
    meta_tags = soup.find_all('meta')
    
    for tag in meta_tags:
        name = tag.get('name', '').lower()
        property_name = tag.get('property', '').lower()
        content = tag.get('content', '')
        
        if name == 'description' or property_name == 'og:description':
            metadata['description'] = content
        elif name == 'keywords':
            metadata['keywords'] = content
        elif name == 'author':
            metadata['author'] = content
    
    return metadata


def main():
    """
    Main function to demonstrate advanced scraping techniques.
    """
    url = "https://example.com"
    
    print("Advanced Web Scraping Techniques Demo\n")
    print("=" * 60)
    
    # Example 1: Scraping with custom headers
    print("\n1. Scraping with custom headers and user agent")
    soup = scrape_with_custom_headers(url)
    
    if soup:
        print("✓ Successfully scraped with custom headers")
        
        # Extract metadata
        metadata = extract_metadata(soup)
        print("\nPage Metadata:")
        for key, value in metadata.items():
            if value:
                print(f"  {key.capitalize()}: {value}")
    
    # Example 2: Scraping with session
    print("\n2. Scraping with session (maintains cookies)")
    soup, cookies = scrape_with_session(url)
    
    if soup:
        print("✓ Successfully scraped with session")
        print(f"  Cookies received: {len(cookies)} cookie(s)")
    
    # Example 3: Rate limiting (commented out to avoid multiple requests)
    print("\n3. Rate limiting demonstration")
    print("  Use scrape_with_rate_limiting() to scrape multiple URLs")
    print("  with delays between requests to be respectful to servers")
    
    print("\n" + "=" * 60)
    print("\nBest Practices for Web Scraping:")
    print("  1. Always use custom User-Agent headers")
    print("  2. Implement rate limiting to avoid overwhelming servers")
    print("  3. Handle errors gracefully with retry logic")
    print("  4. Respect robots.txt and website terms of service")
    print("  5. Use sessions for multiple requests to the same domain")


if __name__ == "__main__":
    main()
