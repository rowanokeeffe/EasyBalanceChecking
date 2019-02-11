
#!/usr/bin/env python
# -*- coding: utf-8 -*-

class accountInfo:
    def __init__(self):
        self.startingBalance = 0.00
        self.purchaseList = []
        self.totalExpense = 0
        self.averageExpense = 0

    def addPurchase (self, id, description, value):
        return True

#takes in a clean string and an account report and outputs a
# fully populated report
def buildAccountInfo(thisAccountInfo, string):
    thisAccountInfo.startingBalance = getStartingBalance(string)
    thisAccountInfo.purchaseList = getPurchaseList(string)
    return thisAccountInfo

#returns the starting balance as a float
def getStartingBalance(string):
    #account balance should be the first line of the string
    splitString = string.splitlines()
    return float(splitString[0])

#get all purchases from the string and add into the structure
def getPurchaseList(string):
    purchaseList = []
    #split into lines and get rid of starting balance     
    splitString = string.splitlines()
    splitString = splitString[1:]
    for line in splitString:
        splitLine = line.split()
        id = int(splitLine[0])
        desc = splitLine[1]
        value = float(splitLine[2])
        thisPurchase = purchase(id, desc, value)
        purchaseList.append(thisPurchase)
    return purchaseList

#NOTE Any new class members have to be added to the __eq__ comp 
# for unit testing to work!
class purchase:
    def __init__(self, id, description, cost):
        self.id = id
        self.description = description
        self.cost = cost
    def __eq__(self, other):
        if other is None:
            return False
        else:
            #check all members to make sure they are equal 
            isIdEqual = self.id == other.id
            isDescriptionEqual = self.description == other.description
            isCostEqual = self.cost == other.cost 
            return isIdEqual and isDescriptionEqual and isCostEqual

def getBalanceReport(spendString):
    #get rid of dodgy characters
    cleanString = getCleanString(spendString)
    thisAccountInfo = accountInfo()
    buildAccountInfo(thisAccountInfo, cleanString)
    thisAccountInfo.startingBalance = getStartingBalance(cleanString)
    return cleanString

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