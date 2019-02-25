
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#takes in a clean string and an account report and populates the structure
class accountInfo:
    def __init__(self, string):
        self.startingBalance = getStartingBalance(string)
        self.purchaseList = getPurchaseList(string)    
        self.totalExpense = getTotalExpense(self.purchaseList)
        self.averageExpense = getAverageExpense(self.purchaseList)

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
    #now each line should have id, desc and value seperated by spaces
    for line in splitString:
        #get rid of the spaces and make a copy of the members
        splitLine = line.split()
        id = int(splitLine[0])
        desc = splitLine[1]
        value = float(splitLine[2])
        thisPurchase = purchase(id, desc, value)
        #store and check the next one
        purchaseList.append(thisPurchase)
    return purchaseList

#returns the sum of the purchases in passed in purchaseList
def getTotalExpense (purchaseList):
    totalExpense = 0.0
    for purchase in purchaseList:
        totalExpense += purchase.cost
    return totalExpense

#Takes in the purchase list and returns the average expense
def getAverageExpense (purchaseList):
    #if we have some purchases get the average spend
    if len(purchaseList) > 0:
        totalExpense = getTotalExpense(purchaseList)
        averageExpense = totalExpense / float(len(purchaseList))
    else:
        #NOTE: Needs fault reporting for no purchases.
        averageExpense = 0.0
    return averageExpense

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
    #populate the account info class
    thisAccountInfo = accountInfo(cleanString)
    #turn it into a string
    report = buildAccountReport(thisAccountInfo)
    return report


def buildAccountReport(accountInfo):
    currentBalance = float(accountInfo.startingBalance)
    report = "Original Balance: " + "{:.2f}".format(currentBalance) + "\n"
    for purchase in accountInfo.purchaseList:
        report += str(purchase.id) + " "
        report += str(purchase.description) + " "
        report += "{:.2f}".format(purchase.cost) + " "
        #Store the balance after this purchase
        currentBalance -= purchase.cost        
        report += "Balance " + "{:.2f}".format(currentBalance)
        report += "\n"
    report += "Total expense  " + "{:.2f}".format(accountInfo.totalExpense) + "\n"
    report += "Average expense  " + "{:.2f}".format(accountInfo.averageExpense) + "\n"
    return report


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
    cleanString = cleanString.replace("\n\n", '\n')
    #Delete new line if it is on the front
    while cleanString[0] == '\n':
        cleanString = cleanString[1:]
    return cleanString

def main():
    return 0


if __name__ == '__main__':
    main()