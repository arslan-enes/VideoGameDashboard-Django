# STEPS
1. ```python -m venv venv```
2. ```venv/bin/activate```
3. ```pip install django```
4. ```django-admin startproject videogamedashboard```
5. ```cd videogamedashboard```
6. ```python manage.py startapp dashboard```
7. create VideoGame model in dashboard/models.py
8. ```python manage.py makemigrations```
9. ```python manage.py migrate```
10. ```python manage.py createsuperuser```
11. update dashboard/admin.py