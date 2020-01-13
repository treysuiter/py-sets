#Create set variable

showroom = set()

#Add models to set
showroom.add("Rogue")
showroom.add("Leaf")
showroom.add("Frontier")
showroom.add("Altima")
#Add duplicate model
showroom.add("Altima")

#Add two more models
showroom.update(["Titan", "Sentra"])

#Remove model
showroom.discard("Altima")

print("showroom length", len(showroom))
print(showroom)

#Create another set of models
junkyard = set()
junkyard.update(["Rogue", "Leaf", "Titan", "Murano", "Xtera"])

print(junkyard)
#Print models in both junkyard and showroom
print(showroom.intersection(junkyard))
#Join all models to showroom
showroom = showroom.union(junkyard)
print(showroom)
#Discard Leaf
showroom.discard("Leaf")
print(showroom)

