def readfromfile():
    BirthYear, IssueYear, ExpirationYear, Height, \
    HairColor, EyeColor, CountryID, PassportID = '', '', '', '', '', '', '', ''

    with open('raw_data', 'r', newline='') as data:
        procdata = []
        for lines in data:
            data = lines.rstrip()
            data = data.split(' ')
            for value in data:
                procdata.append(value)

        passports = {}
        for values in procdata:

            key = values[0:3]
            # print(values, key)

            if key == 'byr':
                BirthYear = values[4:]
            elif key == 'iyr':
                IssueYear = values[4:]
            elif key == 'eyr':
                ExpirationYear = values[4:]
            elif key == 'hgt':
                Height = values[4:]
            elif key == 'hcl':
                HairColor = values[4:]
            elif key == 'ecl':
                EyeColor = values[4:]
            elif key == 'pid':
                PassportID = values[4:]
            elif key == 'cid':
                CountryID = values[4:]
            elif values == '':
                passports[PassportID] = {'byr': BirthYear, 'iyr': IssueYear, 'eyr': ExpirationYear, 'hgt': Height,
                                         'hcl': HairColor, 'ecl': EyeColor, 'cid': CountryID}
                # print(PassportID, ':', passports[PassportID])

                BirthYear, IssueYear, ExpirationYear, Height, \
                HairColor, EyeColor, CountryID, PassportID = '', '', '', '', '', '', '', ''

            else:
                print('Value not recognised: ', values)
        return passports



mydict = readfromfile()
for k in mydict:
    print(k, mydict[k])