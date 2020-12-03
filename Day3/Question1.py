def getdata():
    with open('raw_data', 'r') as data:
        rawdata = data.readlines()
        data = []
        for values in rawdata:
            value = values.split()
            data.append(value)
        print(data)
        return data  # returns list of values as strings


def checkroute(data):
    treecaount = 0
    thisindex = 0
    for values in data:
        for value in values:
            char = (value[thisindex])
            print(char, thisindex, data.index(values))
            if thisindex + 1 >= len(value):
                thisindex = 2
            elif thisindex + 2 >= len(value):
                thisindex = 1
            elif thisindex + 3 >= len(value):
                thisindex = 0
            else:
                thisindex += 3
            if (char == '#'):
                treecaount += 1

    print(treecaount)

checkroute(getdata())