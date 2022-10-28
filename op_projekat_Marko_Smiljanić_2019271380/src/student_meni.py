def racunanje_ocene(student):
    suma = 0
    for o in student['ocene']:
        suma += o['ocena']
    prosek = suma / len(student['ocene'])
    print("Prosecna ocena je: " + str(round(prosek, 2)))


def prikaz_predmeta(student, predmeti):
    opcija = input('''Izaberite predmete koje zelite da se prikazu:
1. Polozeni
2. Nepolozeni
> ''')
    if opcija == '1':
        for o in student['ocene']:
            if o['ocena'] > 5:
                sifra = o['sifra_predmeta']
                print('\t' + predmeti[sifra])  # predmeti su recnik organizovan po sifri
    elif opcija == '2':
        for sifra in predmeti:
            polozen = False  # pretpostavimo da nije
            for o in student['ocene']:
                if o['sifra_predmeta'] == sifra and o['ocena'] > 5:
                    polozen = True  # skontamo da jeste
                    break  # prekinemo pretragu
            if not polozen:
                print('\t' + predmeti[sifra])
    else:
        print('Izabrana opcija ne postoji!')


def prikaz_profesora(studenti, predmeti, profesori):
    print('Unesite sifru predmeta:')
    for sifra, naziv in predmeti.items():
        print('\t' + sifra + '. ' + naziv)
    sifra_predmeta = input('>')
    if sifra_predmeta not in predmeti:
        print('Uneli ste nepostojecu sifru!')
        return
    sifre_profesora = set()  # necemo istog profesora da dodamo vise puta
    for student in studenti:
        for o in student['ocene']:
            if o['sifra_predmeta'] == sifra_predmeta:
                sifre_profesora.add(o['sifra_profesora'])
    if len(sifre_profesora) == 0:
        print('Nijedan profesor ne predaje taj predmet.')
    else:
        for sp in sifre_profesora:
            for profesor in profesori:
                if profesor['sifra'] == sp:
                    print('\t' + profesor['ime'] + ' ' + profesor['prezime'],
                          profesor['email'], profesor['termin'], sep=', ')
