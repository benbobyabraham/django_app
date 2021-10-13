heroku login
heroku create
heroku git:create -a django-01-forum

web: gunicorn django_forum.wsgi
heroku local

git push heroku master
--------------------------------------
heroku git:remote -a app
git push heroku main

