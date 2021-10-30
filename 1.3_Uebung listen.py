#
# a) Schreiben Sie ein Programm, dass einen Satz entgegen nimmt und dem Benutzer
# mitteilt, wie viele Wörter in dem Satz vorkommen.
satz = input("Bitte gib ein Satz ein: ")
# satz = "Danach soll zurückgegeben werden, wie viele Sätze im Text sind."
liste=satz.split()
# gezaehlt = list(enumerate(liste))
print("Dein Satz enhält ", list(enumerate(liste))[-1][0] + 1, "Wörter")
# print(gezaehlt[-1][0] + 1)
# 
# b) Schreiben Sie ein Programm, dass einen Text entgegennimmt und diesen
# Text in seine einzelnen Sätze splittet. Danach soll zurückgegeben werden,
# wie viele Sätze im Text sind.