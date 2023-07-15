"""
Even if you haven’t studied physics (recently or ever!), you might have heard that 
, wherein  represents energy (measured in Joules),  represents mass (measured in kilograms), 
and  represents the speed of light (measured approximately as 300000000 meters per second),
per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.
"""
# computes E=mc^2. Takes user input for mass, m


m = int(input("Enter mass in KG: "))
print("Energy is", m*pow(300000000, 2))
