def getdata():
    with open('raw_data', 'r') as data:
        rawdata = data.readlines()
        data = []
        for values in rawdata:
            value = values.split()
            value = value[0]
            data.append(value)
        # print(data)
        return data  # returns list of values as strings


# returns a value at a specific index

def getelement(data, index1, index2):
    line = data[index1]
    element = line[index2]
    # print(index1, index2, line, element)
    return element


def testelement(element, char):
    if element == char:
        return True


def parselist(index1, index2, char):
    treecount = 0
    incrementdown = index1
    incrementright = index2
    indexdown = 0
    indexright = 0
    data = getdata()
    for values in range(int(len(data)/incrementdown)):
        element = getelement(data, indexdown, indexright)
        if testelement(element, char):
            treecount += 1
        indexright += incrementright
        if indexright >= len(data[indexdown]):
            indexright = indexright - len(data[indexdown])
        indexdown += incrementdown  # increment index by index value - move to next line in data
    return treecount


route1 = parselist(1, 1, '#')
route2 = parselist(1, 3, '#')
route3 = parselist(1, 5, '#')
route4 = parselist(1, 7, '#')
route5 = parselist(2, 1, '#')
print(route1, route2, route3, route4, route5, '\n', route1*route2*route3*route4*route5)
