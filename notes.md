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


#
#on command line
heroku login  # befor creating an app make sure you are logged in
heroku create 
heroku git:remote -a app_name
heroku config:set DISABLE_COLLECTSTATIC=1
git push heroku master
heroku ps:scale web=1
heroku open
dj-database-url==0.5.0
pipenv install whitenoise==3.3.1

#In settings.py
'whitenoise.runserver_nostatic', # new! { in installed_apps}
'whitenoise.middleware.WhiteNoiseMiddleware', # new! { in middle_ware}

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # new!
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' # ne\
w!


#on command line
git add -A
git commit -m 'Heroku config'
git push origin master
git push heroku master


#On command line
pipenv install dj-database-url==0.5.0
pipenv install psycopg2==2.7.4

heroku config:set DJANGO_SECRET_KEY=`sdjnsniodnsdoisdndjnjcndks`
heroku addons | grep -i POSTGRES
heroku run python manage.py makemigrations
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
