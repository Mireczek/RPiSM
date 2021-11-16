import random
import numpy

kostka1 = [1,2,6,7]
kostka2 = [3,4,4,8]
k = 4
liczbaRzutow = 50

def rzucaj(kostka):
    rzuty = []
    for i in range(liczbaRzutow):
        rzuty.append(random.choice(kostka))
    return rzuty

def sumujRzuty(kostka):
    wynik = 0
    for i in range(k):
        wynik += random.choice(kostka)
    return wynik

def rzucajDlaSumy(kostka):
    rzuty = []
    for i in range(liczbaRzutow):
        rzuty.append(sumujRzuty(kostka))
    return rzuty

rzutyKostka1 = []
rzutyKostka2 = []
sumaRzutow1 = []
sumaRzutow2 = []

rzutyKostka1 = rzucaj(kostka1)
rzutyKostka2 = rzucaj(kostka2)
sumaRzutow1 = rzucajDlaSumy(kostka1)
sumaRzutow2 = rzucajDlaSumy(kostka2)

sredniaR1 = numpy.mean(rzutyKostka1)
sredniaR2 = numpy.mean(rzutyKostka2)
sredniaSR1 = numpy.mean(sumaRzutow1)
sredniaSR2 = numpy.mean(sumaRzutow2)

wariancjaR1 = numpy.var(rzutyKostka1)
wariancjaR2 = numpy.var(rzutyKostka2)
wariancjaSR1 = numpy.var(sumaRzutow1)
wariancjaSR2 = numpy.var(sumaRzutow2)

print("Średnia dla kostki 1 : " + str(sredniaR1))
print("Średnia dla kostki 2 : " + str(sredniaR2))
print("Średnia dla sumy kostki 1 : " + str(sredniaSR1))
print("Średnia dla sumy kostki 2 : " + str(sredniaSR2))

print("Wariancja dla kostki 1 : " + str(wariancjaR1))
print("Wariancja dla kostki 2 : " + str(wariancjaR2))
print("Wariancja dla sumy kostki 1 : " + str(wariancjaSR1))
print("Wariancja dla sumy kostki 2 : " + str(wariancjaSR2))