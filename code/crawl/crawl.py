from selenium import webdriver, common
import time

chrome_browser = webdriver.Chrome('chromedriver.exe')

# video_source_url = ''
# extracted_from = chrome_browser.xp
# screenshot_path = chrome_browser.save_screenshot('screenshot.png')

url_list = [{'title': 'title', 'link': 'link', 'site_name': 'site[i][''site_name'']'}]


def get_search_site(site, assets):
    search_site = []
    for item in assets:
        for i in item['keywords']:
            chrome_browser.get(site['site_link'])
            search_button = chrome_browser.find_element_by_class_name(site['search_button_class'])
            search_box = chrome_browser.find_element_by_id(site['search_box_id'])
            search_box.send_keys(i)
            search_button.click()
            search_site.append(chrome_browser.current_url)
    print(search_site)
    return search_site


def get_screenshot(link, title):
    chrome_browser.get(link)
    chrome_browser.save_screenshot(f'../screenshots/{title}.png')



