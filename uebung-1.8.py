# Übung 1.8
# a)
# def dedup(liste):
#     no_dup=set(liste)
#     return(no_dup)
# 
# woerter = ["pferd","hund","pferd","hund","affe"]
# print(dedup(woerter))

# Übung 1.8
# b)
# def dedup(liste):
#     no_dup=[]
#     for i in liste:
#         if i.lower() not in [x.lower() for x in no_dup]:
#             no_dup.append(i)
#     return(no_dup)
# 
# woerter = ["Pferd","Hund","pferd","hund","affe","Frosch", "Frosch"]
# print(dedup(woerter))

# # Übung 1.8
# # b)
def dedup(liste):
    liste_small = []
    for i in liste:
        liste_small.append(i.lower())
    no_dup=set(liste_small)
    return(no_dup)

woerter = ["Pferd","hund","pferd","Hund","affe"]
print(dedup(woerter))
