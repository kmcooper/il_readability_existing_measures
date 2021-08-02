# Welcome! 

## Measuring Ingredients List Readability with Existing Indices


### Setup
This archive assumes you have first downloaded the necessary files from the [USDA FoodData Central website](https://fdc.nal.usda.gov/download-datasets.html).
In this work we used the October 2020 version of the Branded Foods Database, which can be downloaded from the following link:
https://fdc.nal.usda.gov/fdc-datasets/FoodData_Central_branded_food_csv_2020-10-30.zip

Alternatively, you can run the setup.sh script, which will download and store the files needed to reproduce this project. It assumes you are running bash and have wwget installed. If you are on a Mac, you can use curl -L as an alternative but make sure the filenames match.

./setup.sh

This will create a folder called "static_archive" will all the necessary files downloaded and with readonly privileges.

You should also download and install the *readability* package from PyPI: https://pypi.org/project/readability/


## Readability Scores
