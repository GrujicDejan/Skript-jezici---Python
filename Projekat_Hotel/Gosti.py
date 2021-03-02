import matplotlib.pyplot as plt
import numpy as np
import random

def loadGosti():
    for line in open("gosti.txt", "r").readlines():
        if len(line) > 1:
            gost = stringToGost(line)
            gosti.append(gost)
            
    
def saveGost():
    file = open("gosti.txt", "w")
    for gost in gosti:
        file.write(gostToString(gost))
        file.write("\n")
    file.close
    
def gostToString(gost):
    return "|".join((gost["brSobe"], 
                     gost["ime"],
                     gost["prezime"],
                     gost["email"], 
                     gost["brTel"], 
                     gost["brDana"], 
                     gost["datum1"], 
                     gost["datum2"], 
                     gost["cenaS"]))

def stringToGost(line):
    if line[-1] == '\n':
        line = line[:-1]
    brSobe, ime, prezime, mail, brTel, brDana, datum1, datum2, cenaS = line.split("|")
    gost = {
        "brSobe": brSobe,
        "ime": ime,
        "prezime": prezime,
        "email": mail,
        "brTel": brTel,
        "brDana": brDana,
        "datum1": datum1,
        "datum2": datum2,
        "cenaS": cenaS
    }
    return gost


def addGost(gost):
    gosti.append(gost)
    
def foramtHeader():
    return \
        "Broj sobe |Ime         |Prezime     |E-mail                        |Broj telefona  |Dana boravka|Od dana     |Do dana     |Dugovanje € \n"\
        "----------+------------+------------+------------------------------+---------------+------------+------------+------------+------------"
    
def formatGost(gost):
    return "{0:10}|{1:12}|{2:12}|{3:30}|{4:15}|{5:12}|{6:12}|{7:12}|{8:12}".format(
        gost["brSobe"],
        gost["ime"],
        gost["prezime"],
        gost["email"],
        gost["brTel"],
        gost["brDana"],
        gost["datum1"],
        gost["datum2"],
        gost["cenaS"]
    )
    
def formatGosti(gosti):
    lista = ""
    for gost in gosti:
        lista += formatGost(gost) + "\n"
    return lista

def listGost():
    return formatGosti(gosti)

def ukupnaCena(broj, brDana):
    if eval(broj) <= 9:
        cena = 10
    elif eval(broj) >= 10 and eval(broj) <=16:
        cena = 15
    else:
        cena = 20
    ukupno = cena * brDana
    return ukupno
    
def printRacun():
    brSobe = input("Unesite broj sobe za koju zelite da izdate racun >> ")
    for gost in gosti:
        if gost["brSobe"] == brSobe:
            return "Racun gosta " + gost["ime"] + " " + gost["prezime"] + " je " + gost["cenaS"] + "€"
    print("Ne postoji gost u toj sobi.")
    printRacun()
    
def findGost(brSobe):
    for gost in gosti:
        if gost["brSobe"].upper() == brSobe.upper():
            return gost
    print("Ne postoji gost u toj sobi.")

def addDan():
    brSobe = input("Unesite broj sobe u kom se nalazi gost >> ")
    for gost in gosti:
        if gost["brSobe"].upper() == brSobe.upper():
             brDana = input("Unesite za koliko dana zelite da produzite boravak >> ")
             cenaS = int(int(gost["cenaS"]) / int(gost["brDana"]))
             gost["cenaS"] = str(int(gost["cenaS"]) + int(cenaS) * int(brDana))
             gost["brDana"] = str(int(gost["brDana"]) + int(brDana))
             gost["datum2"] = unesiDatum2(gost["datum1"], int(gost["brDana"]))
             return saveGost()
         
    print("Ne postoji gost u toj sobi.")
    return addDan()
        
def updateInfo(brSobe, key, value):
    for gost in gosti:
        if gost["brSobe"].upper() == brSobe.upper():
            gost[key] = value
            return saveGost()
    print("Ne postoji gost u toj sobi.")
    
def unesiDatum1():
    datum = input("Unesite datum useljenja >> ")
    dan, mesec, godina = datum.split(".")
    if int(dan) < 1:
        print("Niste uneli ispravan datum.")
        return unesiDatum1()
    if mesec in ("1", "3", "5", "7", "8", "10", "12"):
        if int(dan) > 31:
            print("Niste uneli ispravan datum.")
            return unesiDatum1()
    elif int(mesec) == 2:
        if int(godina) % 4 == 0 and (int(godina) % 100 != 0 or int(godina) % 400 == 0):
            if int(dan) > 28:
                print("Niste uneli ispravan datum.")
                return unesiDatum1()
        else:
            if int(dan) > 27:
                print("Niste uneli ispravan datum.")
                return unesiDatum1()
    else:
        if int(dan) > 30:
            print("Niste uneli ispravan datum.")
            return unesiDatum1()
    if int(mesec) > 12 or int(mesec) < 1:
        print("Niste uneli ispravan datum.")
        return unesiDatum1()
    if int(godina) < 2019:
        print("Niste uneli ispravan datum.")
        return unesiDatum1()
    return datum

