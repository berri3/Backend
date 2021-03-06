# Backend
Backend for our ECSE 428 application

# Development Setup
We're using python 3+ with django v2. 
Ensure that the python and pip versions you use are configured 
for python 3+.

### Configure VirtualEnv
VirtualEnv ensures that you will have an isolated environment for this project

To create a new virtualenv
```
pip install virtualenv
virtualenv env
```

To activate the virtual env from a bash command line use
```
source env/bin/activate
```

### Install the Project Dependencies

Ensure you're in the virtual environment for the project, then run
```
pip install -r requirements.txt
```

### Configuring MySQL and Redis with Docker Compose

You'll need to run MySQL and Redis on localhost in order for the app to work. With docker compose this is as simple as running
```
docker-compose up
```

If you're running using a docker-machine VM then set the environment variables so that when you run the app locally
it'll know where to reach the machine.
```
MYSQL_HOST=*Insert Docker VM IP here*
REDIS_HOST=*Insert Docker VM IP here*
```

### Installing New Packages

If you require a new package during development, ensure that you add a line for it in requirements.txt. 
If you're working in a virtualenv, then you can also run the to update the requirements.txt file.

##### Don't do this if you're not using a virtualenv or you'll get a slap
```
pip freeze > requirements.txt
```

# Testing

Go into the timemachine folder

```
cd timemachine/
python manage.py test
```

# Style Checking & Linting

```
./test.sh
```
# Running Project
Sorry but your gonna need docker, check the readme on Frontend

```
docker-compose up
```

Nevermind docker has left us hanging all gods are dead. 

```
source env/bin/activate
pip install -r requirements.txt
python manage.py runserver 0.0.0.0:8000
```

# API
These are the rest api that are available

## Problems
This is the endpoint for all problems:

```
http://localhost:8000/restapi/problem/
```

Note: The last slash is important!

This api has GET and POST.


For individual problems:

```
http://localhost:8000/restapi/problem/#/
```

Note: Again the slash is important!

This api has GET, PUT, and DELETE.

## Rating
This is the endpoint for all ratings:

```
http://localhost:8000/restapi/rating/
```

This api has GET and POST.


For individual problems:

```
http://localhost:8000/restapi/rating/#/
```

This api has GET, PUT, and DELETE.

## Solution
This is the endpoint for all solutions:

```
http://localhost:8000/restapi/solution/
```

This api has GET and POST.


For individual problems:

```
http://localhost:8000/restapi/solution/#/
```

This api has GET, PUT, and DELETE.
