from sys import argv

script, dictionaries.py = argv

txt = open(dictionaries.py)

print "here's your file %r:" % dictionaries.py
print txt.read()

print "type of filename again"
file_again = raw_input("> ")
txt._again = open(file_again)
print txt_again.read()

