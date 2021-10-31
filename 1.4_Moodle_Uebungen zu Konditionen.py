# Übungen zu Konditionen
# 1.  Gerade und Ungerade
print("1.  Gerade und Ungerade")
# 
# Schreiben Sie ein Programm, das eine ganze Zahl vom Benutzer liest. Dann sollte Ihr Programm eine Meldung anzeigen,
# die angibt, ob die ganze Zahl gerade oder ungerade ist.
zahl = int(input("Geben Sie eine Zahl ein: "))
if zahl % 2 == 0:
    print("Ihre Zahl ist gerade")
else:
    print("Ihre Zahl ist ungerade")
 
# 
# 2. Hundejahre
print("\n2. Hundejahre")
# 
# Es wird allgemein gesagt, dass ein Menschenjahr 7 Hundejahren entspricht. Diese einfache Umwandlung übersieht jedoch,
# dass Hunde in etwa zwei Jahren das Erwachsenenalter erreichen. Infolgedessen glauben einige Leute, dass es besser ist,
# jedes der ersten beiden Menschenjahre als 10,5 Hundejahre zu zählen und dann jedes weitere Menschenjahr als 4 Hundejahre.
# 
# Schreiben Sie ein Programm, das die im vorherigen Abschnitt beschriebene Umstellung von Menschenjahren auf Hundejahre implementiert.
# Stellen Sie sicher, dass Ihr Programm bei Konvertierungen von weniger als zwei Menschenjahren und bei Konvertierungen von zwei oder
# mehr Menschenjahren korrekt funktioniert. Ihr Programm sollte eine entsprechende Fehlermeldung anzeigen,
# wenn der Benutzer eine negative Zahl eingibt.

hundejahre = 0
mj = int(input("Geben Sie eine Anzahl Menschenjahre ein: "))

if mj <= 0:
    print("Bitte kein negative Jahre eingeben, die Welt ist schon negativ genug!")
elif mj <= 2:
    hundejahre = mj * 10.5
else:
    hundejahre = 21 + (mj-2)*4 
print(mj ,"Menschenjahre entsprechen", hundejahre, "Hundejahren")

# 
# 3. Vokale
print("\n3. Vokale")
# In dieser Übung erstellen Sie ein Programm, das einen Buchstaben des Alphabets vom Benutzer einliest.
# Wenn der Benutzer ein, e, i, o oder u eingibt, sollte Ihr Programm eine Meldung anzeigen die darauf hindeutet, dass der
# eingegebene Buchstabe ein Vokal ist. 
#
# Wenn der Benutzer y eingibt, dann sollte Ihr Programm eine Meldung anzeigen, dass  y manchmal ein Vokal ist und manchmal y ein
# Konsonant ist.
vokale = ("a", "e", "i", "o", "u")
buchstabe = input("Geben Sie einen Buchstaben ein: ")

if buchstabe == "y":
    print("Der Buchstabe", buchstabe, "ist manchmal eine Vokal und manchmal ein Konsonant")
elif buchstabe in vokale:
    print("Der Buchstabe", buchstabe, "ist ein Vokal")
else:
    print("Der Buchstabe", buchstabe, "ist ein Konsonant")