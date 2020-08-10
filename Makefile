PYTHONPATH := $(shell pwd)

test:
	@echo "----running tests"
	@python -m pytest --setup-show --verbose --color=yes --disable-pytest-warnings tests/

run_gunicorn:
	@echo "----running"
	@PYTHONPATH="${PYTHONPATH}" FLASK_ENV=development python app.py

run_dev:
	@echo "----running dev"
	@PYTHONPATH="${PYTHONPATH}" FLASK_ENV=development python app.py

docker_build:
	@echo "-----building docker image------"
	@docker build -t origin .

docker_run:
	@echo "-----running docker image------"
	@docker run -it --rm -p 8080:8080 origin

