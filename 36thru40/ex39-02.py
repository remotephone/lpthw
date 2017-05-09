
# Making a simple foods dictionary

foods = {
        'Mexican': 'tacos',
        'Italian': 'pizza',
        'American': 'hamburgers',
        'Japanese': 'sushi'
}

print "Some italian food is ", foods['Italian']

print "Let's add some more foods."

# We can replace the food items by reassigning Italian
foods['Italian'] = "pasta"

#print all foods to see pizza is now pasta
print foods

#We can add new categories of food too. 
foods['German'] = "brautwurst"
print "Some German food is ", foods['German']

#print all foods with German included
print foods
