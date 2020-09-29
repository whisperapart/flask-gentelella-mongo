# Flask Gentelella
Thanks to Flask Gentelella:

[Gentelella](https://github.com/puikinsh/gentelella) is a free to use Bootstrap admin template.

![Gentelella Bootstrap Admin Template](https://cdn.colorlib.com/wp/wp-content/uploads/sites/2/gentelella-admin-template-preview.jpg "Gentelella Theme Browser Preview")

This project integrates Gentelella with Flask using: 
- [Blueprints](https://flask.palletsprojects.com/en/1.0.x/blueprints/) for scalability.
- [flask_login](https://flask-login.readthedocs.io/en/latest/) for the login system (passwords hashed with bcrypt).
- pyMongo for mongodb connection


This project shows:
- how back-end and front-end can interact responsively with AJAX requests.
- how to implement a User model with mongodb 

## Run Flask Gentelella with MongoDB

### (Optional) Set up a [virtual environment](https://docs.python.org/3/library/venv.html) 

### 1. Get the code
    git clone https://github.com/whisperapart/flask-gentelella-mongo.git
    cd flask-gentelella-mongo

### 2. Install requirements 
    pip install -r requirements.txt

### 3. Set the FLASK_APP environment variable
    (Windows) set FLASK_APP=admin.py
    (Unix) export FLASK_APP=admin.py
    (Powershell) $env:FLASK_APP = ".\admin.py"

### 4. Run the application
    flask run --host=0.0.0.0

### 4. Go to http://localhost:5000/, create an account and log in

## Run Flask Gentelella with a MongoDB database (CentOS)

### 1. Install a PostgreSQL database
	yum install mongo-org-server

### 2. Export the following environment variables
    export GENTELELLA_CONFIG_MODE=Production
    export GENTELELLA_DATABASE_PASSWORD=your-password

### 3. Follow the steps described in the previous section

### 2. Start all services
    sudo docker-compose pull && sudo docker-compose build && sudo docker-compose up -d

### 3. Go to http://server_address, create an account and log in
