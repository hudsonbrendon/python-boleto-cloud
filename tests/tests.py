import unittest

from boletocloud import Ticket

from decouple import config


class TicketTestCase(unittest.TestCase):

    def setUp(self):
        self.ticket = Ticket(config('TOKEN'))

    def test_create_ticket(self):
        self.assertTrue(isinstance(self.ticket, Ticket))

    def test_token(self):
        self.assertEqual(self.ticket._token, config('TOKEN'))

    def test_url(self):
        self.assertEqual(self.ticket._get_url('test/'), 'https://sandbox.boletocloud.com/api/v1/boletos/test/')

    def test_authorization(self):
        self.assertEqual(self.ticket._authorization.username, config('TOKEN'))
        self.assertEqual(self.ticket._authorization.password, 'token')


if __name__ == '__main__':
    unittest.main()
