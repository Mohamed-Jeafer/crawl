import xlsxwriter

url_list = [
    {
        'title': 'some title',
        'video_source': 'some source',
        'screenshot_path': 'path',
        'extracted_from': 'website name',
    },
    {
        'title': 'title_1',
        'video_source': 'video_source_1',
        'screenshot_path': 's_p1',
        'extracted_from': 'ext_from1',
    },
    {
        'title': '2',
        'video_source': '2',
        'screenshot_path': '2',
        'extracted_from': '2',
    },
]

for item in url_list[0]:
    print(item)


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

save_to_excel_file(url_list)
