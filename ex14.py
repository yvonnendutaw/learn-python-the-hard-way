#imports the feature argument
from sys import argv
#the variables are packed in the argv module
script, dictionaries.py = argv
#opens the file
txt = open(dictionaries.py)
#print out the file
print "here's your file %r:" % dictionaries.py
print txt.read()

print "type of filename again"
file_again = raw_input("> ")
txt._again = open(file_again)
print txt_again.read()