def unesiDatum2(datum1, brDana):
    dan1, mesec1, godina1 = datum1.split(".")
    dan2 = str(int(dan1) + brDana)
    mesec2 = mesec1
    godina2 = godina1
    if mesec2 in ("1", "3", "5", "7", "8", "10", "12"):
        if int(dan2) > 31:
            mesec2 = str(int(mesec2) + 1)
            dan2 = str(int(dan2) - 31)
    elif int(mesec2) == 2:
        if (int(godina2) % 4 == 0 and (int(godina2) % 100 != 0 or int(godina2) % 400 == 0)):
            if int(dan2) > 29:
                mesec2 = str(int(mesec2) + 1)
                dan2 = str(int(dan2) - 28)
        else:
            if int(dan2) > 28:
                mesec2 = str(int(mesec2) + 1)
                dan2 = str(int(dan2) - 28)
    else:
        if int(dan2) > 30:
            mesec2 = str(int(mesec2) + 1)
            dan2 = str(int(dan2) - 30)
    if int(mesec2) > 12:
        mesec2 = str(int(mesec2) - 12)
        godina2 = str(int(godina2) + 1)
    datum2 = dan2 + "." + mesec2 + "." + godina2
    return datum2

def gostPoMesecu():
    januar = februar = mart = april = maj = jun = jul = avgust = septembar = oktobar = novembar = decembar = 0
    januar2 = februar2 = mart2 = april2 = maj2 = jun2 = jul2 = avgust2 = septembar2 = oktobar2 = novembar2 = decembar2 = 0
    for gost in gosti:
        dan, mesec, godina = gost["datum1"].split(".")
        dan2, mesec2, godina2 = gost["datum2"].split(".")
        if mesec == "1":
            januar += 1
        elif mesec == "2":
            februar += 1
        elif mesec == "3":
            mart += 1
        elif mesec == "4":
            april += 1
        elif mesec == "5":
            maj += 1
        elif mesec == "6":
            jun += 1
        elif mesec == "7":
            jul += 1
        elif mesec == "8":
            avgust += 1
        elif mesec == "9":
            septembar += 1
        elif mesec == "10":
            oktobar += 1
        elif mesec == "11":
            novembar += 1
        elif mesec == "12":
            decembar += 1   
        
        if mesec2 == "1":
            januar2 += 1
        elif mesec2 == "2":
            februar2 += 1
        elif mesec2 == "3":
            mart2 += 1
        elif mesec2 == "4":
            april2 += 1
        elif mesec2 == "5":
            maj2 += 1
        elif mesec2 == "6":
            jun += 1
            jun2 += 1
        elif mesec2 == "7":
            jul2 += 1
        elif mesec2 == "8":
            avgust2 += 1
        elif mesec2 == "9":
            septembar2 += 1
        elif mesec2 == "10":
            oktobar2 += 1
        elif mesec2 == "11":
            novembar2 += 1
        elif mesec2 == "12":
            decembar2 += 1
    gPmU = [januar, februar, mart, april, maj, jun, jul, avgust, septembar, oktobar, novembar, decembar]
    gPmI = [januar2, februar2, mart2, april2, maj2, jun2, jul2, avgust2, septembar2, oktobar2, novembar2, decembar2]
    return gPmU, gPmI
  
          

def printGrafik():
    x1 = np.arange(12)
    x2 = [x + 0.35/2 for x in x1]
    
    y1,y2 = gostPoMesecu()

    plt.bar(x1 - 0.35/2, y1, color='blue', width=0.35, edgecolor='white', label='Useljenje')
    plt.bar(x2, y2, color='red', width=0.35, edgecolor='white', label='Iseljenje')
    plt.xticks([r for r in range(12)], ["januar", "februar", "mart", "april", "maj", "jun", "jul", "avgust", "septembar", "oktobar", "novembar", "decembar"])
    plt.xlabel('meseci')
    plt.xticks(rotation=90)
    plt.ylabel('broj gostiju')
    if max(y1) > max(y2):
        maks = max(y1)
    else:
        maks = max(y2)
    plt.ylim(ymin=0, ymax=maks+1)
    plt.legend()
    plt.show()
    
def mostDays():
    maxD = 0
    for gost in gosti:
        if int(gost["brDana"]) > maxD:
            maxD = int(gost["brDana"])
            g = gost
    g = []
    for gost in gosti:
        if int(gost["brDana"]) == maxD:
            g.append(gost)
    if len(g) == 1:
        for gost in g:
            print("Gost " + gost["ime"] + " " + gost["prezime"] + " je boravio najvise dana u hotelu")
    else:
        print("Gosti koji su boravili najduze u hotelu su:")
        for gost in g:
            print(gost["ime"] + " " + gost["prezime"])

def leasttDays():
    minD = 100
    for gost in gosti:
        if int(gost["brDana"]) < minD:
            minD = int(gost["brDana"])
    g = []
    for gost in gosti:
        if int(gost["brDana"]) == minD:
            g.append(gost)
    if len(g) == 1:
        for gost in g:
            print("Gost " + gost["ime"] + " " + gost["prezime"] + " je boravio najmanje dana u hotelu")
    else:
        print("Gosti koji su boravili najmanje u hotelu su:")
        for gost in g:
            print(gost["ime"] + " " + gost["prezime"])
                
            
def dodeliSobu():
    print("Izaberite sobu: ")
    print("1 - jednokrevetna")
    print("2 - dvokrevetna")
    print("3 - trokrevetna")
    soba = input("Izbor >> ")
    if soba == '1':
        broj = random.randint(1, 9)
    elif soba == '2':
        broj = random.randint(9,16)
    else:
        broj = random.randint(16, 20)
    return str(broj)
        
    
        
    
            
        

gosti = []
loadGosti()