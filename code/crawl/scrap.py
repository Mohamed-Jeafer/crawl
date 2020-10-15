
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pprint

chrome_browser = webdriver.Chrome('chromedriver.exe')

site = [
    {
        'site_name': 'cimaclub',
        'site_link': 'https://www.cimaclub.io/search/',
        'block': '.MovieBlock',
        'title_class': '.BoxTitle',
    },
    {
        'site_name': 'cimaflash',
        'site_link': 'https://cimaflash.me/?s=',
        'block': '.BlockItem',
        'title_class': '.TitleBlockMovieNormal',
    }
]


def make_asset_searchable(asset):
    splited_string = asset.split()
    capitalzied_string = []
    for i in splited_string:
        capitalzied_string.append(i.capitalize())
    joined_string = '+'.join(capitalzied_string)
    return joined_string


def parse_url(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    return soup


def scrap_url(site, asset):
    url_list = []
    for i, item in enumerate(site):
        parsed = parse_url(site[i]['site_link'] + make_asset_searchable(asset))
        video_class = parsed.select(site[i]['block'])
        for idx, item in enumerate(video_class):
            title_class = video_class[idx].select(site[i]['title_class'])
            href_element = video_class[idx].select('a')
            if len(href_element):
                link = href_element[0].get('href')
                title = title_class[0].getText()
                if asset in title:
                    url_list.append({'title': title, 'link': link, 'site_name': site[i]['site_name']})

    return url_list

def screenshot(url_list):
    chrome_browser.get(url_list[idx]['link'])
    chrome_browser.save_screenshot('screenshot.png')

asset = 'The Blacklist'
pprint.pprint(scrap_url(site, asset))
