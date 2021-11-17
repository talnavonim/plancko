from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.10bis.co.il/next/restaurants/menu/delivery/19156/%D7%90%D7%A8%D7%A7%D7%A4%D7%94').text
soup = BeautifulSoup(source, 'lxml')

print(soup.prettify())