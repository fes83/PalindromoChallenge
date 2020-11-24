def main():
    for i in range(1, 11):
        fileName = 'PALIN' + str(i) + '.IN'
        with open('Inputs/' + fileName, 'r') as f:
            lines = f.readlines()
            minChars = evalString(int(lines[0]), lines[1])

            print(fileName, minChars)


def evalString(stringLength, stringValue):
    changes = 0
    x = 0
    y = stringLength - 1
    while x < y:
        while x < y and stringValue[x] == stringValue[y]:
            x += 1
            y -= 1

        if x < y:
            if stringValue[x + 1] == stringValue[y]:
                x += 1
            else:
                y -= 1

            changes += 1

    return changes


if __name__ == '__main__':
    main()
