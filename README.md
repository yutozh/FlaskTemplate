## Introduction
This is a template flask project. It contains the basic function of database access, verification, and route/view/model example.

## Usage
### Install
This project use `poetry` to manage the dependent packages. Please follow the [Poetry document](https://python-poetry.org/docs/#installation) to install it first.

When you installed `poetry`, run the following command to download dependencies and build the environment.
```bash
poetry install
```

### Run
To run the flask build-in server, execute the command:
```bash
python manager.py runserver
```

For database management and migration, execute these commands:
```bash
python manager.py db init # init data
python manager.py db migrate # change the structure of the database
python manager.py db upgrade  # update database to server
```

## ToDo
- [ ] Frontend Page Example
- [ ] Docker Support
- [ ] Test Support
- [ ] ...