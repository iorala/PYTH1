# Uebung 5

# saison = {
# "Jan": "Winter",
# "Feb": "Winter",
# "März": "Frühling",
# "April": "Frühling",
# "Mai": "Frühling",
# "Juni": "Sommer",
# "Juli": "Sommer",
# "August": "Sommer",
# "September": "Herbst",
# "Oktober": "Herbst",
# "November": "Herbst",
# "Dezember": "Winter"}
# 
# eingabe = input("Geben Sie einen Monat ein: ")
# 
# print("Der Monat",eingabe, "ist im",saison[eingabe])

# Uebung 6
# import random
# zufallszahl = random.randint(0,100)
# print(zufallszahl)
# eingabe = -1
# while eingabe != zufallszahl:
#     eingabe=int(input("Geben Sie eine ganze Zahl ein: "))
#     if eingabe > zufallszahl:
#         print("die gesuchte Zahl ist kleiner")
#     elif eingabe < zufallszahl:
#         print("die gesuchte Zahl ist grösser")
# print("Juhuu richtig")
#         
# while True:
#     eingabe=int(input("Geben Sie eine ganze Zahl ein: "))
#     if eingabe == zufallszahl:
#         print("Juhuu richtig")
#         break
#     elif eingabe > zufallszahl:
#         print("die gesuchte Zahl ist kleiner")
#     elif eingabe < zufallszahl:
#         print("die gesuchte Zahl ist grösser")
# 
# 
# zahl = 3
# 
# for item in range (zahl):
#     print(item)
#     print(zahl)


# Schreiben Sie ein Programm, das einen Satz entgegen nimmt und zurückgibt, welche Buchstaben 
# wie oft vorhanden sind.
# b. Erweitern Sie das Programm sodass der Satz nach Buchstaben sortiert zurückgegeben wird. 
# 
# au en loop? mit while?

satz="Schreiben Sie ein Programm, das einen Satz entgegen nimmt und zurückgibt, welche Buchstaben wie oft vorhanden sind."
buchstaben = {}
for i in satz.replace(" ","").replace(".","").lower():
    if buchstaben.get(i):
        buchstaben[i] = buchstaben[i] + 1
    else:
        buchstaben[i] = 1   
print(buchstaben)
