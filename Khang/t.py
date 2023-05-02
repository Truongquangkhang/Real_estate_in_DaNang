from bs4 import BeautifulSoup
import requests
url = "https://alonhadat.com.vn/can-ban-nha-da-nang-t3/trang-2.htm"
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup)