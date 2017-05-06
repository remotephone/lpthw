# Tend to have capital names for classes
class Crop:
    """A generic food crop"""

    #constructure
    # Special method - run automatically when you instantiate the class
    def __init__(self,growth_rate, light_need, water_need):
        #set the attributes with an initial value
        # self allows an instnace to refer to itself
        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"

        #These attributes are public. Anything can access them. But we want
        # each object to see ony its internal state. In order to make them
        # private you need to add an underscore before its name.

# When we want ot use a class we have to instantiate it.

def main():
    #instantiate it
    new_crop = Crop(1,4,3)
    # This is filling in the meaning of the vallies in the __init__ above!!!!
    # Crop class is called with growth_rate of 1, light_need of 4, and
    # water_need of 3.
    print new_crop._status
    print new_crop._light_need
    print new_crop._water_need
    # WE can do this again and instantiate another crop!
    new_crop2 = Crop(2,3,4)
    print new_crop2._status
    print new_crop2._light_need
    print new_crop2._water_need

if __name__ == "__main__":
    main()
