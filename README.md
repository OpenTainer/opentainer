Opentainer  
==============
To run the opentainer app locally, follow the steps given below:

git clone https://github.com/OpenTainer/opentainer.git
cd opentainer
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

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
