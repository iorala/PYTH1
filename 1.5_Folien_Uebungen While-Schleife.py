# Übung: For-Schleife
#Bauen Sie ein Kassensystem:

# a.  Es sollen so lange Preise eingegeben werden können, bis ein x eingegeben wird. Danach soll der Gesamtpreis ausgegeben werden.
# 
# b.  Falls der Gesamtpreis über 100 CHF sein sollte, gibt es 5% Rabatt.
# 
# c.  Geben Sie den Gesamtpreis in CHF und EUR aus.

total = 0
preis = 0
eurokurs = 0.95
while True:
    preis = input("Geben Sie einen Preis ein: ")
    if preis == "x":
        break
    total = total + float(preis)
if total > 100:
    total = int((total * 0.95)*100)/100 # Runden auf zwei stellen
print("Das Total beträgt:", total, "CHF")
print("Das Total beträgt:", int((total * eurokurs)*100)/100, "EUR")

# 
# d.  Erstellen Sie ein Dict mit Produkten im Shop. Modifizieren Sie den Code sodass nicht mehr der Preis sondern
#     das Produkt angegeben wird um den Gesamtpreis zu berechnen.
# 
# e.  Erweitern Sie Ihr System sodass auch eine Anzahl des Produktes eingegeben werden kann.
# 
produkte = {"Apfel": 1.3, "Birne": 1.4, "Mandarine": 0.90, "Pflaume": 0.70}
total = 0
preis = 0
eurokurs = 0.95
while "Apfel" != "Birne":
    produkt = input("Geben Sie ein Produkt ein: ")
    if produkt == "x":
        break
    elif produkt not in produkte.keys():
        print("haben wir nicht")
        continue
    anzahl = int(input("Wieviel " + produkt + " "))
    total = total + anzahl * produkte[produkt]
if total > 100:
    total = int((total * 0.95)*100)/100 # Runden auf zwei stellen
print("Das Total beträgt:", total, "CHF")
print("Das Total beträgt:", int((total * eurokurs)*100)/100, "EUR")
