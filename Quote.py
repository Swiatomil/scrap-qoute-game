class Quote:
    def __init__(self, cytat, tworca, data):
        self.cytat = cytat
        self.tworca = tworca
        self.data = data
    def daj_pierwsza_podpowiedz(self):
        print(f"author of that quote was born in {self.data}")
    def daj_druga_podpowiedz(self):
        print(f"the first name of author begin with {self.tworca[0]}")
    def daj_trzecia_podpowiedz(self):
        a=0
        for letter in self.tworca:
           a +=1
           if letter == " ":
               break
        print(f"the second name of author begin with {self.tworca[a]}")



