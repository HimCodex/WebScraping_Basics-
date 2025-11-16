"""
CSS Selectors Web Scraping Example
This script demonstrates how to use CSS selectors to extract specific
elements from a webpage using BeautifulSoup.
"""

import requests
from bs4 import BeautifulSoup


def scrape_with_css_selectors(url):
    """
    Fetch webpage and demonstrate various CSS selector techniques.
    
    Args:
        url (str): The URL to scrape
    """
    try:
        # Send GET request
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.content, 'lxml')
        
        return soup
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def select_by_tag(soup, tag):
    """
    Select elements by tag name.
    
    Args:
        soup (BeautifulSoup): Parsed HTML
        tag (str): Tag name to search for
        
    Returns:
        list: List of matching elements
    """
    return soup.select(tag)


def select_by_class(soup, class_name):
    """
    Select elements by class name.
    
    Args:
        soup (BeautifulSoup): Parsed HTML
        class_name (str): Class name to search for
        
    Returns:
        list: List of matching elements
    """
    return soup.select(f'.{class_name}')


def select_by_id(soup, element_id):
    """
    Select element by ID.
    
    Args:
        soup (BeautifulSoup): Parsed HTML
        element_id (str): ID to search for
        
    Returns:
        element: Matching element or None
    """
    result = soup.select(f'#{element_id}')
    return result[0] if result else None


def select_by_attribute(soup, tag, attribute, value):
    """
    Select elements by attribute value.
    
    Args:
        soup (BeautifulSoup): Parsed HTML
        tag (str): Tag name
        attribute (str): Attribute name
        value (str): Attribute value
        
    Returns:
        list: List of matching elements
    """
    return soup.select(f'{tag}[{attribute}="{value}"]')


def select_nested_elements(soup, parent, child):
    """
    Select nested elements using descendant selector.
    
    Args:
        soup (BeautifulSoup): Parsed HTML
        parent (str): Parent selector
        child (str): Child selector
        
    Returns:
        list: List of matching elements
    """
    return soup.select(f'{parent} {child}')


def select_direct_children(soup, parent, child):
    """
    Select direct children using child combinator.
    
    Args:
        soup (BeautifulSoup): Parsed HTML
        parent (str): Parent selector
        child (str): Child selector
        
    Returns:
        list: List of matching elements
    """
    return soup.select(f'{parent} > {child}')


def main():
    """
    Main function to demonstrate CSS selector techniques.
    """
    url = "https://example.com"
    
    print(f"Scraping URL with CSS Selectors: {url}\n")
    
    soup = scrape_with_css_selectors(url)
    
    if soup:
        # Example 1: Select all paragraphs
        paragraphs = select_by_tag(soup, 'p')
        print(f"Found {len(paragraphs)} paragraph(s) using tag selector")
        
        # Example 2: Select all divs
        divs = select_by_tag(soup, 'div')
        print(f"Found {len(divs)} div(s) using tag selector")
        
        # Example 3: Select all links
        links = select_by_tag(soup, 'a')
        print(f"Found {len(links)} link(s)")
        if links:
            print("First link:")
            link = links[0]
            print(f"  Text: {link.text.strip()}")
            print(f"  URL: {link.get('href', 'N/A')}")
        
        # Example 4: Using attribute selectors
        print("\nDemonstration of CSS Selector Syntax:")
        print("  Tag selector: 'p' - selects all <p> elements")
        print("  Class selector: '.classname' - selects elements with class")
        print("  ID selector: '#idname' - selects element with specific ID")
        print("  Attribute selector: 'a[href]' - selects <a> with href attribute")
        print("  Descendant selector: 'div p' - selects <p> inside <div>")
        print("  Child selector: 'div > p' - selects direct <p> children of <div>")
    else:
        print("Failed to scrape the webpage.")


if __name__ == "__main__":
    main()
