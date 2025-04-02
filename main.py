import random

barvy = ["modrá", "červená", "zelená", "fialová", "bíla"]
print(barvy)

dalsiBarva = input("Napište nějakou další barvu: ")

barvy.append (dalsiBarva)

for i in barvy :
    print(i)

nahodnahodnota = random.choice(barvy)
print (nahodnahodnota)