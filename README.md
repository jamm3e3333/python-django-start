1 Initializing repo

## installing pipenv and pi
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
`deactivate

## removing virtual env
`rm -rf <path to the virtyal env>`

2 using different approaches to create virtual environment

## venv
- creating a virtual environment within a folder
`python3 -m venv .`

- activating virt. env.
`source bin/activate`

## virtualenv
`python3 -m pip install virtualenv`
- running virt. env.
`virtualenv -p python3 .`   
