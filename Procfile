web: gunicorn flashcard.wsgi --log-file -
release: python manage.py migrate
release: python manage.py syncdb
release: python manage.py collectstatic
