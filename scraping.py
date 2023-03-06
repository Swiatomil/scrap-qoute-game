from bs4 import BeautifulSoup
import requests
from Quote import Quote
from csv import writer

url = 'https://quotes.toscrape.com'
next = url
book_of_quotes= []

suf_url=""

while(True):
    next = url + suf_url
    site = requests.get(next)
    soup = BeautifulSoup(site.text, "html.parser")

    quotes = soup.select('.quote')
    for qoute_soup in quotes:

        quote_text = qoute_soup.find(class_="text").text
        qoute_author = qoute_soup.find(class_="author").text
        url_author = url + qoute_soup.find("a")['href']  # dostaje link do autora
        site_author = requests.get(url_author)  # pobieram zawartos linku
        soup_author = BeautifulSoup(site_author.text, "html.parser")  # robimy z niego zupe
        born = soup_author.find(class_="author-born-date").text + " " + soup_author.find(class_="author-born-location").text  # znajdujemy date
        book_of_quotes.append(Quote(quote_text, qoute_author, born))  # zapsujemy znalezione informacje
    suf = soup.select(".next")
    if not suf:
        break
    suf_url = suf[0].find("a")['href'] # wybieramy wszystkie klasy next, jest jedna dlatego wybieramy zerowy element, nastepnie z a dostajemy sie do argumentu href pod ktorym jest link
#print (book_of_quotes[79].cytat)
with open("qoute.csv", "w", newline='') as plik:
    cytaty = writer(plik)
    cytaty.writerow(["cytat", "autor", "urodzenie"])
    for quote in book_of_quotes:
        try:
            cytaty.writerow([quote.cytat, quote.tworca, quote.data])
        except:
            pass









