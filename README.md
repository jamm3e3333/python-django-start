1. Initializing repo

# installing pipenv and pi
`python3 -m pip install pipenv pip --upgrade`

# initializae repo
- installing python3 into the repo 
- creating Pipfile (smth like package.json file)
`pipenv install --python python3`

# running pipenv file
- running the  virtual environment
`pipenv shell`

# installing other packages inside the repo
`pipenv install <name of the package>`
- when installing with pip only
`pip install <name of the package>`
- the `pip freeze` command needs to be run to include the package into the Pipfile

# uninstalling the package
`pipenv uninstall <name of the package>`

# deps in txt file
`pip freeze > requirements.txt`
- then installing the deps from the txt file
`pipenv install -r requirements.txt`

# deactivating the virtual environment
`deactivate` 
