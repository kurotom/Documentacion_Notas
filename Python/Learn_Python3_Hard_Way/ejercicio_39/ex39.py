stuff = {'name': 'Zed', 'age': 39, 'height': 6 * 12 + 2}
print(stuff['name'])
print(stuff['age'])
print(stuff['height'])

stuff['city'] = "SF"

print(stuff['city'])

stuff[1] = "Wow"
stuff[2] = "Neato"
print(stuff[1])
print(stuff[2])

del stuff['city']
del stuff[1]
del stuff[2]

print(stuff)
