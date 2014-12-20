Opentainer  
==============

python manage.py makemigrations  

python manage.py migrate  

sudo python manage.py runserver  
(run this command as root to avoid some of the error which might be encountered later)  

===============  

The default credentials of superuser:  
username: admin  
password: admin  

===============  

===============  

If you are using Django 1.7 then the server will through error "No module named security" unless you comment the line "django.middleware.security.SecurityMiddleware" in /opentainer-web/settings.py.  

===============  
