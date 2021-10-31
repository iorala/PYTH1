# Übung: For-Schleife
print ("Übung: For-Schleife")
# Schreiben Sie ein Programm, dass einen Satz entgegen nimmt, jeden Buchstaben durchgeht und wenn ein E gefunden wird
# ein Hurra ansonsten den Buchstaben ausgibt .


# satz = list(input("Gib einen Satz ein: "))
# print 
# for buchstabe in satz:
#     if buchstabe == "e":
#             buchstabe = "Hurra"
#     print(buchstabe)
#     

print("Uebung: For-Schleife 2")
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
    
