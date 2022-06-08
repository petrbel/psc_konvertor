from unittest import TestCase

from psc_konvertor import PscKonvertor


class PSCKonvertorTest(TestCase):

    def setUp(self):
        self.konvertor = PscKonvertor()

    def test_psc2okres(self):
        self.assertEqual(self.konvertor.psc2okres(26601), 'Beroun')
        self.assertEqual(self.konvertor.psc2okres(37833), 'Jindřichův Hradec')
        self.assertEqual(self.konvertor.psc2okres(28401), 'Kutná Hora')
        self.assertEqual(self.konvertor.psc2okres(74254), 'Nový Jičín')

    def test_okres2kraj(self):
        self.assertEqual(self.konvertor.okres2kraj('Beroun'), 'Středočeský kraj')
        self.assertEqual(self.konvertor.okres2kraj('Rakovník'), 'Středočeský kraj')
        self.assertEqual(self.konvertor.okres2kraj('Šumperk'), 'Olomoucký kraj')
        self.assertEqual(self.konvertor.okres2kraj('Žďár nad Sázavou'), 'Kraj Vysočina')

    def test_psc2kraj(self):
        self.assertEqual(self.konvertor.psc2kraj(26601), 'Středočeský kraj')
        self.assertEqual(self.konvertor.psc2kraj(37833), 'Jihočeský kraj')
        self.assertEqual(self.konvertor.psc2kraj(28401), 'Středočeský kraj')
        self.assertEqual(self.konvertor.psc2kraj(74254), 'Moravskoslezský kraj')

    def test_Praha_psc2okres(self):
        self.assertEqual(self.konvertor.psc2okres(25245), 'Praha-západ')
        self.assertEqual(self.konvertor.psc2okres(25170), 'Praha-východ')
        self.assertEqual(self.konvertor.psc2okres(19011), 'Hlavní město Praha')

    def test_Praha_okres2kraj(self):
        self.assertEqual(self.konvertor.okres2kraj('Praha-západ'), 'Středočeský kraj')
        self.assertEqual(self.konvertor.okres2kraj('Praha-východ'), 'Středočeský kraj')
        self.assertEqual(self.konvertor.okres2kraj('Hlavní město Praha'), 'Hlavní město Praha')

    def test_Praha_psc2kraj(self):
        self.assertEqual(self.konvertor.psc2kraj(25245), 'Středočeský kraj')
        self.assertEqual(self.konvertor.psc2kraj(25170), 'Středočeský kraj')
        self.assertEqual(self.konvertor.psc2kraj(19011), 'Hlavní město Praha')    