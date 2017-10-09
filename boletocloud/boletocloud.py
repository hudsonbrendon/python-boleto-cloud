import requests

from requests.auth import HTTPBasicAuth

from .utils import write_pdf


class Ticket(object):
    '''Cria a instância de um boleto'''

    def __init__(self, token):
        self.__token = token
        self.__url = 'https://sandbox.boletocloud.com/api/v1/boletos{}'

    @property
    def _token(self):
        return self.__token

    @property
    def _authorization(self):
        auth = HTTPBasicAuth(self._token, 'token')
        return auth

    def _get_url(self, params=''):
        return self.__url.format(params)

    def create(self, conta_banco, conta_agencia, conta_numero, conta_carteira, beneficiario_nome, beneficiario_cprf,
               beneficiario_endereco_cep, beneficiario_endereco_uf, beneficiario_endereco_localidade,
               beneficiario_endereco_bairro, beneficiario_endereco_logradouro, beneficiario_endereco_numero,
               beneficiario_endereco_complemento, emissao, vencimento, documento, numero, titulo, valor,
               pagador_nome, pagador_cprf, pagador_endereco_cep, pagador_endereco_uf, pagador_endereco_localidade,
               pagador_endereco_bairro, pagador_endereco_logradouro, pagador_endereco_numero, pagador_endereco_complemento,
               instrucao=None):
        '''Cria e retorna o boleto criado no formato PDF, para mais informações sobre esse recurso acesse:
           https://www.boletocloud.com/app/dev/api#boletos-criar

           Você pode encontrar a descrição de todos os parâmetros na documentação da API, acesse:
           https://boletocloud.com/app/dev/api#boletos-criar-campos
        '''
        headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"}
        data = {
            'boleto.conta.banco': conta_banco,
            'boleto.conta.agencia': conta_agencia,
            'boleto.conta.numero': conta_numero,
            'boleto.conta.carteira': conta_carteira,
            'boleto.beneficiario.nome': beneficiario_nome,
            'boleto.beneficiario.cprf': beneficiario_cprf,
            'boleto.beneficiario.endereco.cep': beneficiario_endereco_cep,
            'boleto.beneficiario.endereco.uf': beneficiario_endereco_uf,
            'boleto.beneficiario.endereco.localidade': beneficiario_endereco_localidade,
            'boleto.beneficiario.endereco.bairro': beneficiario_endereco_bairro,
            'boleto.beneficiario.endereco.logradouro': beneficiario_endereco_logradouro,
            'boleto.beneficiario.endereco.numero': beneficiario_endereco_numero,
            'boleto.beneficiario.endereco.complemento': beneficiario_endereco_complemento,
            'boleto.emissao': emissao,
            'boleto.vencimento': vencimento,
            'boleto.documento': documento,
            'boleto.numero': numero,
            'boleto.titulo': titulo,
            'boleto.valor': valor,
            'boleto.pagador.nome': pagador_nome,
            'boleto.pagador.cprf': pagador_cprf,
            'boleto.pagador.endereco.cep': pagador_endereco_cep,
            'boleto.pagador.endereco.uf': pagador_endereco_uf,
            'boleto.pagador.endereco.localidade': pagador_endereco_localidade,
            'boleto.pagador.endereco.bairro': pagador_endereco_bairro,
            'boleto.pagador.endereco.logradouro': pagador_endereco_logradouro,
            'boleto.pagador.endereco.numero': pagador_endereco_numero,
            'boleto.pagador.endereco.complemento': pagador_endereco_complemento,
            'boleto.instrucao': instrucao
        }
        ticket = requests.post(self._get_url(), auth=self._authorization, data=data, headers=headers)
        if ticket.status_code is 201:
            write_pdf(ticket)
        else:
            return ticket.json()

    def search(self, token_ticket):
        '''Retorna um boleto no formato PDF, para mais informações sobre esse recurso acesse:
           https://www.boletocloud.com/app/dev/api#boletos-buscar

           Parâmetros:
           - token_ticket - Ticket do boleto a ser pesquisado.
        '''
        headers = {'content-type': 'application/pdf'}

        ticket = requests.get(self._get_url('/{}'.format(token_ticket)), auth=self._authorization, headers=headers)
        if ticket.status_code is 200:
            write_pdf(ticket)
        else:
            return ticket.json()
