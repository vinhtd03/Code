import requests
from bs4 import BeautifulSoup as bs

url= 'https://dantri.com.vn/the-thao.htm'

response = requests.get(url)

soup = bs(response.content, "html.parser")

titles = soup.find_all('a',{'data-content-name' : 'category-children'})

for title in titles:
    print(title.text)



