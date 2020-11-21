def main():
    for i in range(1, 11):
        fileName = 'PALIN' + str(i) + '.IN'
        f = open('Inputs/' + fileName, 'r')
        if f.mode == 'r':
            lines = f.readlines()
            minChars = evalString(int(lines[0]), lines[1])

            print(fileName, minChars)


def evalString(stringLength, stringValue):
    changes = 0
    while stringLength > 1:
        # print(stringValue)
        y = stringLength - 1
        while stringLength > 1 and stringValue[0] == stringValue[y]:
            stringValue = stringValue[1:y]
            stringLength -= 2
            y = stringLength - 1

        if stringLength > 1:
            if stringValue[1] == stringValue[y]:
                stringValue = stringValue[1:]
            else:
                stringValue = stringValue[:y]

            changes += 1
            stringLength -= 1

    return changes


if __name__ == '__main__':
    main()
