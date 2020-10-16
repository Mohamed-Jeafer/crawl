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
        'name': 'The Blacklist',
        'keywords': ['The Blacklist', ]
    },
    {
        'id': '1',
        'name': 'Afili Ask',
        'keywords': ['Afili Afili ', 'الحب ورطة', ]
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
        print(len(parsed))
    return parsed


def scrap_url(site, assets):
    url_list = []
    for idx_num in range(len(site)):
        print(f'length at the first loop{len(url_list)}')
        parsed_list = parse_url(get_search_site(site[idx_num], assets))
        for parsed_url in parsed_list:
            print(f'length at the second loop{len(url_list)}')
            video_class = parsed_url.select(site[idx_num]['block'])
            for idx, item3 in enumerate(video_class):
                print(f'length at the third loop{len(url_list)}')
                title_class = video_class[idx].select(site[idx_num]['title_class'])
                href_element = video_class[idx].select('a')
                if len(href_element):
                    link = href_element[0].get('href')
                    title = title_class[0].getText()
                    for lst in assets:
                        print(f'length at the fourth loop{len(url_list)}')
                        for keyword in lst['keywords']:
                            if keyword in title:
                                url_list.append({'title': title, 'link': link, 'site_name': site[idx_num]['site_name']})
                                get_screenshot(link, title)
    return url_list


# asset = 'The Blacklist'
pprint.pprint(scrap_url(site, assets))
