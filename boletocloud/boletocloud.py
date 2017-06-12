import requests


class Boleto(object):

    def __init__(self, token):
        self.__token = token

    @property
    def _token(self):
        return self.__token
