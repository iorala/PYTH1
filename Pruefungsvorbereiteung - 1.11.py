# Übung 1.11
# ##########
# a) Schreiben Sie eine Funktion die ein die den Benutzer nach folgenden Daten abfrägt und diese
# dann in ein dict speichert:
#  Name
#  Geburtstag
#  Wohnort
#  Beruf
# Das dict soll zum Schluss ausgegeben werden.
#b)
# personen = {}
# 
# def eingabe():
#     personen["Name"] = input("Name: ")
#     personen["Geburtstag"] = input("Geburtstag: ")
#     personen["Wohnort"] = input("Wohnort: ")
#     personen["Beruf"] = input("Beruf: ")
#     return(personen)
# 
# personen = eingabe()
# print("Name:\t\t",personen["Name"],"\nGeburtstag:\t",personen["Geburtstag"],"\nWohnort:\t",personen["Wohnort"],"\nBeruf:\t\t",personen["Beruf"])


# b) Erweitern Sie das Programm sodass das dict formatiert ausgegeben wird.
#  Bsp:
#  Name: ...
#  Geburtstag: ...
#  ...
# c) Erweitern Sie das Programm sodass der Benutzer mehrere Datensätze eingeben kann. Nach jeder
# Eingabe soll der Benutzer gefragt werden, ob er einen weiteren Datensatz eingeben möchte oder ob
# er die Eingabe beenden möchte und die Datensätze somit ausgegeben werden sollen.
# d) Implementieren Sie eine Funktion, die dem Benutzer erlaubt, im Datensatz nach einer Person zu
# suchen um die dazugehörenden Daten zu erhalten.

#c+d)
personenverz = []

def eingabe():
    personen = {}
    print("Bitte geben Sie eine Person ein")
    personen["Name"] = input("Name: ")
    personen["Geburtstag"] = input("Geburtstag: ")
    personen["Wohnort"] = input("Wohnort: ")
    personen["Beruf"] = input("Beruf: ")
    return(personen)

def suche(verzeichnis):
    term = input("Bitte geben sie den Namen der gesuchten Person ein: ")
    for i in verzeichnis:
        if term in i["Name"]:
            print("Name:\t\t",i["Name"],"\nGeburtstag:\t",i["Geburtstag"],"\nWohnort:\t",i["Wohnort"],"\nBeruf:\t\t",i["Beruf"])

while True:
    personenverz.append(eingabe())
    if input("Möchten sie eine weiter Person erfassen (j/n)? ") == "n":
        break

suche(personenverz)

            
            
