# Übung: For-Schleife
print ("Übung: For-Schleife")
# Schreiben Sie ein Programm, dass einen Satz entgegen nimmt, jeden Buchstaben durchgeht und wenn ein E gefunden wird
# ein Hurra ansonsten den Buchstaben ausgibt .


satz = list(input("Gib einen Satz ein: "))
print 
for buchstabe in satz:
    if buchstabe == "e":
            buchstabe = "Hurra"
    print(buchstabe)
    

print("\nUebung: For-Schleife 2")
# Gegeben sei:
mein_dict = {"Chur": "7000",  "Sargans": "7320",  "Bad Ragaz": "7310"}
# 
# Erstellen Sie mittels einer For-Schleife folgende Ausgabe:
# 
# Chur hat die 7000 als Postleitzahl.
# Sargans hat die 7320 als Postleitzahl.
# Bad Ragaz hat die 7310 als Postleitzahl.
# 
# Benutzen Sie hierfür einmal die Tupel des Dict und einmal das entpackte Dict in der For-Schleife.

for beide_als_tupel in mein_dict.items():
    print(beide_als_tupel[0], "hat die", beide_als_tupel[1], "als Postleitzahl.")

print("\n")

for schluessel, wert in mein_dict.items():
    print(schluessel, "hat die", wert, "als Postleitzahl.")
    
     
# Übung: For-Schleife

print("\nUebung: For-Schleife 3")

# a)  Schreiben Sie ein Programm, das einen Satz entgegen nimmt und mit folgenden Modifikationen zurückgibt:
#     e -> 3, a -> 4, o -> 0, i -> 1, s -> 5. Dabei sollen Gross- sowie Kleinbuchstaben umgewandelt werden.

satz = input("Gib einen Satz ein: ")
ersetz = {"e": "3", "a": "4", "o": "0", "i": "1", "s": "5"}
satz_neu = ""

for buchstabe in satz:
    if buchstabe.lower() in ersetz.keys():
        buchstabe = ersetz[buchstabe.lower()]
    satz_neu = satz_neu + buchstabe
print(satz_neu)


# 
# b)  Geben Sie mittels einer For-Schleife jeden Buchstaben eines Strings aus. Nummerieren Sie dabei jeden Buchstaben.
#     Erinnern Sie sich daran, dass es eine Funktion zum nummerieren einer Sequenz gibt!

string_b = "Supercalifragisilit"
for buchstabe in enumerate(string_b):
    print(buchstabe)


# c)  Geben Sie mittels einer For-Schleife jede Zahl zwischen 0 und 10 aus. Erinnern Sie sich daran, dass es eine Funktion gibt,
#     die einen Zahlenstrahl erstellen kann!

for zahl in range(11):
    print(zahl)

