# Pipfile
[requires]
python_version = "3.6"

#On the command line
pipenv lock
touch Procfile

#On Procfile
web: gunicorn mysite.wsgi --log-file -


#On Command Line
pipenv install gunicorn

#In Settings.py
ALLOWED_HOSTS = ['*]