
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class accountReport:
    def __init__(self):
        self.startingBalance = 0.00
        self.purchaseList = []
        self.totalExpense = 0
        self.averageExpense = 0

    def addPurchase (self, id, description, value):
        return True

class purchase:
    def __init__(self, id, description, cost):
        self.id = id
        self.description = description
        self.cost = cost

def getBalanceReport(spendString):
    #get rid of dodgy characters
    cleanString = getCleanString(spendString)
 
    thisAccountReport = accountReport()
    #find the starting balance
    thisAccountReport.startingBalance = getStartingBalance(cleanString)

    return cleanString

#returns the starting balance as a float
def getStartingBalance(cleanString):
    #account balance should be the first line of the string
    splitString = cleanString.splitlines()
    return float(splitString[0])

#Checks the character against valid criteria
def isCharacterAllowed (character):
    characterStatus = False
    if any ([character.islower(), character.isupper(), character.isnumeric(),
            character == '.', character == ' ', character == '\n']): 
        characterStatus = True
    return characterStatus
    
def getCleanString(string):
#strip out any symbols that are not letters numbers or full stops
# and empty lines
    cleanString = ""
    for character in string:
        if isCharacterAllowed(character):
            cleanString = cleanString + character
    #now get rid of empty lines
    cleanString.replace("\n\n", '\n')
    return cleanString

def main():
    return 0


if __name__ == '__main__':
    main()