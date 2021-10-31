# Übungen zu Dictionaries
# 1.1 Person:
print("Uebung 1.1 Person:")
# Verwenden Sie ein Wörterbuch, um Daten über eine Person zu speichern, die Sie kennen.
# 
# Speichern Sie deren Vornamen, Nachnamen, Alter und die Stadt, in der sie lebt. Sie
# 
# sollte dazu Schlüssel wie Vorname, Nachname, Alter und Stadt verwenden.
# Geben Sie die Daten die im Dictionary gespeichert sind schön formatiert aus.
#

person = {"Vorname": "Napoléon", "Nachname": "Bonaparte" , "Alter": 45, "Stadt": "Portoferraio" }
print( "Vorname:\t", person["Vorname"], "\n"\
       "Nachname:\t", person["Nachname"], "\n"\
       "Alter:\t\t", person["Alter"], "\n"\
       "Stadt:\t\t", person["Stadt"], "\n")

# 
# 
# 1.2 Glossar:
print("\nUebung 1.2 Glossar:")
# Ein Python-Wörterbuch kann verwendet werden, um ein aktuelles Wörterbuch zu modellieren.
# 
# Um Verwirrung zu vermeiden, nennen wir es jedoch ein Glossar.
# 
# Denken Sie an fünf Programmierwörter, die Sie in letzter Zeit gelernt haben.
# Verwenden Sie diese Begriffe als Schlüssel in Ihrem Glossar und speichern Sie sie.
# Als Wert soll die Bedeutung bzw Erklärung des Begriffs dienen.
# 
# Drucken Sie jedes Wort und seine Bedeutung als ordentlich formatierte Ausgabe. Du könntest
# 
# Drucken Sie die Begriffe schön formatiert aus.

glossar = { "Tupel": "Tupel tuple() sind im Prinzip nichts anderes als unveränderbare Listen. Zur Unterscheidung werden sie in Runden Klammern geschrieben",
            "Set": "Sets sind wie ungeordnete Listen jedoch können diese keine gleichen Elemente beinhalten.",
            "Turtle": "Turtle ist ein Basis-Modul in Python. Mit Turtle lässt sich eine kleine Schildkröte bewegen die dabei eine Spur zieht.",
            "Algorithmus": "Verfahrensvorschrift zur Berechnung von Gesuchtem aus gegebenen Grössen unabhängig von Programmiersprache und Rechner",
            "Konditionen": "Konditionen sind Wahr (True) oder Falsch (False). Somit sind sie das Ergebnis bool’scher Operatoren."}


print("Tupel:\t\t", glossar["Tupel"],
      "\nSet:\t\t", glossar["Set"],
      "\nTurtle:\t\t", glossar["Turtle"],
      "\nAlgorithmus:\t", glossar["Algorithmus"],
      "\nKontitionen:\t", glossar["Konditionen"])
# 
# 
# 
# 1.3 Funktion:
print("\nUebung 1.3 Funktion:")
# Schreiben Sie eine Funktion, die ein Begriff entgegen nimmt und dessen
# Bedeutung/Erklärung zurück gibt.

def begriffe_erklaeren():
    begriff= input("Zu welchem begriff möchten Sie eine Erklärung? ")
    print(glossar[begriff])

begriffe_erklaeren()
# 
# 
# 
# 1.4 Erweitern:
# Überlegen Sie sich, welche zusätzlichen Inhalte in so einem Eintrag möglich
# oder interessant wären.