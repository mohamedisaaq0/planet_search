print("Planet Search Tool Started")

# creating a class to handle planet objects
class Planet:
    def __init__(self, name, mass, distance, moons):
        self.name = name
        self.mass = mass
        self.distance = distance
        self.moons = moons

# opening the text file to read the saved data, reference: docs.python.org/3/tutorial/inputoutput.html
f = open("planet_data.txt", "r")
saved_lines = f.readlines()
f.close()

all_planets = [] # list to store all my objects

# loop through the text file lines
for line_data in saved_lines:
    if "Name:" in line_data:
        # text file uses pipes instead of commas so split by pipe, reference: https://stackoverflow.com/questions/1169006/how-to-split-a-string-by-a-specific-delimiter
        pieces = line_data.split("|")
        
        # check that we have all the data parts before trying to read them
        if len(pieces) == 4:
            # strip out the text labels and extra spaces
            n = pieces[0].replace("Name:", "").strip()
            m = pieces[1].replace("Mass:", "").strip()
            d = pieces[2].replace("Dist:", "").strip()
            moons = pieces[3].replace("Moons:", "").strip()
            
            # create object and append to list
            p_data = Planet(n, m, d, moons)
            all_planets.append(p_data)