from crawl import get_search_site, get_screenshot
import requests
from bs4 import BeautifulSoup
import xlsxwriter
import collections
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
        'keywords': ['the blacklist', ]
    },
    {
        'id': '1',
        'name': 'Afili Ask',
        'keywords': ['Afili Ask ', 'الحب ورطة', ]
    }
]


def parse_url(url):
    parsed = []
    for item in url:
        res = requests.get(item)
        soup = BeautifulSoup(res.text, 'html.parser')
        parsed.append(soup)
    return parsed


def scrap_url(site, assets):
    url_list = []
    for idx_num in range(len(site)):
        parsed_list = parse_url(get_search_site(site[idx_num], assets))
        for parsed_url in parsed_list:
            video_class = parsed_url.select(site[idx_num]['block'])
            for idx, item3 in enumerate(video_class):
                title_class = video_class[idx].select(site[idx_num]['title_class'])
                href_element = video_class[idx].select('a')
                if len(href_element):
                    link = href_element[0].get('href')
                    title = title_class[0].getText()
                    for lst in assets:
                        for keyword in lst['keywords']:
                            if keyword in title.lower():
                                screenshot_path = get_screenshot(link, title)
                                ordered_dict = collections.OrderedDict()
                                ordered_dict['title'] = title
                                ordered_dict['link'] = link
                                ordered_dict['site_name'] = site[idx_num]['site_name']
                                ordered_dict['screenshot_path'] = screenshot_path
                                url_list.append(ordered_dict)
                            else:
                                print(f'{keyword} was not found in {link}')
    save_to_excel_file(url_list)
    return url_list


def save_to_excel_file(lst):
    workbook = xlsxwriter.Workbook('../database/data_extract.xlsx')
    worksheet = workbook.add_worksheet('sheet1')
    bold = workbook.add_format({'bold': 1})
    worksheet.set_column(0, 3, 40)
    row = 0
    col = 0
    for title in lst[0]:
        worksheet.write(row, col, title, bold)
        col += 1
    row += 1
    for item in lst:
        col = 0
        values_lst = item.values()
        for value in values_lst:
            worksheet.write(row, col, value)
            col += 1
        row += 1
    workbook.close()


pprint.pprint(scrap_url(site, assets))
