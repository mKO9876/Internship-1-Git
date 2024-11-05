def prikaz_igre(igra):

    for i in range(0, len(igra), 3):
        print(igra[i] + " | " + igra[i+1] + " | " + igra[i+2])
        print("--------")

def provjera_pobjednika(lista, ukupno_koraka):
    for i in range(3): #okomito
        if (lista[i] == lista[i + 3] == lista[i + 6]) and lista[i] != "":
            print(f"{lista[i]} je pobijednik")
            return True

    for i in range(0,7,3): #vodoravno
         if (lista[i] == lista[i + 1] == lista[i + 2]) and lista[i] != "":
            print(f"{lista[i]} je pobijednik")
            return True
         
    if ((lista[2] == lista[4] == lista[6]) or (lista[0] == lista[4] == lista[8])) and lista[4] != "": 
        print(f"{lista[4]} je pobijednik")
        return True
    
    if(ukupno_koraka == 8): 
        print("Neriješeno")
        return True
    
    return False



igra = ["", "", "", 
        "", "", "", 
        "", "", ""]
ukupno_koraka = 0

while True: #da bi se igra mogla nastaviti i nakon pobjede

    while True: #u slučaju da korisnik upiše krivo 

        korak = int(input("Unesi broj od 1 do 9: "))

        if korak <= 9 and korak >=1 and igra[korak-1] =="" :
            if ukupno_koraka % 2 == 0: igra[korak-1] = "x"
            else: igra[korak-1] = "o"

            ukupno_koraka+=1
            prikaz_igre(igra)
            break

        else: print("Unesete neko drugo polje")

    if(provjera_pobjednika(igra, ukupno_koraka)): 

        odg = input("Želite li nastaviti (Y/N): ").lower()

        if (odg == "y"): 
            igra = ["", "", "", 
                    "", "", "", 
                    "", "", ""]
            ukupno_koraka = 0

        else: break


