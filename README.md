# 1 Initializing repo

## installing pipenv and pip
`python3 -m pip install pipenv pip --upgrade`

## initializae repo
- installing python3 into the repo 
- creating Pipfile (smth like package.json file)
`pipenv install --python python3`

## running pipenv file
- running the  virtual environment
`pipenv shell`

## pip freeze 
- saying what's installed in the environment

## installing other packages inside the repo
`pipenv install <name of the package>`
- when installing with pip only
`pip install <name of the package>`
- the `pip freeze` command needs to be run to include the package into the Pipfile

## uninstalling the package
`pipenv uninstall <name of the package>`

## deps in txt file
`pip freeze > requirements.txt`
- then installing the deps from the txt file
`pipenv install -r requirements.txt`

## deactivating the virtual environment
`deactivate`

## removing virtual env
`rm -rf <path to the virtyal env>`

# 2 using different approaches to create virtual environment

## venv
- creating a virtual environment within a folder
`python3 -m venv .`

- activating virt. env.
`source bin/activate`

## virtualenv
`python3 -m pip install virtualenv`
- running virt. env.
`virtualenv -p python3 .`   

# 3 starting the django project
- to create a django project

`django-admin startproject <name of the project > <name of the directory>`

- to run the django app

`python manage.py runserver`

after reopening the repo to start running again:
1. `pipenv shell` to start the virt. env.

2. `pipenv install` something like `npm install`

3. `pipenv run python manage.py runserver <port number (8000 by default)>`

## to fix the errors and sync with the db: 
`pipenv run python manage.py migrate`

## creating superuser
`pipenv run python manage.py createsuperuser`

## creating apps
`pipenv run python manage.py startapp <name of the app>`

## after changing models.py
`pipenv run python manage.py makemigrations`
`pipenv run python manage.py migrate`

## running the python shell

`pipenv run python manage.py shell`

- importing the models in the app
`from <folder name>.models import <class name of model>`

- querying the data 
`<class name>.objects.all()`

- creating new data
`<class name>.objects.create(<fields to create>)`

# 3 Django backend
- creating another app
`django-admin startproject <name of the dir> <dir>`

- running the server
`pipenv run python manage.py runserver`

