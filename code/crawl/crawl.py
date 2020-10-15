from selenium import webdriver
import scrap
import time

chrome_browser = webdriver.Chrome('chromedriver.exe')

asset_id1 = 'Afili Ask'
asset_id2 = 'The Blacklist'

# video_source_url = ''
# extracted_from = chrome_browser.xp
# screenshot_path = chrome_browser.save_screenshot('screenshot.png')

url_list = [{'title': 'title', 'link': 'link', 'site_name': 'site[i][''site_name'']'}]


def search_site(url_list):
    for idx, url in enumerate(site):
        url = url_list[idx]['link']
        chrome_browser.get(url)
        chrome_browser.save_screenshot('screenshot.png')


search_site(url_list)
