n = int(input("Unesite dužinu linije: "))
m = int(input("Unesite broj elemenata u liniji: "))
tekst = input("Uneiste tekst: ").split()
brojac = 0 
print(tekst)
if (n >= m):
    tekst_ispis = ""
    for rijec in tekst:
        if len(rijec) > (m-len(tekst_ispis)):
            praznine = int((n - len(tekst_ispis))/2)
            praznine = " " * praznine 
            print(praznine + tekst_ispis + praznine)
            tekst_ispis = rijec + " "
        else: 
            tekst_ispis += rijec + " "
    if(len(tekst_ispis) != 0):
        praznine = int((n - len(tekst_ispis))/2)
        praznine = " " * praznine 
        print(praznine + tekst_ispis + praznine)
else: print("n je manji od m")

#mislim da nisam shvatila zadatak jer na primjeru je bilo koja linija dulja od moje
#koliko sam shvatila m predstavlja koliko oznaka može biti unutar jedne linije
#no u primjeru vidim da prva ispisana linija ima oko 66 znakova iako je ograničenje m bilo 50