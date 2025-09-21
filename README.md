# Overview

This is a program that connects to a database table with saved birthdays and special events, and sends an email reminder with a reminder. 

# Instruction 

This script should be scheduled to run at the beginning of each day, e.g. by chronjob on linux or with a server (e.g. PythonAnywhere scheduled daily task).

The complete environment requirements are given in the file `conda_environment.yml`, for the Conda environment called `Birthday_reminder`. Additionally, the required Python libraries are given in `requirements.txt`. 

To install the Conda environment:
- First, make sure you have Conda installed. If not, check online how to do it;
- `cd` into this directory
- Run the command `conda env create -f conda_environment.yml`

