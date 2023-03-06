from Quote import Quote
from csv import reader
from pyfiglet import Figlet
from termcolor import colored
from random import randint


end = 1
book_of_quote = []
with open("qoute.csv" , newline='') as plik:
    csvv = reader(plik)
    csvv.__next__()
    for q in csvv:
        book_of_quote.append(Quote(q[0],q[1],q[2]))
hello= Figlet()
print(colored(hello.renderText("zgaduj zgadula!"),"green"))
#print(len(book_of_quote))
while(end):
    cytat = book_of_quote.pop(randint(0, len(book_of_quote)-1))
    print(cytat.cytat)
    gues = input("who said this? \n")
    if gues != cytat.tworca:
        cytat.daj_pierwsza_podpowiedz()
        gues = input("who said this? \n")
        if gues != cytat.tworca:
            cytat.daj_druga_podpowiedz()
            gues = input("who said this? \n")
            if gues != cytat.tworca:
                cytat.daj_trzecia_podpowiedz()
                gues = input("who said this? \n")
                if gues != cytat.tworca:
                    if input(f"Unfortunetly No, this is quote of {cytat.tworca} do you wanna play again? y/n \n ") == "n": end = 0
                else:
                    if input("Bravo! cdo you wanna play again? y/n \n") == "n": end = 0
            else:
                if input("Bravo! cdo you wanna play again? y/n \n") == "n": end = 0
        else:
            if input("Bravo! do you wanna play again? y/n \n") == "n": end = 0
    else:
        if input("Bravo! do you wanna play again? y/n \n") == "n": end=0






