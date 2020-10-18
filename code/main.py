from extract import get_search_site, get_screenshot, close_browser
from database_connection import get_scrap_detail

import requests
from bs4 import BeautifulSoup
import xlsxwriter
import collections
import pprint

# Get the information from the database
site, assets = get_scrap_detail()


# Parse the url to be select the required data
def parse_url(url):
    parsed = []
    for item in url:
        res = requests.get(item)
        soup = BeautifulSoup(res.text, 'html.parser')
        parsed.append(soup)
    return parsed


# Scrap the websites and save data into a list
def main(site, assets):
    url_list = []
    for idx_num in range(len(site)):  # Determine how many likes are there and number of iterations required
        parsed_list = parse_url(get_search_site(site[idx_num], assets))
        for parsed_url in parsed_list:  # Iterate over lists of parsed URLs
            video_class = parsed_url.select(site[idx_num]['block'])
            for idx, item3 in enumerate(video_class):  # iterate over the block of data selected from the parsed URL
                title_class = video_class[idx].select(site[idx_num]['title_class'])
                href_element = video_class[idx].select('a')
                if len(href_element):  # Checks if link exists
                    link = href_element[0].get('href')
                    title = title_class[0].getText()
                    for lst in assets:
                        for keyword in lst['keywords']:  # Iterate over list of keywords provided
                            if keyword in title.lower():  # .lower() is used to ignore capitalization
                                screenshot_path = get_screenshot(link, title)
                                # An ordered dictionary is required for saving the data in order in the excel file
                                ordered_dict = collections.OrderedDict()
                                ordered_dict['link'] = link
                                ordered_dict['ID_asset'] = lst['id']
                                ordered_dict['title'] = title
                                ordered_dict['extracted_from'] = site[idx_num]['site_name']
                                ordered_dict['screenshot_path'] = screenshot_path
                                url_list.append(ordered_dict)
                            else:
                                print(f'{keyword} was not found in {link}')
    save_to_excel_file(url_list)
    pprint.pprint(url_list)
    print(f'The total amount of items found is {len(url_list)}')
    close_browser()
    return url_list


# Writes the extracted data into Excel file
def save_to_excel_file(lst):
    workbook = xlsxwriter.Workbook('./database/data_extract.xlsx')
    worksheet = workbook.add_worksheet('sheet1')
    bold = workbook.add_format({'bold': 1})
    # Fixing the width of the column
    worksheet.set_column(0, 0, 40)
    worksheet.set_column(1, 1, 8)
    worksheet.set_column(2, 2, 40)
    worksheet.set_column(3, 3, 14)
    worksheet.set_column(4, 4, 40)
    row = 0
    col = 0
    for title in lst[0]:  # Iterate over the list key to write the table headers
        worksheet.write(row, col, title, bold)
        col += 1
    row += 1
    for item in lst:  # Insert the items in the list into its proper column
        col = 0
        values_lst = item.values()
        for value in values_lst:
            worksheet.write(row, col, value)
            col += 1
        row += 1
    workbook.close()


if __name__ == '__main__':
    main(site, assets)
