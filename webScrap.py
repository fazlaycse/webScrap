import requests
import re
from bs4  import BeautifulSoup

url='https://oxylabs.io/blog/python-web-scraping-tutorial';
response= requests.get(url)
soup=BeautifulSoup(response.text,'html.parser')
#print(response.text) 
## command###### py -m pip install requests
##### py -m pip install beautifulsoup4
##print(soup.title)
#print(soup.find_all)
'''blog_titles = soup.find_all('a', class_='e1dscegp1')
for title in blog_titles:
    print(title.text)'''
blog_titles = soup.find_all('a', class_=re.compile('oxy-rmqaiq'))
for title in blog_titles:
    print(title.text)