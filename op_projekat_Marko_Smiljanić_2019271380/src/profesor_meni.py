def dodavanje_ocene(profesor, studenti, predmeti):
    ime_studenta = input('''Pretraga po imenu:
> ''')
    filtrirani_studenti = []
    for student in studenti:
        ime = student['ime'].lower()
        if ime.find(ime_studenta.lower()) != -1:
            filtrirani_studenti.append(student)
    if len(filtrirani_studenti) == 0:
        print('Nema studenata sa takvim imenom.')
        return studenti
    for i in range(len(filtrirani_studenti)):
        print('\t' + str(i + 1) + '.', filtrirani_studenti[i]['broj indeksa'],
              filtrirani_studenti[i]['ime'], filtrirani_studenti[i]['prezime'])
    broj_indeksa = input('''Unesite broj indeksa studenta:
> ''')
    try:
        broj_indeksa = int(broj_indeksa)
    except ValueError:
        print('Pogresan format indeksa!')
        return studenti
    izabrani_student = None
    for student in filtrirani_studenti:
        if student['broj indeksa'] == broj_indeksa:
            izabrani_student = student
            break
    if izabrani_student is None:
        print('Ne postoji student sa tim imenom i brojem indeksa!')
        return studenti
    rbr = 1
    for sifra, naziv in predmeti.items():
        print('\t' + str(rbr) + '.', sifra, naziv)
        rbr += 1
    sifra_predmeta = input('''Unesite sifru predmeta:
> ''')
    if sifra_predmeta not in predmeti:
        print('Uneli ste nepostojecu sifru predmeta!')
        return studenti
    print('Unesite ocenu za studenta', izabrani_student['ime'], izabrani_student['prezime'],
          'na predmetu', predmeti[sifra_predmeta], '(celi broj u opsegu od 5 do 10):')
    ocena = input('> ')
    try:
        ocena = int(ocena)
    except ValueError:
        print('Pogresan format ocene.')
        return studenti
    if ocena < 5 or ocena > 10:
        print('Pogresna vrednost ocene.')
        return studenti
    ocena = {
        'sifra_predmeta': sifra_predmeta,
        'sifra_profesora': profesor['sifra'],
        'ocena': ocena
    }
    izabrani_student['ocene'].append(ocena)
    return studenti


def brisanje_ocene(profesor, studenti):
    # isto kao prethodni zadatak
    ime_studenta = input('''Pretraga po imenu:
    > ''')
    filtrirani_studenti = []
    for student in studenti:
        ime = student['ime'].lower()
        if ime.find(ime_studenta.lower()) != -1:
            filtrirani_studenti.append(student)
    if len(filtrirani_studenti) == 0:
        print('Nema studenata sa takvim imenom.')
        return studenti
    for i in range(len(filtrirani_studenti)):
        print('\t' + str(i + 1) + '.', filtrirani_studenti[i]['broj indeksa'],
              filtrirani_studenti[i]['ime'], filtrirani_studenti[i]['prezime'])
    broj_indeksa = input('''Unesite broj indeksa studenta:
    > ''')
    try:
        broj_indeksa = int(broj_indeksa)
    except ValueError:
        print('Pogresan format indeksa!')
        return studenti
    izabrani_student = None
    for student in filtrirani_studenti:
        if student['broj indeksa'] == broj_indeksa:
            izabrani_student = student
            break
    if izabrani_student is None:
        print('Ne postoji student sa tim imenom i brojem indeksa!')
        return studenti
    ocene = []
    rbr = 0
    for ocena in izabrani_student['ocene']:
        if ocena['sifra_profesora'] == profesor['sifra']:
            print('\t' + str(rbr + 1) + '.', ocena['sifra_predmeta'], ocena['ocena'])
            ocene.append(ocena)
            rbr += 1
    izbor = input('''Unesite redni broj ocene:
> ''')
    try:
        izbor = int(izbor)
    except ValueError:
        print('Neispravan format rednog broja!')
        return studenti
    if izbor < 1 or izbor > len(ocene):
        print('Izbor ocene je van opsega!')
        return studenti
    ocena_za_brisanje = ocene[izbor - 1]
    izabrani_student['ocene'].remove(ocena_za_brisanje)
    return studenti


def prosecna_ocena(profesor, studenti, predmeti):
    rbr = 1
    sifre_predmeta = []
    for sifra, naziv in predmeti.items():
        print('\t' + str(rbr) + '.', sifra, naziv)
        sifre_predmeta.append(sifra)
    izbor = input('''Unesite redni broj predmeta:
> ''')
    try:
        izbor = int(izbor)
    except ValueError:
        print('Pogresan format rednog broja!')
        return
    if izbor < 1 or izbor > len(predmeti):
        print('Izbor predmeta je van opsega!')
        return
    sifra_predmeta = sifre_predmeta[izbor - 1]  # jer smo krenuli od 1!!!
    ocene_za_predmet = []
    for student in studenti:
        for o in student['ocene']:
            if o['sifra_predmeta'] == sifra_predmeta and o['sifra_profesora'] == profesor['sifra']:
                ocene_za_predmet.append(o)
    if len(ocene_za_predmet) == 0:
        print('Niste uneli nijednu ocenu za taj predmet.')
        return
    suma = 0
    for o in ocene_za_predmet:
        suma += o['ocena']
    prosek = suma / len(ocene_za_predmet)
    print('Prosecna ocena za taj predmet je:', round(prosek, 2))


def promena_termina(profesor, profesori):
    print('Trenutni termin konsultacija:', profesor['termin'])
    termin = input('''Unesite novi termin konsultacija:
> ''')
    if len(termin) == 0:
        return profesori
    profesor['termin'] = termin
    for i in range(len(profesori)):
        if profesori[i]['sifra'] == profesor['sifra']:
            profesori[i] = profesor
    return profesori
