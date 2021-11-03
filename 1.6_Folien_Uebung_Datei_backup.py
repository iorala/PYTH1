# Übung: Backup
# Schreiben sie ein Programm, das eine Sicherungskopie einer Textdatei erstellt.
# (Eine Datei auslesen und in eine neue Datei einfügen.)
# Verändern Sie das Programm so, dass in der Zieldatei bei
# jeder Zeile zuerst die Zeilennummer gefolgt von einem Doppelpunkt steht.
# Erweitern Sie das Programm, sodass es eine Fehlermeldung ausgibt,
# wenn die Datei nicht geöffnet (oder geschrieben) werden konnte.
textdatei = "pizza.txt"
sicherung = "pizza.txt.bak"
original_zeilen = []

try:
    with open(textdatei, "r") as original_datei:
        for zeile in original_datei.readlines():
            original_zeilen.append(zeile)
            
except:
    print(textdatei, "konnte nicht zum lesen geöffnet werden")
    


try:
    with open(sicherung, "w") as backup_datei:
        for nr,zeile in enumerate(original_zeilen):
            backup_datei.write(str(nr+1) + ":\t" + zeile)
            
except:
    print(sicherung, "konnte nicht zum schreiben geöffnet werden")
    
