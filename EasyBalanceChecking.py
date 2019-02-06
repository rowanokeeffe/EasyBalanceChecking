
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def getBalanceReport(spendString):
    cleanString = getCleanString(spendString)
    return cleanString
    
def getCleanString(string):
#strip out any symbols that are not letters numbers or full stops.
    cleanString = ""
    for letter in string:
        if letter.islower() or letter.isupper() or letter == '.' or letter.isnumeric() or letter == ' ':
            cleanString = cleanString + letter
    return cleanString

def main():
    return 0


if __name__ == '__main__':
    main()