

def getdata():
    with open('raw_data', 'r') as data:
        data = data.readlines()
        return data  # returns list of values as strings


def isvalid(min, max, letter, password):
    if min <= password.count(letter) <= max:
        return True



def processdata(datalist):
    isvalidcount = 0
    for values in datalist:
        newvalues = values.split()
        # print(newvalues)

        numbers = newvalues[0]
        numbers = numbers.split('-')
        min = int(numbers[0])
        max = int(numbers[1])
        # print(min, max)

        char = newvalues[1]
        char = char.split(':')
        letter = char[0]
        # print(letter)

        password = newvalues[2]

        
        if isvalid(min, max, letter, password):
            isvalidcount +=1
    print(isvalidcount)

processdata(getdata())