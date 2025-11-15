"""
Local HTML Scraping Demo
This script demonstrates web scraping using a local HTML file,
so you can test the functionality without internet access.
"""

from bs4 import BeautifulSoup


# Sample HTML content
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="A sample page for web scraping demonstration">
    <meta name="keywords" content="web scraping, python, beautifulsoup">
    <title>Sample Page for Web Scraping</title>
</head>
<body>
    <header>
        <h1>Welcome to Web Scraping Tutorial</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/contact">Contact</a>
            <a href="https://github.com" class="external">GitHub</a>
        </nav>
    </header>
    
    <main>
        <section id="intro">
            <h2>Introduction to Web Scraping</h2>
            <p>Web scraping is the process of extracting data from websites. 
            It's a powerful technique used for data mining, research, and automation.</p>
            <p>This page demonstrates various HTML elements that can be scraped.</p>
        </section>
        
        <section id="technologies">
            <h2>Technologies We Use</h2>
            <ul>
                <li class="tech-item">Python</li>
                <li class="tech-item">Requests</li>
                <li class="tech-item">BeautifulSoup</li>
                <li class="tech-item">lxml</li>
            </ul>
        </section>
        
        <section id="data-table">
            <h2>Sample Data Table</h2>
            <table border="1">
                <thead>
                    <tr>
                        <th>Library</th>
                        <th>Purpose</th>
                        <th>Version</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Requests</td>
                        <td>HTTP Requests</td>
                        <td>2.31.0</td>
                    </tr>
                    <tr>
                        <td>BeautifulSoup4</td>
                        <td>HTML Parsing</td>
                        <td>4.12.0</td>
                    </tr>
                    <tr>
                        <td>lxml</td>
                        <td>Fast Parser</td>
                        <td>4.9.0</td>
                    </tr>
                </tbody>
            </table>
        </section>
        
        <section id="images">
            <h2>Images</h2>
            <img src="/images/scraping.png" alt="Web Scraping Diagram" title="How Web Scraping Works">
            <img src="/images/python.png" alt="Python Logo" title="Python Programming Language">
        </section>
        
        <section id="articles">
            <h2>Recent Articles</h2>
            <article>
                <h3>Getting Started with BeautifulSoup</h3>
                <p class="date">Posted on: 2024-01-15</p>
                <p>Learn how to parse HTML documents using BeautifulSoup library.</p>
                <a href="/article/1">Read more</a>
            </article>
            <article>
                <h3>Advanced Scraping Techniques</h3>
                <p class="date">Posted on: 2024-01-20</p>
                <p>Discover advanced techniques for handling dynamic content and pagination.</p>
                <a href="/article/2">Read more</a>
            </article>
        </article>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2024 Web Scraping Tutorial. All rights reserved.</p>
        <div id="social">
            <a href="https://twitter.com/example">Twitter</a>
            <a href="https://linkedin.com/example">LinkedIn</a>
        </div>
    </footer>
