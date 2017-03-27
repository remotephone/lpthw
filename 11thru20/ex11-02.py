# So i thought I'd be cute and add things together, but it literally adds your
# raw_input, just like i told it to. (how rude). Instead, you need to cast each
# input value as a integer if you know it's going to be an integer and that
# will let you add them up.


print "How old are you?"

age = int(raw_input())

print "How many years would you like to look ahead?"

years = int(raw_input())


total = age + years

print "In that many years, you will be %s years old" % total 
