#Text-Input wird in B-Sprache übersetzt

entry = input("Eingabe: ")
entry_liste = list(entry)
ausgabe = []
vokale = ['a', 'e', 'i', 'o', 'u', 'ü', 'ä', 'ö']
b = "b"

for i in entry_liste:
    if i not in vokale:
        ausgabe.append(i)
    else:
        ausgabe.extend((i, b, i))

uebersetzt = ''.join(ausgabe)
print(uebersetzt)



        
        

