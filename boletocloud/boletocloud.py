import requests

from requests.auth import HTTPBasicAuth


class Boleto(object):

    def __init__(self, token):
        self.__token = token

    @property
    def _token(self):
        return self.__token

    def criar(self):
        pass
        
    def buscar(self):
        pass
