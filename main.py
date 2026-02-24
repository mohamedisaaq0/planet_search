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

while running == 1:
    print("\nAsk a question about a planet (or enter exit)")
    search_val = input("Question: ")
    
    # input validation so it doesnt crash on empty strings
    if search_val.strip() == "":
        print("Invalid input. Please type a question.")
        continue
    
    # check if user wants to quit
    if search_val.lower() == "exit":
        running = 0
        print("Done.")
    else:
        match_found = 0 # flag to check if we find a planet match
        
        # I was stuck on how to make the program read full sentences instead of just single words.
        # I used an AI to help me debug this loop and it showed me how to use .lower() and 'in'.
        for p_item in all_planets:
            # chekcing for the planet in their question
            if p_item.name.lower() in search_val.lower():
                match_found = 1
                
                # looking for keywords in their question to figure out what they want to know
                if "mass" in search_val.lower() or "massive" in search_val.lower():
                    print("The mass of " + p_item.name + " is " + p_item.mass)
                    
                elif "moon" in search_val.lower():
                    print(p_item.name + " has these moons: " + p_item.moons)
                    
                elif "distance" in search_val.lower() or "far" in search_val.lower():
                    print(p_item.name + " is " + p_item.distance + " from the sun")
                    
                elif "everything" in search_val.lower() or "about" in search_val.lower():
                    print("Here is everything about " + p_item.name + ":")
                    print("- Mass: " + p_item.mass)
                    print("- Distance: " + p_item.distance)
                    print("- Moons: " + p_item.moons)
                    
                else:
                    # fallback if they just type the planet name or ask if it is in the list
                    print("Yep, " + p_item.name + " is a planet in the list.")
                    
        # if loop finishes and flag is unchanged then theyre asking about a missing planet
        if match_found == 0:
            print("Planet not found, try again.")