import Recepcija
import Gosti

def main():
    print()
    print( "Evidencija gostiju")
    print( "==================")
    print()
    if not login():
        print("\nNiste uneli dobro korisnicko ime ili lozinku.")
        print()
        main()    
    komanda = '0'
    while komanda != 'X':
        komanda = menu()
        if komanda == '1':
            addGost()
        elif komanda == '2':
            listGost()
        elif komanda == '3':
            addDan()
        elif komanda == '4':
            updateInfo()
        elif komanda == '5':
            findGost()
        elif komanda == '6':
            printRacun()
        elif komanda == '7':
            mostDays()
        elif komanda == '8':
            leastDays()
        elif komanda == '9':
            printGrafik()
        else:
            print( "Dovidjenja.")
            break

def menu():
    printMenu()
    command = input(">> ")
    while command.upper() not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "X"):
        print("\nUneli ste pogresnu komandu")
        printMenu()
        command = input(">> ")
    return command.upper()

def printMenu():
    print("\nIzaberite opciju: ")
    print("1 - Dodaj gosta")
    print("2 - Prikaz svih goostiju")
    print("3 - Produzenje boravka")
    print("4 - Izmena informacija")
    print("5 - Pronadji gosta")
    print("6 - Prikaz racuna")
    print("7 - Gost koji je najvise boravio u hotelu")
    print("8 - Gost koji je najmanje boravio u hotelu")
    print("9 - Broj gostiju po mesecu")
    print("x - Izlaz ")
         
        
def login():
    username = input("Korisnicko ime >> ")
    password = input("Lozinka >> ")
    return Recepcija.login(username, password)
    
def addGost():
    print("[1] Upis novog gosta\n")
    print()
    g = {}
    g["ime"] = input("Ime >> ")
    g["prezime"] = input("Prezime >> ")
    g["email"] = input("mail >> ")
    g["brTel"] = input("Broj telefona >> ")
    brDana = eval(input("Broj dana boravka >> "))
    g["brDana"] = str(brDana)
    datum1 = Gosti.unesiDatum1()
    g["datum1"] = datum1
    datum2 = Gosti.unesiDatum2(datum1, brDana)
    g["datum2"] = datum2
    g["brSobe"] = Gosti.dodeliSobu()
    g["cenaS"] = str(Gosti.ukupnaCena(g["brSobe"], brDana))
    Gosti.addGost(g)
    Gosti.saveGost()
    
        
def listGost():
    print("[2] Lista svih gostiju:\n")
    print(Gosti.foramtHeader())
    print(Gosti.listGost())
    

def addDan():
    print("[5] Produzenje boravka:\n")
    Gosti.addDan()

def updateInfo():
    print("[4] Izmena informacija:\n")
    brSobe = input("Unesite broj sobe u kom se nalazi gost >> ")
    print("Da li zelite da menjate e-mail ili broj telefona (uneti [email/brTel]) ?")
    kljuc = input(">> ")
    while kljuc not in ("email", "brTel"):
        print("\nUneli ste pogresnu komandu")
        kljuc = input(">> ")
    vrednost = input("Unesite novu vrednost >> ")
    Gosti.updateInfo(brSobe, kljuc, vrednost)

def findGost():
    print("[5] Pronadji gosta po broju sobe:\n")
    brSobe = input("Unesite broj sobe >> ")
    gost = Gosti.findGost(brSobe)
    if len(gost) == 0:
        print("Nema gosta u toj sobi")
    else:
        print(Gosti.foramtHeader())
        print(Gosti.formatGost(gost))
    

def printRacun():
    print("[6] Prikazi racun:\n")
    print(Gosti.printRacun())
        
def printGrafik():
    print("[9] Broj gostiju po mesecu:\n")
    Gosti.printGrafik()
    
def mostDays():
    print("[7] Gost koji je najvise boravio u hotelu:\n")
    Gosti.mostDays()
    
def leastDays():
    print("[7] Gost koji je najmanje boravio u hotelu:\n")
    Gosti.leasttDays()

print("------Hotel Novi Sad------")

print(__name__)    
if __name__ == '__main__':
    main()