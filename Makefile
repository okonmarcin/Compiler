regenerate-requirements:
	pip-compile -r ./requirements/requirements.in
	pip install -r ./requirements/requirements.txt

format:
	ruff format .

mypy:
	mypy .
