import random #pip install randoms
import requests # pip install requests 

from bs4 import BeautifulSoup # pip install bs4

url = 'https://www.imdb.com/chart/top' #url we want to crawl and scrape for data

def main(): #function which runs 
    response = requests.get(url)
    html = response.text    
    soup = BeautifulSoup(html, 'html.parser') #makes the html readable for python
    movietags = soup.select('td.titleColumn') #selects the title tags
    inner_movietags = soup.select('td.titleColumn a') #selects the a in href html from the whole website 
    rating_tags = soup.select('td.posterColumn span[name=ir]') #selects the rating tag
    
    def get_year(movie_tag): #this function applies to the previous function
        moviesplit = movie_tag.text.split() #splits when any whitespace is found / splits into a string 
        year = moviesplit [-1] #removes the 1.
        return year
    
    years = [get_year(tag) for tag in movietags] # gets the year in every movie
    actors_list = [tag['title'] for tag in inner_movietags] # gets the names of the actors in every movie
    titles = [tag.text for tag in inner_movietags] # gets the names of titles in every movie
    ratings = [float (tag ['data-value']) for tag in rating_tags] # gets the rating tag in every movie and the value within that is read as a string and converts it into a float instead of string

    n_movies = len (titles) #gets the length of titles and number of movies by random choice

    


    while(True):
        index = random.randrange(0,n_movies) # this will select by random a number of moveis and return an integer 
        print(f'{titles [index]} {years[index]}, rating: {ratings[index]:.1f}, starring: {actors_list[index]}') 
        # prints to the screen each selection from the index at random 

        user_input = input ('Do you want another choice of movie to watch, there is a choice out of 250 films ? (y/[n])? ') # asks the user for their input

        if user_input != 'y': #if the user says no then quit the program
            break 

    
if __name__ == '__main__': #executes only if run as a script
    main()
