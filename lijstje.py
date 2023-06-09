from time import sleep
menu = "\n"*100+" "*15+"""Welkom bij de bootschappenlijst!
•---------------------------------------------------------•
Typ:
    •Lijst voor een lijst van je boodschappen
    •Voegtoe <naam> <prijs> om een product toe te voegen
    •Wijzig <naam> <prijs> om een product te wijziggen
    •Verwijder <naam> om een product te verwijderen
    •Boodschappen om boodschappen te doen
    •Opslaan om je de lijst op te slaan
    •afsluiten om te stoppen
•---------------------------------------------------------•
typ hier: """

keuze = [1,2,3]

lijstje = {} #zodat vs code geen error geeft
file = open("lijstje.txt","r")
exec("lijstje = "+file.read())
file.close()

def pauze():
    input("Druk enter om door te gaan")

def enkelprint(printer):
    print(printer)
    sleep(1)

def lijtjefunction(lijst):
    print("\n"*100+" "*25+"Jouw lijst\n•---------------------------------------------------------•")
    for i in lijst:
        print("•Een "+i+" voor €"+lijst[i])
    print("•---------------------------------------------------------•")
    pauze()

def add(functkeuze, lijst):
    if functkeuze[1] not in lijst:
        lijst[functkeuze[1]] = functkeuze[2]
        return lijtjefunction(lijst)
    else:
        enkelprint("dat bestaat al!")

def change(functkeuze, lijst):
    if functkeuze[1] in lijst:
        lijst[functkeuze[1]] = functkeuze[2]
        return lijtjefunction(lijst)
    else:
        enkelprint("dat bestaat niet!")

def delete(functkeuze, lijst):
    if functkeuze[1] in lijst:
        del lijst[functkeuze[1]]
        return lijtjefunction(lijst)
    else:
        enkelprint("dat bestaat niet!")

def boodschappenfunction(lijst):
    boodschappenwaarde = 0
    eerste = True
    boodschappenkeuze = ""
    while boodschappenkeuze != "klaar":
        lijtjefunction(lijst)
        if eerste:
            boodschappenkeuze = input("kies een product om in je mand te stoppen of klaar om te stoppen:\n").lower()
            eerste = False
        else: boodschappenkeuze = input("nu nog één (of klaar om te stoppen):\n").lower()
        if boodschappenkeuze in lijst:
            boodschappenwaarde += float(lijst[boodschappenkeuze])
        elif boodschappenkeuze != "klaar":
            enkelprint("dat bestaat niet!")
    print("\ndat wordt dan €"+str(boodschappenwaarde))
    pauze()

def save(lijst):
    file = open("lijstje.txt","w")
    file.write(str(lijst))
    file.close()


while keuze[0] != "afsluiten":
    keuze = input(menu).lower().split(" ")

    if keuze[0] == "lijst":
        lijtjefunction(lijstje)
    
    elif keuze[0] == "voegtoe" and len(keuze ) > 2:
        add(keuze, lijstje)
    
    elif keuze[0] == "wijzig" and len(keuze ) > 2:
        change(keuze, lijstje)
    
    elif keuze[0] == "verwijder" and len(keuze ) > 1:
        delete(keuze, lijstje)
    
    elif keuze[0] == "boodschappen":
        boodschappenfunction(lijstje)
    
    elif keuze[0] == "opslaan":#save
        save(lijstje)
    
    elif keuze[0] != "afsluiten":#error
        enkelprint("kies een optie")

enkelprint("fijne dag verder!")