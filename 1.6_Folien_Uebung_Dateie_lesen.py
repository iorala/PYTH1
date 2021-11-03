# Übung: Datei lesen
# 
# Erstellen Sie eine Textdatei (Endung: txt) mit Inhalt und speichern Sie diese im gleichen Ordner wie Ihre Python Programme ab. (Keine Word Dokumente!!)
# 
# Lesen Sie die ganze Datei aus und printen Sie den Inhalt aus.
# Geben Sie Zeile für Zeile der Datei aus.
# Nummerieren Sie die einzelnen Zeilen.
# Geben Sie die 4. Zeile aus.
datei_liste = []
with open("pizza.txt", "r") as offene_datei:
    #print(offene_datei.read())
    for zeile in offene_datei.readlines():
        datei_liste.append(zeile)
    print("alle Zeilen nummerieren")
    for nummer,zeile in enumerate(datei_liste):
        print((nummer+1), zeile)
    print("\nZeile 4 ausgeben:", datei_liste[3] )

