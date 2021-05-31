# Alembic
Alembic is a database migration tool to be used with SQLAlchemy library.

A "migration" is the set of steps needed whenever the structure of the SQLAlchemy models is changed (eg, adding a new attribute) to replicate the changes in the database (eg, add a new column, a new table, etc)

Steps to recreate this folder (not required if you have already cloned this repo)

#### Step 1
Initialise alembic.
```
alembic init alembic
```
This creates the `alembic` directory and an `alembic.ini` file at the root of the project folder. Modify the connection in the `alembic.ini` file.

#### Step 2
Create migration to initialise the table.
```
alembic revision -m "init"
```
This creates a script in `alembic/versions` directory.

First create an `upgrade` function in the script.
This creates a table with the model's name and defines the columns which match the model.

Next, create a `downgrade` function.
This will be used to revert migration if needed.

#### Step 3
Run the migration.
```
alembic upgrade head
```
## Author
Joy Sng

## Sources
https://alembic.sqlalchemy.org/en/latest/tutorial.html
