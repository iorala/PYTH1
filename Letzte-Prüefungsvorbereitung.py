# Übung 1.9
# #########
# a) Schreiben Sie eine Funktion, die einen Text entgegen nimmt und zurück gibt, wie viele Wörter in
# dem Text vorkommen.

#def zaehl_wort(text):
#    return(len(text.split()))
#print(zaehl_wort(input("Gib text: ")))

# b) Schreiben Sie eine Funktion, die einen Text entgegen nimmt und die Anzahl der Sätze zurück
# gibt.
#def zaehl_satz(text):
#    return(len(text.split(". ")))
#print(zaehl_satz(input("Gib text: ")))

# c) Schreiben Sie eine Funktion, die einen Text entgegen nimmt und der am meisten benutzter
# Buchstabe (mit Anzahl) zurückgibt.
# 
# def zaehl_buchst(text):
#     anzahl = {}
#     text = text.lower()
#     for buchst in text:
#         if buchst == " ":
#             continue
#         elif buchst == ".":
#             continue
#         elif buchst in anzahl:
#             anzahl[buchst] += 1
#         else:
#             anzahl[buchst] = 1
#     
#     hauf_b = ""
#     hauf_anz = 0
#     for letter,count in anzahl.items():
#         if count > hauf_anz:
#             hauf_b = letter
#             hauf_anz = count
#     return(hauf_b, hauf_anz)
# 
# print(zaehl_buchst("Des einen Freud ist des anderen Leid. Früh übt sich, wer ein meister werden will"))

#8)
# Fibonacci Reihe*: Schreiben Sie ein Programm, dass die Fibonacci
# Reihe bis zu einem vom Benutzer definierten Maximalwert berechnet
# (ein Element der Fibonacci Reihe berechnet sich aus der Summe der
# beiden vorhergehenden Zahlen berechnet (sprich: 0+1 = 1; 1+1 = 2;
# 1+2 = 3; 2+3 = 5; 3+5 = 8; 5+8 = 13, ...)).

def fibonacci(stop):
    value = 1
    oldvalue = 0
    print(oldvalue)
    while True:
        newvalue = value + oldvalue
        oldvalue = value
        value = newvalue
        if value >= stop:
            break
        print(value)
        

fibonacci(int(input("maximalwert: ")))
