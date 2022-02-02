#!/usr/bin/python3

#################
#
# Imports
#
#################
import readability
from nltk.tokenize import word_tokenize
import sys

#################
#
# Open the Branded Foods CSV file and parse it
#
#################
branded_foods_file = "./static_archive/branded_food.csv"
orig_stdout = sys.stdout
output_file = "readability_measures.csv"
contents = open(branded_foods_file,"r")
line = contents.readline()
round_to = 2


f = open(output_file, 'w')
sys.stdout = f

print("Characters,Syllables,Words,Long_Words,Complex_Words,Kincaid,ARI,Coleman,Flesh,Gunning,LIX,SMOG,RIX,Dale")

counter = 1
# Iterate through each line of ingredients
# and create a csv file of different measures, including
# The number of words, long words, and complex words
# All readability measures included
while(line):
	#
	# Grab the ingredients from the file
	#
	tokens = line.split('","')
	ingredients = tokens[3].lower()
	ingredients = ingredients.rstrip()

	#
	# Store the ingredients to print later
	#
	ingr = ingredients
	if(ingredients != "---" and ingredients != ""):
		tokenized = word_tokenize(ingredients)
		ingredients = tokenized
		read = readability.getmeasures(ingredients,lang='en')
		print(	str(read['sentence info']['characters']) + "," + \
			str(read['sentence info']['syllables']) + "," + \
			str(read['sentence info']['words']) + "," + \
			str(read['sentence info']['long_words']) + "," + \
			str(read['sentence info']['complex_words']) + "," + \
			str(round(read['readability grades']['Kincaid'],round_to)) + "," + \
			str(round(read['readability grades']['ARI'],round_to)) + "," + \
			str(round(read['readability grades']['Coleman-Liau'],round_to)) + "," + \
			str(round(read['readability grades']['FleschReadingEase'],round_to)) + "," + \
			str(round(read['readability grades']['GunningFogIndex'],round_to)) + "," + \
			str(round(read['readability grades']['LIX'],round_to)) + "," + \
			str(round(read['readability grades']['SMOGIndex'],round_to)) + "," + \
			str(round(read['readability grades']['RIX'],round_to)) + "," + \
			str(round(read['readability grades']['DaleChallIndex'],round_to))) 
	line = contents.readline()
	counter += 1
		
sys.stdout = orig_stdout
f.close()
