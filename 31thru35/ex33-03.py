
# Call for input, the user will put stuff in for us to start and increment.
print "Gimme a number."
val = int(raw_input())

print "And you wanna increment by whaaaat?"
increm = int(raw_input())

# def whileloop function which is the meat of what we're doing
def whileloop():

# define i to start at 0 and set numbers as an empty range that will take info.
    i = 0
    numbers = []

# While i is less than val, print and add i. 
    while i < val:
        print "At the top i is %d" % i
        numbers.append(i)

# Each time i is added, its incrememted by the value. 

        i = i + increm
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

# Print the number that's incrementing.
    for num in numbers:
        print num

#Run the function whileloop()
whileloop()
