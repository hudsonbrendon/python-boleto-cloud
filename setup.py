from setuptools import setup


setup(name='python-boleto-cloud',
      version='0.1',
      description='Integração com a API do boletocloud.com',
      url='https://github.com/hudsonbrendon/python-boleto-cloud',
      author='Hudson Brendon',
      author_email='contato.hudsonbrendon@gmail.com',
      license='MIT',
      packages=['boletocloud'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
