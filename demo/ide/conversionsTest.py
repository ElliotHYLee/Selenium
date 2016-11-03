# -*- coding: utf-8 -*-
from selenium import selenium
import unittest, time, re

class test1(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "https://elliothylee.github.io/")
        self.selenium.start()
    
    def test_test1(self):
        sel = self.selenium
        sel.open("/Selenium/")
        sel.type("id=txtMeter1", "12")
        sel.type("id=txtMeter2", "13")
        sel.type("id=txtMeter3", "45")
        sel.type("id=txtMinute", "34")
        sel.click("id=btn1")
        try: self.assertEqual("39.37008", sel.get_value("id=txtFt"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        sel.click("id=btn2")
        try: self.assertEqual("0.008077823", sel.get_value("id=txtMile"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        sel.click("id=btn3")
        try: self.assertEqual("100", sel.get_value("id=txtYard"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        sel.click("id=btn4")
        try: self.assertEqual("2040.8888", sel.get_value("id=txtSec"))
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
