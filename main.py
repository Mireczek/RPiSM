import random
import numpy

kostka1 = [1,2,6,7]
kostka2 = [3,4,4,8]
k = 4
liczbaWylosowanych = 50

def udawajZeLosujeszZRozkladu(kostka):
    rzuty = []
    for i in range(liczbaWylosowanych):
        wynik = 0
        for z in range(k):
            wynik += random.choice(kostka)
        rzuty.append(wynik)
    return rzuty

def testRownosciSrednich(srednia1, srednia2, wariancja1, wariancja2):
    mianownik = numpy.sqrt((wariancja1/liczbaWylosowanych)+(wariancja2/liczbaWylosowanych))
    return (srednia1 - srednia2)/mianownik

def testRownosciWariancji(wariancja1, wariancja2):
    return numpy.maximum(wariancja1,wariancja2)/numpy.minimum(wariancja1,wariancja2)

wylosowaneZRozkladuKostka1 = udawajZeLosujeszZRozkladu(kostka1)
wylosowaneZRozkladuKostka2 = udawajZeLosujeszZRozkladu(kostka2)

sredniaR1 = numpy.mean(wylosowaneZRozkladuKostka1)
sredniaR2 = numpy.mean(wylosowaneZRozkladuKostka2)

wariancjaR1 = numpy.var(wylosowaneZRozkladuKostka1)
wariancjaR2 = numpy.var(wylosowaneZRozkladuKostka2)

print("Średnia dla wylosowanych z rozkładu kostki 1 : " + str(sredniaR1))
print("Średnia dla wylosowanych z rozkładu kostki 2 : " + str(sredniaR2))

print("Wariancja dla wylosowanych z rozkładu kostki 1 : " + str(wariancjaR1))
print("Wariancja dla wylosowanych z rozkładu kostki 2 : " + str(wariancjaR2))

print("Test równości średnich : " + str(testRownosciSrednich(sredniaR1,sredniaR2,wariancjaR1,wariancjaR2)))
print("Test równości wariancji : " + str(testRownosciWariancji(wariancjaR1,wariancjaR2)))
