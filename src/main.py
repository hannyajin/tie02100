# -*- coding: utf-8 -*-
# Christian Talmo 229756 TIE-02100 Harjoitustyo (Itsenainen Opiskelu)
# url: https://www.cs.tut.fi/~johoh/K2015/@wrapper.shtml?harjoitustyot/ht/tehtavananto
# repo: https://github.com/hannyajin/tie02100

class Osallistuja:
    __id = None # rinta numero
    __name = None # nimi
    __sid = None # sarja tunniste
    __map_series = None # pisteet lajeittan - laji : pisteet

    # constructor
    def __init__(self, id, name, sid):
        self.__id = id
        self.__name = name
        self.__sid = sid
        self.__map_series = {}

    # methods
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_sid(self):
        return self.__sid

    def set_points(self, series, points):
        self.__map_series[series] = points

    def get_points(self, series):
        if series in self.__map_series:
            return self.__map_series.get(series)
        else:
            return None

    def toString(self):
        return "{} '{}' {} : {}".format(self.__id, self.__name, self.__sid, self.__map_series)
def main():

    # apu funktio
    def is_num(n):
        try:
            float(n)
            return True
        except:
            return False

    '''
    Ohjelma lukee ensin tiedoston osallistujat.txt, tämän jälkeen tiedoston ottelu.txt ja viimeiseksi kaikki ne tiedostot, joiden nimet tiedostossa ottelu.txt on lueteltuina. Tiedostot luetaan em. luettelossa esitetyssä järjestyksessä.
    '''

    map_osallistujat = {} # map ossallistujoista
    lajit = [] # lista lajeista

    # luetaan lista
    try:
        file_osallistujat = open("osallistujat.txt", "r")
    except:
        print ("Virhe osallistujatiedoston lukemisessa.")
        return -1

    for line in file_osallistujat:
        s = line.strip().split(";") # id ; nimi ; sarja
        if (len(s) != 3):
            print ("Virheellinen osallistujatiedosto: rivi '"
                    + line.strip() +
                    "' ei ole muodossa tunnus;nimi;sarja.")
            return -1

        if (s[0] in map_osallistujat):
            print ("Virheellinen osallistujatiedosto: tunnus "
                    + s[0] + " toistuu.")
            return -1

        o = Osallistuja( s[0], s[1], s[2] )
        map_osallistujat[ s[0] ] = o
    file_osallistujat.close()

    # luetaan ottelu tiedot
    try:
        file_ottelut = open("ottelu.txt", "r")
    except:
        print ("Virhe ottelutiedoston lukemisessa.")
        return -1

    for line in file_ottelut:
        # pistetaan laji nimi talteen
        laji = line[:line.find(".txt")]
        lajit.append(laji)

        # pomitaan lajin tiedot taman tiedostosta
        # ja lisataan pisteet osallistjoille
        try:
            file_ottelu = open(line.strip(), "r")
        except:
            print ("Virhe lajitiedoston " + line.strip() + " lukemisessa.")
            return -1

        for subline in file_ottelu:
            s = subline.strip().split(";") # id ; pisteet
            if (len(s) != 2 or not is_num(s[1])):
                print ("Virheellinen lajitiedosto "
                        + line.strip() + ": rivi '" + subline.strip() +
                        "' ei ole muodossa tunnus;pisteet.")
                return -1

            if not (s[0] in map_osallistujat):
                print ("Virheellinen lajitiedosto "
                        + line.strip() + ": tunnus "
                        + s[0] + " puuttuu osallistujatiedostosta.")
                return -1

            o = map_osallistujat[ s[0] ]

            if (o.get_points(laji) != None):
                print ("Virheellinen lajitiedosto "
                        + line.strip() + ": tunnus " + s[0] + " toistuu.")
                return -1

            o.set_points(laji, s[1])
        file_ottelu.close()
    file_ottelut.close()


    '''
    Syötetiedostot luettuaan ohjelma tulostaa CSV-muotoisen tiedoston tulokset.txt, johon tulee otsikkorivi sekä yksi rivi kutakin osallistujat.txt-tiedostossa ollutta osallistujaa kohden. Rivin alkuun tulevat osallistujan perustiedot osallistujat.txt-tiedostosta, sen jälkeen jokaisen lajin pistetiedot ja loppuriville tulee vielä yhteenvetotietoja kilpailijan koko seitsenottelusta.
    '''

    tulokset = []

    '''
    Otsikkorivin sisältö muodostuu seuraavasti: Ensimmäiseksi tulevat sarakkeet tunnus, nimi ja sarja, tämän jälkeen sarake jokaiselle lajille, ja lopuksi sarakkeet kokonaispisteet sekä lajeja. Oletetaan, että lajitiedostojen nimet ovat .txt-päätteisiä. Tulostiedoston otsikkorivillä käytetään lajin nimenä tiedoston nimen alkuosaa.
    '''
    str_otsikkorivi = "tunnus;nimi;sarja"
    for laji in lajit:
        str_otsikkorivi += (";" + laji)
    str_otsikkorivi += ";kokonaispisteet;lajeja"

    '''
    Kunkin osallistujan riville tulee ensimmäisiin kolmeen sarakkeeseen tiedostosta osallistujat.txt luetut tiedot. Lajisarakkeisiin tulevat muista syötetiedostoista luetut pistemäärät aina asiaankuuluvan otsikon alle, tai jos kilpailijalta puuttuu suoritus kyseisestä lajista, merkitään sarakkeeseen "-". Rivin loppuun tulevat:

        * sarakkeeseen kokonaispistemäärä kilpailijan suorittamien lajien pistemäärien summa
        * sarakkeeseen lajeja suoritettujen lajien lukumäärä ja lajien kokonaislukumäärä merkkijonona, jossa niiden välissä on merkki "/" eli esimerkiksi "6/7", jos kilpailija on suorittanut kuusi lajia seitsemästä.
    '''
    for key in map_osallistujat.keys():
        o = map_osallistujat.get(key)
        ostr = ("" + o.get_id() + ";" + o.get_name() + ";" + o.get_sid())
        total_points = 0;
        total_series = 0;
        for laji in lajit:
            p = o.get_points(laji)
            if p:
                total_points += float(p)
                total_series += 1
                ostr += (";" + str(float(p)))
            else:
                ostr += ";-"
        ostr += (";" + str(total_points))
        ostr += (";" + str(total_series) + "/" + str(len(lajit)))
        tulokset.append( ostr )

    tulokset = sorted(tulokset)

    try:
        file_tulokset = open("tulokset.txt", "w")
        file_tulokset.write( str_otsikkorivi + '\n' )
        for line in tulokset:
            file_tulokset.write( line + '\n' )
        file_tulokset.close()
        print ("Tulokset kirjoitettu tiedostoon tulokset.txt.")
    except:
        print ("Virhe tulostiedoston kirjoittamisessa.")
        return -1

    return 0 # exit success


# run program
if __name__ == "__main__":
    main()
