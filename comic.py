# Grundschritte für eine Sentiment-Analyse
from csv import reader
comics = {}
conflicts = []

with open("something-positive.csv") as open_file:
        csv_reader = reader(open_file) # Reader wird mit der geöffneten Datei initialisiert
        for row in csv_reader:
            if row[1] in comics.values():
                conflicts.append((row[0], row[1]))
            comics[row[0]] = row[1]

for i in conflicts:
    print(i[0],i[1])
        