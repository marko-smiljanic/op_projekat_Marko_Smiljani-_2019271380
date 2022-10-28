def prijava(studenti, profesori):
    korisnicko_ime = input('Unesite korisnicko ime: ')
    lozinka = input('Unesite lozinku: ')
    for profesor in profesori:
        if profesor['sifra'] == korisnicko_ime and profesor['lozinka'] == lozinka:
            return profesor
    try:
        korisnicko_ime = int(korisnicko_ime)
    except ValueError:
        return None
    for student in studenti:
        if student['broj indeksa'] == korisnicko_ime and student['lozinka'] == lozinka:
            return student
    return None


def registracija(studenti, profesori):
    p_ili_s = input('''Izaberite broj opcije:
1. Profesor
2. Student
> ''')
    if p_ili_s == '1':
        sifra = input('Unesite sifru profesora: ')
        try:
            celi_broj = int(sifra)  # da proverimo da li je tekst celi broj
        except ValueError:
            print('Pogresan format sifre!')
            return studenti, profesori  # vratimo bez izmena
        sifra_postoji = False  # ne sme da postoji duplikat!!!
        for profesor in profesori:
            if profesor['sifra'] == sifra:
                sifra_postoji = True  # nasli smo sifru
                break
        if sifra_postoji:
            print('Sifra vec postoji!')
            return studenti, profesori  # vratimo bez izmena
        lozinka = input('Unesite loziku: ')
        ime = input('Unesite ime profesora: ')
        prezime = input('Unesite prezime profesora: ')
        email = input('Unesite e-mail adresu profesora: ')  # proveriti e-mail?!
        termin = input('Unesite termin konsultacija: ')
        profesor = {
            'sifra': sifra,
            'lozinka': lozinka,
            'ime': ime,
            'prezime': prezime,
            'email': email,
            'termin': termin
        }
        profesori.append(profesor)
        return studenti, profesori  # vratimo sa izmenom
    elif p_ili_s == '2':
        broj_indeksa = input('Unesite broj indeksa: ')
        try:
            broj_indeksa = int(broj_indeksa)  # da proverimo da li je tekst celi broj
        except ValueError:
            print('Pogresan format broja indeksa!')
            return studenti, profesori  # vratimo bez izmena
        indeks_postoji = False  # ne sme da postoji duplikat!!!
        for student in studenti:
            if student['broj indeksa'] == broj_indeksa:
                indeks_postoji = True  # nasli smo broj indeksa
                break
        if indeks_postoji:
            print('Broj indeksa vec postoji!')
            return studenti, profesori  # vratimo bez izmena
        lozinka = input('Unesite loziku: ')
        ime = input('Unesite ime studenta: ')
        prezime = input('Unesite prezime studenta: ')
        email = input('Unesite e-mail adresu studenta: ')  # proveriti e-mail?!
        student = {
            'broj indeksa': broj_indeksa,
            'lozinka': lozinka,
            'ime': ime,
            'prezime': prezime,
            'email': email,
            'ocene': []
        }
        studenti.append(student)
        return studenti, profesori  # vratimo sa izmenom
    else:
        print('Izabrana opcija ne postoji!')
        return studenti, profesori  # prekidamo registraciju, nema izmena
