import os #lets me change directiores and make folders
import requests
from bs4 import BeautifulSoup

print ('Starting Search....') #prints to the terminal

url = 'https://www.imdb.com/chart/top/' #paste URL of site you want to crawl

def imagedown(url, folder): #where we will save the downloaded images
    #basic error handling
    try:
        os.mkdir(os.path.join(os.getcwd(), folder)) #join current pwd and the new folder were creating
    except:
        pass
    os.chdir(os.path.join(os.getcwd(), folder)) #change directory 
    
    r = requests.get(url) #requests the url from the IMDB server
    soup = BeautifulSoup(r.text, 'html.parser') # parses the html to be understood by Python
    images = soup.find_all('img') #finds all html tags with img

    for image in images: 

        name = image ['alt'] #include the information in the alt html which is important for SEO 
        link = image ['src'] #search the html only for the links within the img src tag 

        with open(name.replace(' ', '-').replace('/', '').replace('|', '').replace('*', '').replace('"', '') + '.jpg', 'wb') as f:  #writing to a file, opening it and saving it

            im = requests.get(link) 
            f.write (im.content) #saving the bytes content 
            print('writing', name)

imagedown('https://www.imdb.com/chart/top/' , '2021 Movies') #calls the imagedown function 
