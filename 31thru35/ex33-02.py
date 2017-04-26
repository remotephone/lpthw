print "Gimme a number."

val = int(raw_input())


# def whileloop():
def whileloop():

    i = 0
    numbers = []

    while i < val:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

whileloop()
