# backend-modern-intra

## made by abdellah and assim

### how to start the backend on a local server:

#### create a virtual environment
{% filename %}python3 -m venv venv{% endfilename %}
#### Activate the venv
{% filename %}source venv/bin/activate{% endfilename %}
#### clone the project
{% filename %}git clone https://github.com/abdellahJR/backend-modern-intra.git{% endfilename %}
#### cd to the project
{% filename %}cd backend-modern-intra{% endfilename %}
#### install the requirments
{% filename %}pip install -r requirements.txt{% endfilename %}
#### migrate the models
{% filename %}python manage.py migrate --run-syncdb{% endfilename %}
#### create super user
{% filename %}python manage.py createsuperuser{% endfilename %}
#### run the server
{% filename %}python manage.py runserver{% endfilename %}




