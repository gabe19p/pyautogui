# dictionary
coordsDictionary = {}
clickCount = 3
for click in range(0, clickCount):
    coordsDictionary["string{0}".format(click)] = "Hello"
    print(coordsDictionary)