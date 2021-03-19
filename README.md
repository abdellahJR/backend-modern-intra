# backend-modern-intra

## made by abdellah and assim

### how to start the backend on a local server:

```
$ python3 -m venv venv # create a virtual environment
$ source venv/bin/activate # Activate the venv
$ git clone https://github.com/abdellahJR/backend-modern-intra.git # clone the project
$ cd backend-modern-intra # cd to the project
$ pip install -r requirements.txt # install the requirments
$ python manage.py migrate --run-syncdb # migrate the models
$ python manage.py createsuperuser # create super user
$ python manage.py runserver # run the server
```


