def readfromfile():
    BirthYear = 'byr'
    IssueYear = 'iyr'
    ExpirationYear = 'eyr'
    Height = 'hgt'
    HairColor = 'hcl'
    EyeColor = 'ecl'
    PassportID = 'pid'
    CountryID = 'cid'
    with open('raw_data', 'r+', newline=None) as data:
        rawdata = data.readline()
        procdata = []
        for lines in data:
            # print(lines)
            lines = lines.split(' ')
            lines = lines[0].rstrip()
            procdata.append(lines)
        passports = {}
        for values in procdata:
            BirthYear
            IssueYear
            ExpirationYear
            Height
            HairColor
            EyeColor
            PassportID
            CountryID

            key = values[0:3]
            # print(key)

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
                BirthYear = ''
                IssueYear = ''
                ExpirationYear = ''
                Height = ''
                HairColor = ''
                EyeColor = ''
                PassportID = ''
                CountryID = ''
            else:
                print('Value not recognised: ', values)
        return passports



mydict = readfromfile()
for k in mydict:
    print(k, mydict[k])