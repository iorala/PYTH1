# Copyright (c) 2021 Andreas la Roi
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 
# Grundschritte für eine Sentiment-Analyse
from csv import reader
artikel = "all_stories_temp_0_iso_short.txt"
sentiment_ws_pos = 'SentiWS_v2.0_Positive.txt'
sentiment_ws_neg = 'SentiWS_v2.0_Negative.txt'

# 1. Text holen
#     a. Von einer Textdatei: Schreiben Sie eine Funktion, die eine Textdatei einliest und als String zurückgib
#     b. Aus dem Internet
try:
    with open(artikel, "r") as offene_datei:
        text = offene_datei.read()
except:
    print("Artikel-Datei kann icht geöffnet werden:", artikel)
    exit()
# 
# 2. Text aufbereiten
#     a. Gross/Kleinschreibung normalisieren: Wandeln Sie den gesamten Text in Kleinbuchstaben um

text = text.lower()

#     b. Sonderzeichen entfernen: Entfernen Sie alle Sonderzeichen aus dem Text.
#         - Erst prüfen, welche Sonderzeichen es gibt: Dies sind !'(),-.:?«»  (gemäss sed s/'[a-zA-Z0-9]'/""/g)

sonderzeichen = {"!": " ", "'": " ","(": " ",")": " ", ",": " ", "-": " ",";": " ",".": " ",":" : " ","?": " ", "«": " ","»": " "} 
table = text.maketrans(sonderzeichen)
text = text.translate(table)

#     c. Aufteilung in einzelne Wörter: Teilen Sie die den Text in einzelnen Wörter auf.
woerter = text.split()

# 3. Sentiment zählen
#     a. Sentiment Lexikon einlesen:  Suchen und implementieren Sie ein Sentiment Lexikon.
#        i. Einlesen, Auslesen, Abspeichern. Beachten Sie, dass das Lexikon "benutzbar" sein muss.

# negatives Sentiment Lexikon auslesen und dict erstellen
dict_neg = {}

try:
    with open(sentiment_ws_neg) as open_file:
        csv_reader = reader(open_file, dialect="excel-tab") # Reader wird mit der geöffneten Datei initialisiert
        for row in csv_reader:
            key = row[0].rsplit(sep="|")[0] # trennt das Wort vom POS-Tag
            dict_neg[key.lower()] = float(row[1])
            # Für jede Flexion wird ein eigenener Eintrag erstelle, da wir noch kein stemming gelernt haben 
            if len(row) > 2:
                if row[2] != "": # Aus irgendeinem Grund landen sonst leere Strings als key im dict?!
                    for word in row[2].split(sep=","):    
                        dict_neg[word.lower()] = float(row[1]) 
except:
    print("Negativer Sentiment-Wortschatz kann nicht geöffnet werden: ", sentiment_ws_neg)
    exit()

# positives Sentiment Lexikon auslesen und dict erstellen
dict_pos = {}

try:
    with open(sentiment_ws_pos) as open_file:
        csv_reader = reader(open_file, dialect="excel-tab") # Reader wird mit der geöffneten Datei initialisiert
        for row in csv_reader:
            key = row[0].rsplit(sep="|")[0] # trennt das Wort vom POS-Tag
            dict_pos[key.lower()] = float(row[1])
            # Für jede Flexion wird ein eigenener Eintrag erstelle, da wir noch kein stemming gelernt haben 
            if len(row) > 2:
                if row[2] != "": # Aus irgendeinem Grund landen sonst leere Strings als key im dict?!
                    for word in row[2].split(sep=","):
                        dict_pos[word.lower()] = float(row[1]) 
except:
    print("Positiver Sentiment-Wortschatz kann nicht geöffnet werden: ", sentiment_ws_pos)
    exit()
        
#     b. Mit Artikel abgleichen: Vergleichen Sie die Wörter im Artikel mit den Wörtern im Lexicon
#
## Anscheinende sind wörter sowohl in der positiven, wie auch der negativen liste drin? 
# for lemma in dict_pos.keys():
#     if lemma in dict_neg:
#         print(lemma, "ist in beiden dicts vorhanden mit", dict_pos[lemma], "und", dict_neg[lemma])
#

sentiment_pos = 0.0
sentiment_neg = 0.0
worte_neg = set()
worte_pos = set()
counter_neg = 0
counter_pos = 0

for wort in woerter:
    ### Zwei ifs, da das gleiche wort sowohl positive, wie negative werte haben kann (siehe test oben)
    if wort in dict_pos:
        sentiment_pos = sentiment_pos + dict_pos[wort]
        worte_pos.add((wort,dict_pos[wort]))
        counter_pos = counter_pos + 1

    if wort in dict_neg:
        sentiment_neg = sentiment_neg + dict_neg[wort]
        worte_neg.add((wort,dict_neg[wort]))
        counter_neg = counter_neg + 1

#
# 4. Ausgabe
#     a. Geben Sie das Sentiment aus.
print("Die Artikel enthalten", counter_pos,"positive Wörter und", counter_neg,"negative. Die Summe positiven Werte beträgt", sentiment_pos, "diejenige der negativen", sentiment_neg,". für ein Total von", sentiment_pos + sentiment_neg)
#     b. Geben Sie die negativsten Wörter aus.
print("\nDie 10 negativsten Wörter und ihr Werte:")
worte_neg_list = sorted(worte_neg,key=lambda score: score[1])
for wort in worte_neg_list[0:9]:
    print(wort[0] + ":", wort[1])

#     c. Geben Sie die positivsten Wörter aus.
print("\nDie 10 positivsten Wörter und ihr Werte:")
worte_pos_list = sorted(worte_pos,key=lambda score: score[1], reverse=True)
for wort in worte_pos_list[0:9]:
    print(wort[0] + ":", wort[1])
