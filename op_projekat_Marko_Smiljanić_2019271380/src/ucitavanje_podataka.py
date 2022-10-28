import json


def ucitaj_predmete():
    predmeti = dict()
    try:
        fajl_predmeti = open('../data/predmeti.csv', encoding='UTF-8')  # ../ je povratak iz src foldera
    except FileNotFoundError:
        print('Ne postoji fajl: ../data/predmeti.csv')
        return predmeti
    linije_teksta = fajl_predmeti.readlines()
    fajl_predmeti.close()
    for linija_teksta in linije_teksta[1:]:  # preskocimo zaglavlje
        podaci = linija_teksta.split(';')   # rezultat je niz od dva stringa koja su bila razdvojena sa ';'
        sifra = podaci[0]
        naziv = podaci[1].strip()  # brise znakove za prelazak u novi red iz naziva
        predmeti[sifra] = naziv  # znamo da su sifre jedinstvene
    return predmeti


def ucitaj_profestore():
    profesori = list()
    try:
        fajl_profesori = open('../data/profesori.csv', encoding='UTF-8')
    except FileNotFoundError:
        print('Ne postoji fajl: ../data/profesori.csv')
        return profesori
    linije_teksta = fajl_profesori.readlines()
    fajl_profesori.close()
    for linija_teksta in linije_teksta:
        podaci = linija_teksta.split('-')
        sifra = podaci[0]
        lozinka = podaci[1]
        ime = podaci[2]
        prezime = podaci[3]
        email = podaci[4]
        termin = podaci[5] + '-' + podaci[6]
        profesor = {
            'sifra': sifra,
            'lozinka': lozinka,
            'ime': ime,
            'prezime': prezime,
            'email': email,
            'termin': termin
        }
        profesori.append(profesor)
    return profesori


def ucitaj_studente():
    studenti = list()
    try:
        fajl_studenti = open('../data/studenti.json', encoding='UTF-8')
    except FileNotFoundError:
        print('Ne postoji fajl: ../data/studenti.json')
        return studenti
    studenti = json.load(fajl_studenti)
    fajl_studenti.close()
    return studenti
