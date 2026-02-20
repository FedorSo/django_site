pip freeze
python -m venv .venv
pip install django
.\.venv\Scripts\activate
pip install -r .\requirements.txt
pip freeze > requirements.txt
django-admin startproject djangosite .
python .\manage.py startapp blog
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser 