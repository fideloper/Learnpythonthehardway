from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, git CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

# 'w' mode actually truncates the file to begin with.
# Reference: http://docs.python.org/library/functions.html#open

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

output = "%s \n %s \n %s \n" % (line1, line2, line3)
target.write(output)

#target.write(line1+"\n")
#target.write(line2+"\n")
#target.write(line3+"\n")

print "And finally, we close it."

target.close()
