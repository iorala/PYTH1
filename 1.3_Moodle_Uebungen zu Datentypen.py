# 1.3 Übungen zu Datentypen 
# Übung 1
# Gegeben ist:
# 
random = ['a', ('b', 'cd'), [3, 4]]
# Wählen Sie mittel Index (liste[x]) folgendes aus:
# 
# [3, 4]
print(random[2])
# a
print(random[0])
# 4
print(random[2][1])
# b
print(random[1][0])
# d
print(random[1][1][1])
# 'cd'
print(random[1][1])
#
# Übung 2
# Gegeben ist: 
liste = ['larry', 'curly', 'moe']
# 
# Fügen Sie "shemp" zur Ende der Liste hinzu.
liste.append("shemp")
print(liste)
# Fügen Sie "xxx" an Index 0 ein.
liste.insert(0,"xxx")
print(liste)
# Fügen Sie die Liste ['yyy', 'zzz'] am Ende der Liste hinzu.
liste.append(['yyy', 'zzz'])
print(liste)
# Suchen und entfernen Sie den Eintrag 'curly'.
liste.remove("curly")
print(liste)