</body>
</html>
"""


def demo_basic_parsing():
    """Demonstrate basic HTML parsing."""
    print("=" * 60)
    print("1. BASIC PARSING")
    print("=" * 60)
    
    soup = BeautifulSoup(HTML_CONTENT, 'lxml')
    
    # Get title
    title = soup.find('title')
    print(f"Page Title: {title.text}")
    
    # Get main heading
    h1 = soup.find('h1')
    print(f"Main Heading: {h1.text}")
    print()


def demo_find_methods():
    """Demonstrate find and find_all methods."""
    print("=" * 60)
    print("2. FIND METHODS")
    print("=" * 60)
    
    soup = BeautifulSoup(HTML_CONTENT, 'lxml')
    
    # Find all h2 headings
    h2_tags = soup.find_all('h2')
    print(f"All H2 headings ({len(h2_tags)}):")
    for h2 in h2_tags:
        print(f"  - {h2.text}")
    print()
    
    # Find all paragraphs
    paragraphs = soup.find_all('p', limit=3)
    print(f"First 3 paragraphs:")
    for i, p in enumerate(paragraphs, 1):
        print(f"  {i}. {p.text[:60]}...")
    print()


def demo_css_selectors():
    """Demonstrate CSS selectors."""
    print("=" * 60)
    print("3. CSS SELECTORS")
    print("=" * 60)
    
    soup = BeautifulSoup(HTML_CONTENT, 'lxml')
    
    # Select by ID
    intro = soup.select('#intro')
    print(f"Section with id='intro': {intro[0].h2.text}")
    
    # Select by class
    tech_items = soup.select('.tech-item')
    print(f"\nTechnologies (class='tech-item'):")
    for item in tech_items:
        print(f"  - {item.text}")
    
    # Select nested elements
    nav_links = soup.select('nav a')
    print(f"\nNavigation links ({len(nav_links)}):")
    for link in nav_links:
        print(f"  - {link.text}: {link.get('href')}")
    print()


def demo_table_scraping():
    """Demonstrate table scraping."""
    print("=" * 60)
    print("4. TABLE SCRAPING")
    print("=" * 60)
    
    soup = BeautifulSoup(HTML_CONTENT, 'lxml')
    
    # Find the table
    table = soup.find('table')
    
    # Extract headers
    headers = [th.text for th in table.find('thead').find_all('th')]
    print(f"Table Headers: {' | '.join(headers)}")
    print("-" * 60)
    
    # Extract rows
    rows = table.find('tbody').find_all('tr')
    for row in rows:
        cells = [td.text for td in row.find_all('td')]
        print(' | '.join(cells))
    print()


def demo_links_and_images():
    """Demonstrate extracting links and images."""
    print("=" * 60)
    print("5. LINKS AND IMAGES")
    print("=" * 60)
    
    soup = BeautifulSoup(HTML_CONTENT, 'lxml')
    
    # Extract all links
    all_links = soup.find_all('a')
    print(f"Total links found: {len(all_links)}")
    print("\nInternal links:")
    for link in all_links:
        href = link.get('href', '')
        if href.startswith('/'):
            print(f"  - {link.text}: {href}")
    
    print("\nExternal links:")
    for link in all_links:
        href = link.get('href', '')
        if href.startswith('http'):
            print(f"  - {link.text}: {href}")
    
    # Extract all images
    images = soup.find_all('img')
    print(f"\nTotal images found: {len(images)}")
    for img in images:
        print(f"  - {img.get('alt')}: {img.get('src')}")
    print()


def demo_attributes():
    """Demonstrate accessing attributes."""
    print("=" * 60)
    print("6. ACCESSING ATTRIBUTES")
    print("=" * 60)
    
    soup = BeautifulSoup(HTML_CONTENT, 'lxml')
    
    # Get meta tags
    meta_tags = soup.find_all('meta')
    print("Meta tags:")
    for meta in meta_tags:
        if meta.get('name'):
            print(f"  {meta.get('name')}: {meta.get('content')}")
    
    # Get external links
    external_link = soup.find('a', class_='external')
    if external_link:
        print(f"\nExternal link class: {external_link.get('class')}")
        print(f"External link href: {external_link.get('href')}")
    print()


def demo_navigating_tree():
    """Demonstrate navigating the HTML tree."""
    print("=" * 60)
    print("7. NAVIGATING THE HTML TREE")
    print("=" * 60)
    
    soup = BeautifulSoup(HTML_CONTENT, 'lxml')
    
    # Get first article
    article = soup.find('article')
    
    print("First article structure:")
    print(f"  Article heading: {article.h3.text}")
    print(f"  Date: {article.find('p', class_='date').text}")
    
    # Get next sibling (next article)
    next_article = article.find_next_sibling('article')
    if next_article:
        print(f"  Next article: {next_article.h3.text}")
    
    # Get parent
    section = article.parent
    print(f"  Parent section ID: {section.get('id')}")
    print()


def main():
    """Run all demonstrations."""
    print("\n")
    print("*" * 60)
    print("  LOCAL HTML WEB SCRAPING DEMONSTRATION")
    print("*" * 60)
    print("\nThis demo shows various web scraping techniques")
    print("using BeautifulSoup on a local HTML sample.\n")
    
    demo_basic_parsing()
    demo_find_methods()
    demo_css_selectors()
    demo_table_scraping()
    demo_links_and_images()
    demo_attributes()
    demo_navigating_tree()
    
    print("=" * 60)
    print("DEMONSTRATION COMPLETE!")
    print("=" * 60)
    print("\nAll examples show core web scraping techniques that work")
    print("the same way with real websites (using requests library).")
    print("\nCheck out the other examples in the 'examples/' directory")
    print("for more advanced techniques and real-world scenarios.")
    print()


if __name__ == "__main__":
    main()
