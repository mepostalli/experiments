import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"

html = requests.get(url).content

soup = BeautifulSoup(html,'html.parser')
list = soup.find('tbody', {"class":"lister-list"}).find_all("tr" )
count = 1
for tr in list:
    title = tr.find('td', {"class":"titleColumn"}).find('a').text
    year = tr.find('span', {"class":"secondaryInfo"}).text.strip("()")
    rating = tr.find('td', {"class":"ratingColumn imdbRating"}).text.strip()
    
    print(f"{count} - film: {title.ljust(50)} yıl : {year} puan : {rating}")   
    count += 1
    


