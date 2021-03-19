# backend-modern-intra
## made by abdellah and assim
### how to start the backend on a local server:
create a virtual environment : $ python3 -m venv venv
Activate the venv : $ source venv/bin/activate
clone the project : $ git clone https://github.com/abdellahJR/backend-modern-intra.git
cd to the project : $ cd backend-modern-intra
install the requirments : $ pip install -r requirements.txt
migrate the models : $ python manage.py migrate --run-syncdb
create super user : $ python manage.py createsuperuser
rin the server : $ python manage.py runserver


