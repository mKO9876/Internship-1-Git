def permutacija(lista):
    if len(lista) == 0:
        return []
    elif len(lista) == 1:
        return [lista]
    
    lista_perm = []
    for i in range(len(lista)):
        ost_liste = lista[:i] + lista[i+1:]
        
        for j in permutacija(ost_liste):
            el = [lista[i]] + j
            if el not in lista_perm: #kako se ne bi spremale iste permutacije
                lista_perm.append(el)
    
    return lista_perm



while True:
    lista = input("Unesite niz brojeva odvojeni razmacima: ").split()
    print(permutacija([int(i) for i in lista]))
    odg = input("Želite li nastaviti (Y/N): ").lower()
    if (odg != "y"): break
