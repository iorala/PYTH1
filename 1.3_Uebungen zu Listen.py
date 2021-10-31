# 1.3 Übungen zu Listen
# 1.1 Namen
# Speichern Sie die Namen einiger Ihrer Freunde in einer Liste mit
# Namen. Drucken Sie den Namen jeder Person, indem Sie nacheinander
# auf jedes Element in der Liste zugreifen.

freunde = ["Kapt'n Blaubär","Napoleon","Jon Snow"]
print(freunde[0],freunde[2],freunde[1])

# 
# 1.2 Seid gegrüsst
# Beginnen Sie mit der Liste, die Sie in Übung 1.1 verwendet haben:
# Begrüssen Sie jede Person mit einer personalisierten Nachricht.

print("Ahoy",freunde[0],"\nBonjour",freunde[1],"\nYou know nothing",freunde[2])
# 
# 1.3 Funktion
# Erstellen Sie eine Funktion die eine Liste von Personen enthält.
# Die Funktion nimmt dann denn Index einer spezifischen Person als Argument
# und begrüsst dann die spezifische Person.
# 
# Beispiel:
# 
# grüsse(3) #-> Hallo Fabian
# 
# grüsse(1) #-> Hallo Norman

def gruesse(index):
    namen = ["Pippi","Kasper","Hotzenplotz"]
    print("Guten morgen", namen[index])

gruesse(0)


