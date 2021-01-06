# Nurserystore
This project is the backend for nursery store created using Django Rest Framework

# Installation steps
Create Virtual environment
```
virtualenv -p python3 jango
```

Install dependencies by installing requirements.txt
```
pip install -r requirements.txt
```

Setup database schema by running
```
python3 manage.py makemigrations
python3 manage.py migrate
```

Create superuser for accessing django admin panel
```
python3 manage.py createsuperuser
```
