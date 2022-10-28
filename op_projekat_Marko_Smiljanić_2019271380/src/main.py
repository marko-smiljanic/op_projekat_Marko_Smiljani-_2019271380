from glavni_meni import *
from ucitavanje_podataka import *
from cuvanje_podataka import *
from student_meni import *
from profesor_meni import *


def jeste_student(korisnik):
    return 'ocene' in korisnik  # ako ima ocene, onda je student


predmeti = ucitaj_predmete()
profesori = ucitaj_profestore()
studenti = ucitaj_studente()

korisnik = None  # promenljiva u kojoj cuvamo trenutnog korisnika

izbor = input('''Glavni meni:
1. Prijava na sistem
2. Registracija
3. Izlazak iz aplikacije
> ''')
while izbor != '3':
    if izbor == '1':
        korisnik = prijava(studenti, profesori)
        if korisnik is None:
            print('Ne postoji korisnik sa unesenom kombinacijom korisnickog imena i lozinke!')
        if jeste_student(korisnik):
            izbor = input('''Student meni:
1. Racunanje globalne prosecne ocene
2. Prikaz polozenih i nepolozenih predmeta
3. Prikaz podataka o profesoru koji predaje predmet
4. Povratak na glavni meni
> ''')
            while izbor != '4':
                if izbor == '1':
                    racunanje_ocene(korisnik)
                elif izbor == '2':
                    prikaz_predmeta(korisnik, predmeti)
                elif izbor == '3':
                    prikaz_profesora(studenti, predmeti, profesori)
                else:
                    print('Izabrali se nepostojeću opciju! Pokušajte ponovo.')
                izbor = input('''Student meni:
1. Racunanje globalne prosecne ocene
2. Prikaz polozenih i nepolozenih predmeta
3. Prikaz podataka o profesoru koji predaje predmet
4. Povratak na glavni meni
> ''')
            korisnik = None  # korisnik zavrsio sa radom; izlogujemo se
        else:  # ako nije student ni None, onda je profesor!
            izbor = input('''Profesor meni:
1. Dodavanje ocene studentu
2. Brisanje ocene studentu
3. Računanje prosečne ocene za predmet
4. Promena termina konsultacija
5. Povratak na glavni meni
> ''')
            while izbor != '5':
                if izbor == '1':
                    studenti = dodavanje_ocene(korisnik, studenti, predmeti)
                    sacuvaj_sudente(studenti)
                elif izbor == '2':
                    studenti = brisanje_ocene(korisnik, studenti)
                    sacuvaj_sudente(studenti)
                elif izbor == '3':
                    prosecna_ocena(korisnik, studenti, predmeti)
                elif izbor == '4':
                    profesori = promena_termina(korisnik, profesori)
                    sacuvaj_profesore(profesori)
                else:
                    print('Izabrali se nepostojeću opciju! Pokušajte ponovo.')
                izbor = input('''Profesor meni:
1. Dodavanje ocene studentu
2. Brisanje ocene studentu
3. Računanje prosečne ocene za predmet
4. Promena termina konsultacija
5. Povratak na glavni meni
> ''')
            korisnik = None
    elif izbor == '2':
        studenti, profesori = registracija(studenti, profesori)
        sacuvaj_sudente(studenti)
        sacuvaj_profesore(profesori)
    else:
        print('Izabrali se nepostojeću opciju! Pokušajte ponovo.')
    izbor = input('''Glavni meni:
1. Prijava na sistem
2. Registracija
3. Izlazak iz aplikacije
> ''')