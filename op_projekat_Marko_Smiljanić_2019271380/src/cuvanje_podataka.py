import json


def sacuvaj_predmete():
    pass


def sacuvaj_profesore(profesori):
    fajl_profesori = open('../data/profesori.csv', 'w', encoding='UTF-8')
    for profesor in profesori:
        string = ""
        for podatak in profesor.values():
            string += podatak + '-'
        # imamo '-' viska na kraju
        string = string[:-2]
        fajl_profesori.write(string)
    fajl_profesori.close()


def sacuvaj_sudente(studenti):
    fajl_studenti = open('../data/studenti.json', 'w', encoding='UTF-8')
    studenti_json = json.dumps(studenti)
    fajl_studenti.write(studenti_json)
    fajl_studenti.close()
