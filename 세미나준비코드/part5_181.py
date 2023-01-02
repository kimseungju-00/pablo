def countBirths():
    ret = []
    for y in range(1880, 2016):
        count = 0
        filename = 'yob%d.txt' %y
        with open(filename, 'r') as f:
            data = f.readlines()
            for d in data:
                if d[-1] == '\n':
                    d = d[:-1]

                birth = d.split(',')[2]
                count += int(birth)
        ret.append((y, count))
    return ret

result = countBirths()
with open('birth_by_year.csv', 'w') as f:
    for year, birth in enumerate(result):
        data = '%s, %s\n'%(year, birth)
        print(data)
        f.write(data)