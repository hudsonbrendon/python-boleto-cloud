import os
import unittest

from boletocloud import Boleto


class TestBoleto(unittest.TestCase):

    def setUp(self):
        self.boleto = Boleto(os.environ.get('TOKEN'))

    def test_create_boleto(self):
        self.assertTrue(isinstance(self.boleto, Boleto))


if __name__ == '__main__':
    unittest.main()
