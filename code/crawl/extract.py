from selenium import webdriver

chrome_browser = webdriver.Chrome('chromedriver.exe')
chrome_browser.maximize_window()


# Searches the given URLs for the assets provided
def get_search_site(site, assets):
    search_site = []
    for item in assets:
        for i in item['keywords']:
            chrome_browser.get(site['site_link'])
            search_button = chrome_browser.find_element_by_class_name(site['search_button_class'])
            search_box = chrome_browser.find_element_by_id(site['search_box_id'])
            search_box.send_keys(i)  # i is the keyword in the assets provided
            search_button.click()
            search_site.append(chrome_browser.current_url)
    print(search_site)
    return search_site


# Takes a screenshot of every link it receives, then saves it using the title of the page
def get_screenshot(link, title):
    chrome_browser.get(link)
    chrome_browser.save_screenshot(f'../screenshots/{title}.png')
    return f'../screenshots/{title}.png'
