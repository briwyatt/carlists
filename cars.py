# create an empty set named showroom
showroom = set()

#Add four of your favorite car model names to the set.
showroom.update(['Lexus', 'Prius', 'Passat', 'Range Rover'])

#Print the length of your set.
print(len(showroom))

# Pick one of the items in your show room and add it to the set again.
showroom.add('Prius')

#Print your showroom. Notice how there's still only one instance of that model in there.
print(showroom)

#Using update(), add two more car models to your showroom with another set.
showroom.update(['Corolla', 'Camry'])

print(showroom)

#You've sold one of your cars. Remove it from the set with the discard() method.
showroom.discard('Passat')

print(showroom)
