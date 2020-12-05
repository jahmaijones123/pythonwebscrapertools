import requests
from bs4 import BeautifulSoup


url = requests.get('https://techcrunch.com/?guccounter=2')
        
soup = BeautifulSoup(url.content, 'html.parser')

links = soup.find_all('a')

for link in links:
    if 'href' in link.attrs: #if there is a link in the href attribute 

        print('Starting Search....')

        print(str(link.attrs['href']) + "\n") #printing the link 
