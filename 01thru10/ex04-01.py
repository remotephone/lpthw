# We are assigning variables!
# Each one of these values is assigned a number. This is stored in memory as
# the program runs.

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

# You can do math on its own or you can do math on the variables. Python will
# interpret the variables as you use them so there's no need to recall a value
# if you've already set it previously. I don't have to do the math for
# carpool_capacity each time if it's already done once as a variable.

cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# Now we're pritning stuff left and right here. Pow pow pow pow. Each one of
# them is taking the math I've already done and displaying it.

print "There are", cars, "cars available"
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car"
