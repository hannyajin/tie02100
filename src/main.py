# -*- coding: utf-8 -*-
# Christina Talmo 229756 TIE-02100 Harjoitustyo (Itsenainen Opiskelu)
# url: https://www.cs.tut.fi/~johoh/K2015/@wrapper.shtml?harjoitustyot/ht/tehtavananto

class Osallistuja:
    __id = None # rinta numero
    __name = None # nimi
    __sid = None # sarja tunniste
    __map_series = {} # pisteet lajeittan - laji : pisteet

    # constructor
    def __init__(self, id, name, sid):
        self.__id = id
        self.__name = name
        self.__sid = sid

    # methods
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_sid(self):
        return self.__sid

    def set_points(self, series, points):
        self.__map_series[series] = points

    def toString(self):
        return "{} '{}' {} : {}".format(self.__id, self.__name, self.__sid, self.__points)

'''
Ohjelma lukee ensin tiedoston osallistujat.txt, tämän jälkeen tiedoston ottelu.txt ja viimeiseksi kaikki ne tiedostot, joiden nimet tiedostossa ottelu.txt on lueteltuina. Tiedostot luetaan em. luettelossa esitetyssä järjestyksessä.
'''

map_osallistujat = {} # map ossallistujoista
lajit = [] # lista lajeista

# luetaan lista
file_osallistujat = open("osallistujat.txt", "r+")
for line in file_osallistujat:
    s = line.split(";") # id ; nimi ; sarja
    o = Osallistuja( s[0], s[1], s[2] )
    map_osallistujat[ s[0] ] = o
file_osallistujat.close()

# luetaan ottelu tiedot
file_ottelut = open("ottelu.txt", "r+")
for line in file_ottelut:
    # pistetaan laji nimi talteen
    laji = line[:line.find(".txt")]
    lajit.append(laji)

    # pomitaan lajin tiedot taman tiedostosta
    # ja lisataan pisteet osallistjoille
    file_ottelu = open(line.strip(), "r+")
    for line in file_ottelu:
        s = line.split(";") # id ; pisteet
        map_osallistujat[ s[0] ].set_points(laji, s[1])

print map_osallistujat




