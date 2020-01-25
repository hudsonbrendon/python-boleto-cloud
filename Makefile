install:
	pipenv run python setup.py install

test:
	pipenv run coverage run --source='.' tests/tests.py

dev:
	make install
	make test