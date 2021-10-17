f = open("snooker.txt", "r")
lista = []
for sor in f:
    lista.append(sor.strip().split(";"))
f.close()
lista.remove(lista[0])
#3.feladat:
print(f"3.feladat: A világranglistán {len(lista)} versenyző szerepel.")
#4.feladat:
p2v = lambda x: x.replace(".",",")
pont = []
for sor in lista:
    pont.append(int(sor[-1]))
atlag = f"{sum(pont) / len(lista):.2f}"
print(f"4.feladat: A versenyzők átlagosan {p2v(atlag)} pontot kerestek")
#5.feladat.
kinaversenyzo = []
for sor in lista:
    if sor[2] == "Kína":
        kinaversenyzo.append(sor)
nagyobb = 0
for sor in kinaversenyzo:
    if nagyobb < int(sor[-1]):
        nagyobb = int(sor[-1])
        helyezes = sor[0]
        nev = sor[1]
        orszag = sor[2]
        nyeremeny = nagyobb * 380
print(f"5.feladat: A legjobban kereső kínai versenyző")
print(f"        Helyezés: {helyezes}")
print(f"        Név: {nev}")
print(f"        Ország: {orszag}")
print(f"        A nyeremény összege: {nyeremeny} Ft")
#6.feladat.
if sor[2] != "Norvégia":
    print(f"6.feladat: A versenyzők között nincs norvég játtékos")
else:
    print(f"6.feladat: A versenyzők között van norvég játtékos")
#7.feladat.
stat = dict()
for sor in lista:
    orszag = sor[2]
    stat[orszag] = stat.get(orszag,0) + 1
print(f"7.feladadat: Statisztika:")
for sor in stat.items():
    if sor[0] == "Kína":
        print(f"        Kína: {sor[1]} fő")
    if sor[0] == "Anglia":
        print(f"        Anglia: {sor[1]} fő ")
    if sor[0] == "Wales":
        print(f"        Wales: {sor[1]} fő ")
    if sor[0] == "Skócia":   
        print(f"        Skócia: {sor[1]} fő")
    
    
    
