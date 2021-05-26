#!/usr/bin/python3

#################
#
# Imports
#
#################
import readability
from nltk.tokenize import word_tokenize

#################
#
# Open the file branded_food and parse it
#
#################
#all_info = "test.csv"
all_info = "./static_archive/branded_food.csv"
contents = open(all_info,"r")
line = contents.readline()
print("Length,Kincaid,ARI,Coleman,Flesh,Gunning,LIX,SMOG,RIX,Dale")
counter = 1
while(line):
        #print(counter)
        tokens = line.split('","')
        ingredients = tokens[3].lower()
        ingredients = ingredients.rstrip()
        ingr = ingredients
        #print("-->"+ingredients+"<---")
        if(ingredients != "---" and ingredients != ""):
                tokenized = word_tokenize(ingredients)
                ingredients = tokenized
                read = readability.getmeasures(ingredients,lang='en')
                print(  str(len(ingredients))+ "," + \
                        str(ingr) + ',' + \
                        str(read['readability grades']['Kincaid']) + "," + \
                        str(read['readability grades']['ARI']) + "," + \
                        str(read['readability grades']['Coleman-Liau']) + "," + \
                        str(read['readability grades']['FleschReadingEase']) + "," + \
                        str(read['readability grades']['GunningFogIndex']) + "," + \
                        str(read['readability grades']['LIX']) + "," + \
                        str(read['readability grades']['SMOGIndex']) + "," + \
                        str(read['readability grades']['RIX']) + "," + \
                        str(read['readability grades']['DaleChallIndex']))
        line = contents.readline()
        counter += 1
