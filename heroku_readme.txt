heroku login
heroku create
heroku git:create -a django-01-forum

web: gunicorn django_forum.wsgi
heroku local

git push heroku master
--------------------------------------

heroku git:remote -a app
git push heroku main
--------------------------------------
- Add gunicorn server and webworker procfile web: gunicorn django_forum.wsgi
- Add STATIC_ROOT and do python manage.py collectstatic
- Add whitenoise.middlewares.WhiteNoiseMiddleware for using static files on heroku
- Migrate from sqlite database to a postgres database and add USER
