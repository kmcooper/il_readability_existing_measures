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

At this point you will want to navigate one folder up from the static_archive, so that the branded_foods.csv file is available at the following path:
`./static_archive/branded_foods.csv`
This is hard-coded into the Python script (yes, this code is very hack-y) so you can also change it to point to your version of the branded foods csv file as well. From there, you should run the Python script called `get_readability_measures.py` which takes branded_foods.csv as an input file and generates a file called `readability_measures.csv`. The script uses the readability library from above to identify a number of readabilitiy measures. `readability_measures.csv` analyzes one product ingredient list and the ouput contains the following items per ingredient list on separate rows (in order, also given as the file header):
- Characters	
- Syllables	
- Words	
- Long_Words	
- Complex_Words	
- Kincaid	
- ARI	
- Coleman	
- Flesh	
- Gunning	
- LIX	
- SMOG	
- RIX	
- Dale
Running this script will take some time and will generate a file that is approximately **X** in size.

## Validation
If you are using an updated version of the Branded Foods database or the readability library, here's a simple and quick check you can use to ensure the measures have not changed significantly using the GitHub Terms of Serive Summary, below:
"*Thank you for using GitHub! We're happy you're here. Please read this Terms of Service agreement carefully before accessing or using GitHub. Because it is such an important contract between us and our users, we have tried to make it as clear as possible. For your convenience, we have presented these terms in a short non-binding summary followed by the full legal terms.*"

#### Readability Metrics Using PyPI Readability Index:

#### Readability Metrics Using Online Tool:


### License
This repo uses the [GNU General Public License v 3.0](https://github.com/kmcooper/il_readability_existing_measures/blob/main/LICENSE)

### Further Reading/Future Work
Some interesting literature that might spark ideas on how one might expand this work are listed below:
- Zhou, S., Jeong, H., & Green, P. A. (2017). How consistent are the best-known readability equations in estimating the readability of design standards?. IEEE Transactions on Professional Communication, 60(1), 97-111.
- Redish, J. C. (1981). Understanding the limitations of readability formulas. IEEE transactions on professional communication, (1), 46-48.
