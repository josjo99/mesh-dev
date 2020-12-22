# mesh-dev

1. Install postgresql-13

    `apt install postgresql-13`

2. Install python3-venv
    
   `apt install python3-venv`

3. Install MongoDB
    
    [MongoDB-Debian](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-debian/)
   
    [MongoDB-Ubuntu](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)
   
    [MongoDB-Windows](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/)

4. Virtual environment

    a. Create virtual environment
    
        python3 -m venv meshenv

    b. Activate virtual environment
        
        cd meshenv
        source bin/activate
        
5. Install packages

        pip3 install -r requirements.txt
        
6. Modify settings.py

        
