# Grundschritte für eine Sentiment-Analyse
# Autor: Andreas la Roi
# 1. Text holen
#     a. Von einer Textdatei: Schreiben Sie eine Funktion, die eine Textdatei einliest und als String zurückgib
#     b. Aus dem Internet

with open("all_stories_temp_0_iso.txt", "r") as offene_datei:
    text = offene_datei.read()


# 
# 2. Text aufbereiten
#     a. Gross/Kleinschreibung normalisieren: Wandeln Sie den gesamten Text in Kleinbuchstaben um

text = text.lower()


#     b. Sonderzeichen entfernen: Entfernen Sie alle Sonderzeichen aus dem Text.
#         - Erst prüfen, welche Sonderzeichen es gibt. Dies sind : !'(),-.:?«»  (gemäss sed s/'[a-zA-Z0-9]'/""/g)

sonderzeichen = {"!": " ", "'": " ","(": " ",")": " ", ",": " ", "-": " ",";": " ",".": " ",":" : " ","?": " ", "«": " ","»": " "} 
table = text.maketrans(sonderzeichen)
text = text.translate(table)
#print(text)

#     c. Aufteilung in einzelne Wörter: Teilen Sie die den Text in einzelnen Wörter auf.
woerter = text.split()
#print(woerter)


# 3. Sentiment zählen
#     a. Sentiment Lexikon einlesen:  Suchen und implementieren Sie ein Sentiment Lexikon.
#        i. Einlesen, Auslesen, Abspeichern. Beachten Sie, dass das Lexikon "benutzbar" sein muss.

from csv import reader

# negatives Sentiment Lexikon auslesen und dict erstellen
dict_neg = {}

with open('SentiWS_v2.0_Negative.txt') as open_file:
    csv_reader = reader(open_file, dialect="excel-tab") # Reader wird mit der geöffneten Datei initialisiert
    for row in csv_reader:
        key = row[0].rsplit(sep="|")[0] # trennt das Wort vom POS-Tag
        dict_neg[key] = float(row[1])
        # Für jede Flexion wird ein eigenener Eintrag erstelle, da wir noch kein stemming gelernt haben 
        if len(row) > 2:
            if row[2] != "": # Aus irgendeinem Grund landen sonst leere Strings als key im dict?!
                for word in row[2].split(sep=","):    
                    dict_neg[word] = float(row[1]) 

# positoves Sentiment Lexikon auslesen und dict erstellen
dict_pos = {}

with open('SentiWS_v2.0_Positive.txt') as open_file:
    csv_reader = reader(open_file, dialect="excel-tab") # Reader wird mit der geöffneten Datei initialisiert
    for row in csv_reader:
        key = row[0].rsplit(sep="|")[0] # trennt das Wort vom POS-Tag
        dict_pos[key] = float(row[1])
        # Für jede Flexion wird ein eigenener Eintrag erstelle, da wir noch kein stemming gelernt haben 
        if len(row) > 2:
            if row[2] != "": # Aus irgendeinem Grund landen sonst leere Strings als key im dict?!
                for word in row[2].split(sep=","):
                    dict_pos[word] = float(row[1]) 

#     b. Mit Artikel abgleichen: Vergleichen Sie die Wörter im Artikel mit den Wörtern im Lexicon

#
## Anscheinende sind wörter sowohl in der positiven, wie auch der negativen liste drin? 
# for lemma in dict_pos.keys():
#     if lemma in dict_neg:
#         print(lemma, "ist in beiden dicts vorhanden mit", dict_pos[lemma], "und", dict_neg[lemma])
#


sentiment = 0

score_neg = 0
worte_neg = set()
score_pos = 0
worte_pos = set()

for wort in woerter:
    ### Zwei ifs, da das gleiche wort sowohl positive, wie negative werte haben kann (siehe test oben)
    if wort in dict_pos:
        sentiment = sentiment + dict_pos[wort]
        if dict_pos[wort] == score_pos:
            worte_pos.add(wort)
        elif dict_pos[wort] > score_pos:
            score_pos = dict_pos[wort]
            worte_pos.clear()
            worte_pos.add(wort)
            
    if wort in dict_neg:
        sentiment = sentiment + dict_neg[wort]
        if dict_neg[wort] == score_neg:
            worte_neg.add(wort)
        elif dict_neg[wort] < score_neg:
            score_neg = dict_neg[wort]
            worte_neg.clear()
            worte_neg.add(wort)
            
             

#
# 4. Ausgabe
#     a. Geben Sie das Sentiment aus.
print(sentiment)
#     b. Geben Sie die negativsten Wörter aus. (ich interpretiere das als alle Wörter im Text, welche den gleichen negativsten Score haben)
print(score_neg, worte_neg)

#     c. Geben Sie die positivsten Wörter aus. (ich interpretiere das als alle Wörter im Text, welche den gleichen negativsten Score haben)
print(score_pos, worte_pos)