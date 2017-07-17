from bs4 import BeautifulSoup
import requests
import csv


#retrieve page html
def extract_source(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    source=requests.get(url, headers=headers)
    return source


source = extract_source("http://www.allmusic.com/style/shoegaze-ma0000004454/albums")


soup = BeautifulSoup(source.content, 'html.parser')
albums =soup.find_all(class_="info")

with open("test.csv", "w") as out:
    header = ["Artist","Album"]
    writer = csv.writer(out)
    
    writer.writerow(header)
    
    for i in range(0, len(albums)):
        line = [albums[i].find(class_="artist").get_text().strip(),albums[i].find(class_="title").get_text().strip()]
        writer.writerow(line)
        print("%s" % (line))
    

