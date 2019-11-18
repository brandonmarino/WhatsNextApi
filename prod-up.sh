cd eatthis
gunicorn whatsnextadmin.wsgi:application --bind 0.0.0.0:8000