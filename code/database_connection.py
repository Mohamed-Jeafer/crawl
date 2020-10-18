import pymysql


# Function to retrieve data from a given query
def get_data_from_db(query):
    # Database Configuration
    endpoint = 'assignment.ch1o2xbrlqqq.us-east-1.rds.amazonaws.com'
    username = 'admin'
    password = 'password1234'
    database_name = 'assignment'

    # Establishing connection
    connection = pymysql.Connect(endpoint, user=username, passwd=password, db=database_name, charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Read from new record
            cursor.execute(query)
            result = cursor.fetchall()
    finally:
        pass  # connection.close()
    return result


def get_scrap_detail():
    # Query to get the website URLs
    site_link = get_data_from_db("select website_name from website_name")
    site = [
        {
            'site_name': 'cimaclub',
            'site_link': site_link[0]['website_name'],
            'block': '.MovieBlock',  # CSS class on the website that holds the needed information
            'title_class': '.BoxTitle',  # CSS class that refers to the asset title
            'search_box_xpath': '/html/body/div[1]/div[1]/form/input',  # Search Box Xpath
            'search_button_xpath': '/html/body/div[1]/div[1]/form/button',  # search button xpath
            'search_box_id': 'SearchingInput',  # CSS id element for the search text box
            'search_button_class': 'ion-md-search',  # CSS class in the button
        },
        {
            'site_name': 'cimaflash',
            'site_link': site_link[1]['website_name'],
            'block': '.BlockItem',
            'title_class': '.TitleBlockMovieNormal',
            'search_box_xpath': '/html/body/div[3]/h2/div[3]/form/input',
            'search_button_xpath': '/html/body/div[3]/h2/div[3]/form/button/i',
            'search_box_id': 's',
            'search_button_class': 'fa-search',
        }
    ]
    asset_name = get_data_from_db("select * from assets")
    keyword = get_data_from_db("select keyword from keywords")
    assets = [
        {
            'id': asset_name[0]['ID_asset'],
            'asset_name': asset_name[0]['asset_name'],
            'keywords': [keyword[0]['keyword'], keyword[1]['keyword']]
        },
        {
            'id': asset_name[1]['ID_asset'],
            'asset_name': asset_name[1]['asset_name'],
            'keywords': [keyword[2]['keyword']]
        },
    ]
    return site, assets


get_scrap_detail()
