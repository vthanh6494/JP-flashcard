web: gunicorn flashcard.wsgi --log-file -
release: python manage.py migrate
release: python manage.py createsuperuser
release: python manage.py collectstatic
