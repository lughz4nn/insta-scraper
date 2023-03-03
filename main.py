#By: Lughz4nn

import time, warnings
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

print('\nStarting the web scraping\n')

#########     CONFIG   ####################
###########################################3
warnings.filterwarnings("ignore", category=Warning)
chrome_options = Options()
chrome_options.add_argument("--headless")#FOR HIDDEN EXECUTE
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
path_webdriver = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=path_webdriver, options=chrome_options)
############################################


def scrap_data():

    username = input('Type the username: ').lower()

    driver.get('https://instagram.com/'+username)

    time.sleep(2)

    html_document = driver.page_source

    driver.quit()

    user_data = {}

    soup = BeautifulSoup(html_document,'html.parser')

    user_data['name'] = soup.find('span', {'class':'_aacw'}).text

    try:
        user_data['biography'] = soup.find('h1', {'class':'_aacu'}).text.strip('\n')
    except AttributeError:
        exit('\nThis username does not exist\n')

    try:
        user_data['picture_url'] = soup.find('img', {'class':'_aadp'})['src']
    except TypeError:
        user_data['picture_url'] = None
 
    instagram_basic_data = soup.find_all('span', {'class':'_ac2a'})

    user_data['posts'] = instagram_basic_data[0].text
    user_data['followers'] = instagram_basic_data[1].text
    user_data['following'] = instagram_basic_data[2].text

    return user_data

def show_data(data):

    print(f'''
    Name: {data['name']}
    Bio: {data['biography']}
    Posts: {data['posts']}
    Followers: {data['followers']}
    Following: {data['following']}
    Picture URL: {data['picture_url']}
    ''')


if __name__ == '__main__':

    data = scrap_data()

    show_data(data)
