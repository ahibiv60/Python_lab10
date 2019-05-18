class Helicopter:
    
    numberOfHelicopters = 3
    #
    def __init__(self, name = "unknown", maxLiftingWeight = 0, maxHeight = 0, maxSpeed = 0, crew = 0, diameterOfRotor = 0):
        self.name = name
        self.maxLiftingWeight = maxLiftingWeight
        self.maxHeight = maxHeight
        self.maxSpeed = maxSpeed
        self.crew = crew
        self.diameterOfRotor = diameterOfRotor
    #    
    def __str__(self):
        return "Name: {0}\nMax Lifting Weight: {1}\nMax Height: {2}\nMax Speed: {3}\nCrew: {4}\nDiameter Of Rotor: {5}.\n".format(self.name, self.maxLiftingWeight, 
            self.maxHeight, self.maxSpeed, self.crew, self.diameterOfRotor)
        
    @staticmethod
    def getNumberOfHelicopters():
        return Helicopter.numberOfHelicopters
    
    def __del__(self):
        print("Helicopters deleted.")
    
def main():  
    unknown = Helicopter()      
    helicopter1 = Helicopter('Bell 47', 4125, 6453, 2432, 2, 7.5)
    helicopter2 = Helicopter('Bell 206', 3567, 7543, 3256, 3, 7.4)
    helicopter3 = Helicopter('Bell 400', 6314, 5452, 4256, 2, 7.6)

    print(unknown)
    print(helicopter1)
    print(helicopter2)
    print(helicopter3)

    print("Number of helicopters: ", Helicopter.getNumberOfHelicopters(), "\n")

if __name__ == "__main__": main()