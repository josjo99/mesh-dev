# mesh-dev
#try

1. Update package lists

        sudo apt update

2. Install postgresql-13

        sudo apt install postgresql-13

3. Install python3-virtualenv
    
        sudo apt install python3-virtualenv

4. Install MongoDB
    
    [MongoDB-Debian](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-debian/)
   
    [MongoDB-Ubuntu](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)
   
    [MongoDB-Windows](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/)

5. Virtual environment

    a. Create virtual environment
    
        python3 -m venv meshenv

    b. Activate virtual environment
        
        cd meshenv
        source bin/activate
        
6. Install packages

        pip3 install -r requirements.txt
        
7. a. Create Project
        
        django-admin startproject mesh

   b. Create Apps
        
        django-admin startapp authent
        django-admin startapp main

   c. Switch to 'mesh' directory and create superuser:
   
   Follow prompts to create Superuser <username> with password as 
   <password>
        
        cd mesh && python3 manage.py createsuperuser

8. OR clone from github: https://githhub.com/josjo99/mesh-dev.git
10. Modify settings.py

   a. Modify 'default' database as: 
         
         'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'meshdb',
            'USER': 'meshuser',
            'PASSWORD': 'meshpass',
            'HOST': '127.0.0.1',
            'PORT': '5433',
         }

   b. Add to INSTALLED_APPS:
      
         INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'rest_framework',
            'authent',
            'main',
         ]

Possible Additional Settings for PostgreSQL:
        
        nano /etc/postgresql/13/main/pg_hba.conf

    Change the following lines from peer to md5

        # "local" is for Unix domain socket connections only
        local   all             all                                     md5
        # IPv4 local connections:
        host    all             all             0.0.0.0/0               md5
        # IPv6 local connections:
        host    all             all             ::1/128                 md5
    
   Switch to postgres user
        $ sudo su - postgres
        
   Open postgresql shell
        $ psql

   Create user 'meshuser' with password 'meshpass'
        
        $ postgres=# createuser --interactive meshuser;

   Create database 'meshdb'
        
        $ postgres=# create database meshdb;

Optional GUI:

        Install pgadmin4 in windows.
