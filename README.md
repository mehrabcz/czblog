# czblog

**czblog** is a open source project and **free** for everyone : )

## to use

this project programmed by **python 2.7.14** and **django 1.11.13**
###### create your database
* I wanted to make the project smaller so i did not put the database in the GIT *
* use below commands for migrate your database *
```
python manage.py makemigrations
python manage.py migrate
```
* now you have your datdabase *
###### create super user
* use below command for create super user *

```
python manage.py createsuperuser
```

** now you can see project on your browser **
##### just onmore step

* use blow command for run tour localhost server * 

```
python manage.py runserver
```
now you can go to http://127.0.0.1:8000/ (http://127.0.0.1:8000/)

<note :8000 is the default port for django if you wnat to changed it just write your port number when you runing server **>
```
python manage.py runserver [your port number]
```
