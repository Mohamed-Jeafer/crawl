from crawl import get_search_site, get_screenshot
import requests
from bs4 import BeautifulSoup
import pprint


site = [
    {
        'site_name': 'cimaclub',
        'site_link': 'https://www.cimaclub.io/',
        'block': '.MovieBlock',
        'title_class': '.BoxTitle',
        'search_box_id': 'SearchingInput',
        'search_button_class': 'ion-md-search',
    },
    {
        'site_name': 'cimaflash',
        'site_link': 'https://cimaflash.me/',
        'block': '.BlockItem',
        'title_class': '.TitleBlockMovieNormal',
        'search_box_id': 's',
        'search_button_class': 'fa-search'
    }
]

assets = [
    {
        'id': '2',
        'name': 'the blacklist',
        'keywords': ['the blacklist', ]
    },
    {
        'id': '1',
        'name': 'afili aşk',
        'keywords': ['afili ask ', 'الحب ورطة', ]
    }
]

# for item in assets:
#     for i in item['keywords']:
#         print (i)

# print(assets[0]['keywords'][0])

#
# def make_asset_searchable(asset):
#     splited_string = asset.split()
#     capitalzied_string = []
#     for i in splited_string:
#         capitalzied_string.append(i.capitalize())
#     joined_string = '+'.join(capitalzied_string)
#     return joined_string


def parse_url(url):
    parsed = []
    for item in url:
        res = requests.get(item)
        soup = BeautifulSoup(res.text, 'html.parser')
        parsed.append(soup)
    return parsed


def scrap_url(site, assets):
    url_list = []
    for i, item1 in enumerate(site):
        parsed = parse_url(get_search_site(site[i], assets))
        for item2 in parsed:
            video_class = item2.select(site[i]['block'])
            for idx, item3 in enumerate(video_class):
                title_class = video_class[idx].select(site[i]['title_class'])
                href_element = video_class[idx].select('a')
                if len(href_element):
                    link = href_element[0].get('href')
                    title = title_class[0].getText()
                    for item4 in assets:
                        for i2 in item4['keywords']:
                            if i2 in title:
                                url_list.append({'title': title, 'link': link, 'site_name': site[i]['site_name']})
                                get_screenshot(link, title)
    return url_list


# asset = 'The Blacklist'
pprint.pprint(scrap_url(site, assets))
