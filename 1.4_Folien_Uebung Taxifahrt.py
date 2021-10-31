# 1.4 Übung Taxifahrt
# Schreiben Sie eine Funktion die den Preis für eine Taxifahrt berechnet:
# 
# Pro Fahrt wird ein Startpreis von 8.-CHF am Tag und 10.-CHF in der Nacht berechnet.
# Pro gefahrener Kilometer werden 3.-CHF am Tag und 4.-CHF in der Nacht berechnet.
# Die ersten 2 Kilometer sind im Startpreis inbegriffen.
# 
# Die Funktion soll dabei folgende Argumente entgegen nehmen:
# Tageszeit (“Tag” oder “Nacht”)
# Die Strecke in Kilometer
# 
# Erweitern Sie die Funktion sodass sie den Benutzer nach den Daten abfragt,
# also ohne Argumente aufgerufen werden muss.


def taxifahrt(tageszeit,strecke):
    if tageszeit == "Tag":
        preis = 8 + (strecke - 2)* 3
    if tageszeit == "Nacht":
        preis = 10 + (strecke - 2)* 4 
    return preis

tageszeit = input("War die Fahrt am Tag oder in der Nacht? ")
strecke = int(input("Wie lang war die Strecke (in km)? "))
print("Kosten in CHF:", taxifahrt(tageszeit,strecke))

