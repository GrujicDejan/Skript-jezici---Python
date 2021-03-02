def stringToRec(line):
    ime, prezime, username, password = line.split("|")
    rec = {
            "ime": ime, 
           "prezime": prezime, 
           "username": username, 
           "password": password
           }
    return rec

def login(username, password):
    for rec in recepcionari:
        if rec["username"] == username and rec["password"] == password:
            return True
    return False

def loadRec():
    for line in open("recepcija.txt", "r").readlines():
        if len(line) > 1:
            rec = stringToRec(line[:-1])
            recepcionari.append(rec)
        
recepcionari = []
loadRec()
