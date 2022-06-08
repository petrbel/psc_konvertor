# -*- coding: utf-8 -*-

import os

import pandas

__author__ = 'Petr Belohlavek <me@petrbel.cz>'

print()

class PscKonvertor:
    """Konvertuje postovni smerovaci cisla na prislusne okresy a kraje.
       Vyhledavani je pro maximalni rychlost indexovane."""

    _MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
    _DATA_PATH = os.path.join(_MODULE_PATH, 'data')

    def __init__(self, psc2okres_f=os.path.join(_DATA_PATH, 'psc2okres.csv'),
                 okres2kraj_f=os.path.join(_DATA_PATH, 'okres2kraj.csv')):
        """CSV tabulky se sloupci PSC,Okres a Okres,Kraj. Volitelne mohou obsahovat i dalsi sloupce."""

        self.psc2okres_ = pandas.read_csv(psc2okres_f, header=0, encoding='utf-8')
        self.psc2okres_ = self.psc2okres_.set_index(['PSC'])

        self.okres2kraj_ = pandas.read_csv(okres2kraj_f, header=0, encoding='utf-8')
        self.okres2kraj_ = self.okres2kraj_.set_index(['Okres'])

    def psc2okres(self, psc):
        """Prevede `pcs` na okres, ve kterem dana obec lezi."""

        psc_zaznamy = self.psc2okres_.loc[psc]
        zaznam = {}

        if type(psc_zaznamy) == pandas.core.frame.DataFrame:
            zaznam = psc_zaznamy.iloc[0]
        elif type(psc_zaznamy) == pandas.core.series.Series:
            zaznam = psc_zaznamy
        else:
            raise KeyError('Unexpected type')

        return zaznam['Okres']

    def okres2kraj(self, okres):
        """Prevede `okres` na kraj, ve kterem dany okres lezi."""

        kraj_zaznam = self.okres2kraj_.loc[okres]
        return kraj_zaznam['Kraj']

    def psc2kraj(self, psc):
        """Prevede `pcs` na kraj, ve kterem dana obec lezi."""

        okres = self.psc2okres(psc)
        return self.okres2kraj(okres)
