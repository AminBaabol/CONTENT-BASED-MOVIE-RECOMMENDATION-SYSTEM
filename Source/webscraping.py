import time
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def web_scrap_imdb_site():
    pages = 1
    movies_data =[]
    cast = []
    while(pages < 13):
        try:
            # Movie title
            all_header_information = driver.find_elements_by_class_name('lister-item-header')
        except NoSuchElementException:
            print('I TOOK AN L')
        try:
            # 9.3 stars
            all_ratings_info = driver.find_elements_by_class_name('ratings-bar')
        except NoSuchElementException:
            print('I TOOK AN L')
        try:
            # Rated R, PG-13
            content_ratings = driver.find_elements_by_class_name('certificate')
        except NoSuchElementException:
            print('I TOOK AN L')
        try:
            # Genre
            movie_genre = driver.find_elements_by_class_name('genre')
        except NoSuchElementException:
            print('I TOOK AN L')
        try:
            # Box office gross
            box_office = driver.find_elements_by_class_name('sort-num_votes-visible')
        except NoSuchElementException:
            print('I TOOK AN L')
        try:
            # Movie runtime
            run_time = driver.find_elements_by_class_name('runtime')
        except NoSuchElementException:
            print('I TOOK AN L')
        #try:
            # Notable stars
            #stars = driver.find_elements_by_class_name('')
            #print('stars ', len(stars))
        #except NoSuchElementException:
            #print('I TOOK AN L')
        #print("hey")
        """
        elems = driver.find_elements_by_xpath("//a[@href]")
        res = []
        for elem in elems:
            res.append(res)
        cast.append(res)
        """
        try:
            # Movie runtime
            stars_search = driver.find_elements_by_class_name('lister-item-content')
        except NoSuchElementException:
            print('I TOOK AN L')

        
        for (header_info, all_ratings_info, content_ratings, movie_genre, box_office, run_time, stars_search) in zip(all_header_information, all_ratings_info, content_ratings, movie_genre, box_office, run_time, stars_search):
             current_star = stars_search.find_elements_by_tag_name('p')
             movies_data.append({
                 "Movie title": header_info.text,
                 "Movie Rating": all_ratings_info.text,
                 "Genre": movie_genre.text,
                 "Box Office": box_office.text,
                 "Run Time": run_time.text,
                 "Stars": current_star[2].text
             })
        try:
            next_button = driver.find_element_by_class_name('lister-page-next.next-page')
            next_button.click()
        except NoSuchElementException:
            print('No Pages')
        pages += 1
        time.sleep(3)
    return(movies_data, cast)


# Path I have the chrome driver on my labtop
PATH = "/Users/aminbaabol/Desktop/chromeDriver"

# instantiating the Driver (gives me access to all the functionality webdriver has)
driver = webdriver.Chrome(PATH)

# opens Url
driver.get("https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating")

results, cast_data =  web_scrap_imdb_site()

myData = pd.DataFrame(results)
myData.to_excel('films_data.xlsx')


starsData = pd.DataFrame(cast_data)
starsData.to_excel('cast.xlsx')

driver.quit()

"""
Movie Content Rating (PG-13, R, etc)  DONE
Movei Rating Stars (9.3, 9.0)      DONE
Movie Genre                      DONE
Release Year    DONE
Grosss $$$ - Box Office         DONE
Titile                            DONE
Length of Movie- Runtime        DONE
Notable Actors - Stars          comeback to it later!
"""