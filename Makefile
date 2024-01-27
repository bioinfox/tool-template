install:
	pip3 install -r requirements.txt

run:
	python3 -m api

test:
	python3 -m unittest discover -s tests -p '*_test.py'
