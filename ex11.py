print "How old are you?",
age = raw_input()

print "How tall are you?",
height = raw_input()

print "How much do you weigh?"
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)

#raw_input: http://docs.python.org/library/functions.html#raw_input
# see also: input(); - http://www.daniweb.com/software-development/python/threads/12326/how-to-do-input-in-python
#input() will evaluate as python code, so it's unsafe.