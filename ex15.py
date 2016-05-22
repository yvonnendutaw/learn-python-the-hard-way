from sys import argv

script, dictionaries.py = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C ."

print "If you do want that, hit RETURN."
raw_input("?")

print "Opening the file..."
target = open(dictionaries.py, 'w')

print "Truncating the file.
target.truncate() Goodbye!"

print "Now I'm going to ask you for three lines."
#what will be written in the file
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
#writing the file
print "I'm going to write these to the file."
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print "And finally, we close it."
target.close()
