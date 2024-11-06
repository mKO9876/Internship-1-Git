import math

while True:
    broj = int(input("Unesite prirodni broj: "))
    lista = [[] for i in range(broj)]
    if broj > 1 and broj % 2 != 0:
        srednji_red = int(math.ceil(broj / 2))
        zvjezdice = 1
        for i in range (srednji_red):
            praznine = int((broj - zvjezdice) / 2) * " "
            lista[i] = praznine + zvjezdice * "*" + praznine
            lista[broj-i-1]= praznine + zvjezdice * "*" + praznine
            zvjezdice += 2

    for i in lista:
        print(i)

    odg = input("Y/N: ").lower()
    if odg != "y": break


