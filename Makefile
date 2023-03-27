DJANGO_MANAGE=python test_task/manage.py
DJANGO_SETTINGS_MODULE=test_task.settings

install_requirements:
			python -m venv venv
			source venv/bin/activate
			pip install --upgrade pip
			pip install -r requirements.txt

runserver:
	$(DJANGO_MANAGE) runserver --settings=$(DJANGO_SETTINGS_MODULE)

migrate:
	$(DJANGO_MANAGE) makemigrations --settings=$(DJANGO_SETTINGS_MODULE)
	$(DJANGO_MANAGE) migrate --settings=$(DJANGO_SETTINGS_MODULE)