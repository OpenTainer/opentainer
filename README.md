Opentainer
==============

python manage.py makemigrations

python manage.py migrate

python manage.py runserver  

================

If you are using Django 1.7 then the server will through error "No module named security" unless you comment the line "django.middleware.security.SecurityMiddleware" in /opentainer-web/settings.py.

================