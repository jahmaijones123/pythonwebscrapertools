import requests  #installs get requests 
from bs4 import BeautifulSoup #installs bs4
import pandas as pd
import time


main_list = [] #list is added here

def extract(url):

    headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    r = requests.get(url , headers=headers) #headers = headers specifies r and sends the user agent with the request 
    soup = BeautifulSoup(r.content , 'html.parser')
    return soup.find_all('div', class_ = 'row businessCapsule--mainRow') #searches the html for a div with class business capsule
    #soup.find_all will return a list 

def transform(articles):


    for item in articles: #loops through the list 
        name = item.find('span' , class_ = "businessCapsule--name").text 

        address = item.find('span' , {'itemprop' : 'address'}).text.strip().replace('\n', '') # text.strip removes the whitespace in between searches 

        try:
            website = item.find('a' , class_ = 'btn btn-yellow businessCapsule--ctaItem')['href'] #specifically look for the a href tag
        except:
            website = ''
        

        try:
            phone = item.find('span' , class_ = 'business--telephoneNumber').text
        except:
            phone = ''
        
        business = {

            'name' : name,
            'phone' : phone,
            'address' : address,
            'website' : website,

        }

        main_list.append(business) #creates a list from business
    return 

def load():

    df = pd.DataFrame(main_list) #loads main list into a data frame
    df.to_csv('businessleadgeneration.csv' , index=False) #index is equal to false makes sure the data frame has its own index to start from what i have collected



for x in range (1,11): #loops through each page
    print(f'Scanning Page {x} Please Wait....')
    articles = extract(f'https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=1215529652&keywords=resteraunt&location=birmingham&pageNum={x}') # everytime extracts loops through it will use x as the page number    
    transform(articles)
    time.sleep(5) #timer to delay each search, if it goes to fast the server will block my IP

load()
print('Saved to CSV')

