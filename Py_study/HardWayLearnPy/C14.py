from sys import argv

script, user_name, age = argv
prompt = '... '

print "Hi %s, you are %s old? I'm the %s script." % (user_name,age, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)
print "Where do you live %s?" % user_name
lives = raw_input()
print "What kind of computer do you use?"
computer = raw_input()

print """
Alrigth, so you said %r like me.
You live in %s.Not sure where it is.
And you have a %r computer.Nice. 
""" % (likes,lives,computer)

