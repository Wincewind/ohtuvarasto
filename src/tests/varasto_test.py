import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_setup(self):
        self.varasto = Varasto(-10, -10)
        self.assertEqual((self.varasto.saldo, self.varasto.tilavuus), (0,0))

    def test_saldo_gt_tilavuus_setup(self):
        self.varasto = Varasto(10, 100)
        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_lisaa_negatiivinen_varastoon(self):
        saldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-5)
        self.assertEqual(self.varasto.saldo, saldo)

    def test_lisaa_enemman_kuin_mahtuu(self):
        self.varasto.lisaa_varastoon(self.varasto.tilavuus+10)
        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ota_negatiivinen_varastosta(self):
        saldo = self.varasto.saldo
        self.varasto.ota_varastosta(-5)
        self.assertEqual(self.varasto.saldo, saldo)

    def test_ota_enemman_kuin_saldo(self):
        self.varasto.ota_varastosta(self.varasto.saldo+10)
        self.assertEqual(self.varasto.saldo, 0)

    def test_str(self):
        self.assertEqual(str(self.varasto), 'saldo = ~, vielä tilaa 10')