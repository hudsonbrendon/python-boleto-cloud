black:
	pipenv run black .

install:
	pipenv run python setup.py install

test:
	pipenv run coverage run --source='.' tests/tests.py

coverage:
	pipenv run coverage report -m

dev:
	make black
	make install
	make test
	make coverage