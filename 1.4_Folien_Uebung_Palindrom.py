# Ein Palindrom ist ein Wort das in beide Richtungen gleich gelesen wird:
# Bsp: Anna, Drehherd, Kukuk
# 
# Bauen Sie eine Funktion, die ein Wort entgegennimmt und dann zurückgibt, ob es sie bei dem Wort um ein Palindrom handelt oder nicht.

#wort = input("Geben sie ein Wort ein")

def palindrom(wort):
    wort = wort.lower() 
    if wort == wort[::-1]:
        return("Ihr Wort ist ein Palindrom")
    else:
        return("Ihr Wort ist kein Palindrom")
    
print(palindrom(input("Geben Sie ein Wort ein: ")))