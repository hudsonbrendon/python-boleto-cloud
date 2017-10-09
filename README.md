# Python Boleto Cloud

[![Build Status](https://travis-ci.org/hudsonbrendon/python-boleto-cloud.svg?branch=master)](https://travis-ci.org/hudsonbrendon/python-boleto-cloud)
[![Github Issues](http://img.shields.io/github/issues/hudsonbrendon/python-boleto-cloud.svg?style=flat)](https://github.com/hudsonbrendon/python-boleto-cloud/issues?sort=updated&state=open)
![MIT licensed](https://img.shields.io/badge/license-MIT-blue.svg)

![boletocloud](boleto.png)

Integração com a API do boletocloud.com

# Instalação

Você pode instalar a biblioteca através do pip:

```bash
$ pip install python-boleto-cloud
```
ou

```bash
$ python setup.py install
```

# Primeiros passos

Antes de começar a trabalhar com a biblioteca você precisa de um token de acesso, para isso crie uma conta na plataforma do boleto cloud e um token lhe será gerado, acesse: [https://app.boletocloud.com/usuario/cadastro](https://app.boletocloud.com/usuario/cadastro)

Com o token em mãos, você precisa criar uma instância da classe **Ticket** que será usada para fazer todos os procedimentos na plataforma:

```python
>>> from boletocloud import Ticket
```

```bash
>>> ticket = Ticket(<TOKEN>)
```

# Criar boleto

Com a instância criada é hora de criar o primeiro boleto, para isso, utilize a função **create** que recebe uma série de parâmetros, tas parâmetros podem ser conferidos aqui: [https://www.boletocloud.com/app/dev/api#boletos-criar-campos](https://www.boletocloud.com/app/dev/api#boletos-criar-campos)

```python
>>> ticket.create("237", "1234-5", "123456-0", "12", "DevAware Solutions", "15.719.277/0001-46", "59020-000", "RN", "Natal", "Lagoa Nova", "Avenida Hermes da Fonseca", "384", "Sala 2A, segundo andar", "2014-07-11", "2020-05-30", "EX1", "12345678906-P", "DM", "2000.43", "Alberto Santos Dumont", "111.111.111-11", "36240-000", "MG", "Santos Dumont", "Casa Na
tal", "BR-499", "s/n", "Sitio - Subindo  a serra", "Atenção - Não receber esse boleto")
```
Se tudo ocorrer bem, um arquivo em PDF chamado boleto.pdf será gerado no diretório onde o comando foi executado e também ficará disponível na sua interface de administração na plataforma, caso contrário, será retornado um json com o erro(s) referentes a solicitação.

# Pesquisar boleto

Se você precisar pesquisar por um boleto criado, utilize o método **search**, que recebe único e exclusivamente o token do boleto, os tokens ficam disponibilizados na sua área administrativa na plataforma.

```python
>>> ticket.search(<TICKET_TOKEN>)
```
Se tudo ocorrer bem, um arquivo em PDF chamado boleto.pdf será gerado no diretório onde o comando foi executado, caso contrário, será retornado um json com o erro(s) referentes a solicitação.

# Dependencias
- Python 3.5

# Licença
[MIT](http://en.wikipedia.org/wiki/MIT_License)
