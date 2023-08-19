install:
	poetry install
build:
	poetry build
	python3 -m pip install --user dist/*.whl --force-reinstall
lint:
	poetry run flake8