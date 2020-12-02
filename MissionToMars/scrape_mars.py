import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    return Browser('chrome', **executable_path, headless=False)

def scrape_news():
    browser = init_browser()

    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    browser.visit(url)
    news = soup.find_all('div', class_='content_title')
    news[0]

    news_title = "MOXIE Could Help Future Rockets Launch Off Mars"
    news_p = "NASA's Perseverance rover carries a device to convert Martian air into oxygen that,if produced on a larger scale, could be used not just for breathing, but also for fuel."

    return news, news_p, news_title

def scrape_img():

    browser = init_browser()
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    browser.visit(url)

    img = soup.find_all('li', class_='slide')
    img[0]

    featured_img = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA17793_hires.jpg'

    return img, featured_img

def scrape_tables():

    factsurl = 'https://space-facts.com/mars/'
    tables = pd.read_html(factsurl)

    factsdf = tables[1]
    factshtml = factsdf.to_html()
    hemisphere_image_urls = [
    {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
]

    return factshtml, hemisphere_image_urls