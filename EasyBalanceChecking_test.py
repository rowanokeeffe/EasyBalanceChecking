#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import EasyBalanceChecking
 
class TestEasyBalanceCheck(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        pass
    def test_getPurchaseList(self):
        thisPurchaseList = []
        thisPurchase = EasyBalanceChecking.purchase(123, "Desc", 1.00)
        thisPurchaseList.append(thisPurchase)
        thatPurchaseList = EasyBalanceChecking.getPurchaseList("1000.00\n 123 Desc 1.00\n")
        self.assertEqual(thisPurchaseList[0], thatPurchaseList[0])

    def test_getTotalExpense(self):
        thisPurchaseList = []
        thisPurchase = EasyBalanceChecking.purchase(123, "Desc", 1.00)
        thisPurchaseList.append(thisPurchase)
        thisPurchase = EasyBalanceChecking.purchase(123, "Desc", 1.00)
        thisPurchaseList.append(thisPurchase)    
        thisPurchase = EasyBalanceChecking.purchase(123, "Desc", 1.00)
        thisPurchaseList.append(thisPurchase)
        thisPurchase = EasyBalanceChecking.purchase(123, "Desc", 1.00)
        thisPurchaseList.append(thisPurchase)    
        self.assertEqual(EasyBalanceChecking.getTotalExpense(thisPurchaseList), 4.00)
        thisPurchaseList = []
        self.assertEqual(EasyBalanceChecking.getTotalExpense(thisPurchaseList), 0.00)

    def test_getAverageExpense(self):
        thisPurchaseList = []
        thisPurchase = EasyBalanceChecking.purchase(123, "Desc", 1.00)
        thisPurchaseList.append(thisPurchase)
        thisPurchase = EasyBalanceChecking.purchase(123, "Desc", 1.00)
        thisPurchaseList.append(thisPurchase)    
        thisPurchase = EasyBalanceChecking.purchase(123, "Desc", 1.00)
        thisPurchaseList.append(thisPurchase)
        thisPurchase = EasyBalanceChecking.purchase(123, "Desc", 1.00)
        thisPurchaseList.append(thisPurchase)    
        self.assertEqual(EasyBalanceChecking.getAverageExpense(thisPurchaseList), 1.00)        
        thisPurchaseList = []
        self.assertEqual(EasyBalanceChecking.getAverageExpense(thisPurchaseList), 0.00)

    def test_getStartingBalance(self):
        self.assertEqual(EasyBalanceChecking.getStartingBalance("1000.00\n 34455.67\n"), 1000.00)

    def test_getCleanString(self):
        self.assertEqual(EasyBalanceChecking.getCleanString("\n£3$4!.& aFrg"),"34. aFrg")

    def test_getBalanceReport(self):
        self.assertEqual(EasyBalanceChecking.getBalanceReport(
            "1000.00\n" \
            "125 Market 125.45\n" \
            "126 Hardware 34.95\n" \
            "127 Video 7.45\n" \
            "128 Book 14.32\n" \
            "129 Gasoline 16.10\n"),
            "Original Balance: 1000.00\n" \
            "125 Market 125.45 Balance 874.55\n" \
            "126 Hardware 34.95 Balance 839.60\n" \
            "127 Video 7.45 Balance 832.15\n" \
            "128 Book 14.32 Balance 817.83\n" \
            "129 Gasoline 16.10 Balance 801.73\n" \
            "Total expense  198.27\n" \
            "Average expense  39.65\n" \
            )
        self.assertEqual(EasyBalanceChecking.getBalanceReport(
            "\n" \
            "1000.00\n" \
            "125 Market 125.45\n" \
            "\n" \
            "126 Hardware 34.95\n" \
            "127 Video 7.45\n" \
            "128 Book 14.32\n" \
            "129 Gasoline 16.10\n"),
            "Original Balance: 1000.00\n" \
            "125 Market 125.45 Balance 874.55\n" \
            "126 Hardware 34.95 Balance 839.60\n" \
            "127 Video 7.45 Balance 832.15\n" \
            "128 Book 14.32 Balance 817.83\n" \
            "129 Gasoline 16.10 Balance 801.73\n" \
            "Total expense  198.27\n" \
            "Average expense  39.65\n" \
            )

if __name__ == '__main__':
    unittest.main()