# -*- coding: utf-8 -*-
# Christina Talmo 229756 TIE-02100 Harjoitustyo (Itsenainen Opiskelu)
# url: https://www.cs.tut.fi/~johoh/K2015/@wrapper.shtml?harjoitustyot/ht/tehtavananto

class Osallistuja:
    __id = None # rinta numero
    __name = None # nimi
    __sid = None # sarja tunniste
    __points = 0 # pisteet

    def __init__(self, id, name, sid):
        self.__id = id
        self.__name = name
        self.__sid = sid

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_sid(self):
        return self.__sid

    def add_points(self, points):
        self.__points += points

    def get_points(self):
        return self.__points

'''
Ohjelma lukee ensin tiedoston osallistujat.txt, tämän jälkeen tiedoston ottelu.txt ja viimeiseksi kaikki ne tiedostot, joiden nimet tiedostossa ottelu.txt on lueteltuina. Tiedostot luetaan em. luettelossa esitetyssä järjestyksessä.
'''

osallistujat = open("osallistujat.txt", "r+");

print("filename: " + osallistujat.name);

for line in osallistujat:
    split = line.split(";")
    for str in split:
        print str,
