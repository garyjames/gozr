# IMX Dev Exercise
## Overview
In this exercise you will create a python program that will create analytics from data provided in the sqlite database in this repo.
### Deliverables
* A completed program which performs the described functionality
* A Dockerfile for the program
* A Bash script that will build the docker container and run the built container
## Components
### number_cruncher
Number cruncher is the python module containing the python code for the app. Complete the code as commented in app.py
### data.db
The sqlite database for the app. The python app should use the data in this database for it's calculations
### Dockerfile
The definition for the programs docker container
### crunch_numbers.sh
The bash script that builds the application and runs it
## Want more?
**NOTE**: Please know this is only an extra challenge and choosing not to do it will not 
be of any detriment
### Bonus Challenge
Turn the functions in number_cruncher into REST API endpoints and query the data
from crunch_numbers.sh
