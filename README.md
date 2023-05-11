# scrap-qoute-game
program that scrap to get quotes and information about author, and game that will make you guess the author

Modules:
  scraping.py - scrap website (https://quotes.toscrape.com) ,gathering qoute text, name of the author, date and palce of author born and save it in csv file
  
  Quote.py - class that stores qoute text, name of the author, date and palce of author born and is able to give as a 3 clues - fierst letter of the author first name, first letter of the author second name, and date and place of atuhor born
  
  game.py - take qoutes and information about author form qoute.csv and make list of Qoute object form it, take one random qoute form it and make you quess who sad it. If you don't quess, it will give you a clues.
  
