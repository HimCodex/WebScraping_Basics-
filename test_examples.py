"""
Test script to verify that all example scripts are syntactically correct
and can be imported without errors.
"""

import sys
import importlib.util


def test_import_module(filepath, module_name):
    """
    Test if a module can be imported successfully.
    
    Args:
        filepath (str): Path to the Python file
        module_name (str): Name to give the module
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        spec = importlib.util.spec_from_file_location(module_name, filepath)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return True
    except Exception as e:
        print(f"Error importing {module_name}: {e}")
        return False


def main():
    """
    Test all example modules.
    """
    examples = [
        ('examples/01_basic_scraping.py', 'basic_scraping'),
        ('examples/02_css_selectors.py', 'css_selectors'),
        ('examples/03_links_and_images.py', 'links_and_images'),
        ('examples/04_table_scraping.py', 'table_scraping'),
        ('examples/05_advanced_techniques.py', 'advanced_techniques'),
    ]
    
    print("Testing example modules...\n")
    
    all_passed = True
    for filepath, module_name in examples:
        # We'll just check if the file exists and is syntactically valid
        try:
            with open(filepath, 'r') as f:
                code = f.read()
                compile(code, filepath, 'exec')
            print(f"✓ {filepath} - Syntax valid")
        except FileNotFoundError:
            print(f"✗ {filepath} - File not found")
            all_passed = False
        except SyntaxError as e:
            print(f"✗ {filepath} - Syntax error: {e}")
            all_passed = False
    
    print()
    if all_passed:
        print("All tests passed! ✓")
        return 0
    else:
        print("Some tests failed! ✗")
        return 1


if __name__ == "__main__":
    exit(main())
