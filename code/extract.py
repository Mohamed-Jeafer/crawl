from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

chrome_options = webdriver.ChromeOptions()

# Ads blocker extension is added to prevent ads from causing errors
path_to_extension = os.path.abspath('./3.9.5_0')
chrome_options.add_argument("load-extension=" + path_to_extension)

chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')  ## Applicable to windows only

# ChromeDriverManager allows driver to run on multiple os
chrome_browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
chrome_browser.implicitly_wait(10)


def close_browser():
    chrome_browser.quit()


# Searches the given URLs for the assets provided
def get_search_site(site, assets):
    search_site = []
    for item in assets:
        for i in item['keywords']:
            try:
                # Try to get the elements by class and id
                chrome_browser.get(site['site_link'])
                search_button = chrome_browser.find_element_by_class_name(site['search_button_class'])
                search_box = chrome_browser.find_element_by_id(site['search_box_id'])
                search_box.send_keys(i)  # i is the keyword in the assets provided
                search_button.click()
                search_site.append(chrome_browser.current_url)
            except (NoSuchElementException, ElementClickInterceptedException) as ex:  # Handle the error
                continue  # If the element was not clickable, it will try again
    return search_site


# Takes a screenshot of every link it receives, then saves it using the title of the page
def get_screenshot(link, title):
    chrome_browser.get(link)
    chrome_browser.save_screenshot(f'./screenshots/{title}.png')
    return f'./screenshots/{title}.png'
