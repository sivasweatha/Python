# Import Hello class
from hello_class import Hello

# Creating a object
h = Hello()

# Get the User's Name
name = input("Your name: ")

# Some IFs
yogi = name == "Yogi" or name == "Sivayogeith" or name == "Sivayogeith Umamaheswaran"
akkama = name == "Sivi" or name == "Sivasweatha" or name == "Sivasweatha Umamaheswaran"
if (yogi):
    name = "CTO of Ulagellam, Sivayogeith Umamaheswaran"
elif (akkama):
    name = "Akkama"

# Last but not the least printing the greeting
h.sayHelloP(name, True)
