# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import unittest

from Mortgage_Package.financial.creditRating import *


# %%
class Test_cr_conversion(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Class setup for Credit Rating Conversions')

    def setUp(self):
        self.buyer1 = creditRating(20, 'own', 15000)
        self.buyer2 = creditRating(25, 'rent', 20000)
        self.buyer3 = creditRating(28, 'Own', 30000)
        self.buyer4 = creditRating(30, 'Rent', 40000)
        self.buyer5 = creditRating(35, 'OWN', 50000)
        self.buyer6 = creditRating(40, 'RENT', 100000)
        self.buyer7 = creditRating(50, 'oWn', 10000000)
        print('start test')

    def test_convert_age(self): #testcase1
        self.assertEqual(self.buyer1.convert_age(), 100)
        self.assertEqual(self.buyer2.convert_age(), 120) 
        self.assertEqual(self.buyer3.convert_age(), 185)
        self.assertEqual(self.buyer4.convert_age(), 200)
        self.assertEqual(self.buyer5.convert_age(), 210)
        self.assertEqual(self.buyer6.convert_age(), 225)
        self.assertEqual(self.buyer7.convert_age(), 250)
        

    def test_convert_home(self): #testcase2
        self.assertEqual(self.buyer1.convert_home(), 225)
        self.assertEqual(self.buyer2.convert_home(), 100)
        self.assertEqual(self.buyer3.convert_home(), 225)
        self.assertEqual(self.buyer4.convert_home(), 100)
        self.assertEqual(self.buyer5.convert_home(), 225)
        self.assertEqual(self.buyer6.convert_home(), 100)
        self.assertEqual(self.buyer7.convert_home(), 225)
        

    def test_convert_income(self): #testcase3
        self.assertEqual(self.buyer1.convert_income(), 140)
        self.assertEqual(self.buyer2.convert_income(), 180)
        self.assertEqual(self.buyer3.convert_income(), 200)
        self.assertEqual(self.buyer4.convert_income(), 225)
        self.assertEqual(self.buyer5.convert_income(), 230)
        self.assertEqual(self.buyer6.convert_income(), 260)
        self.assertEqual(self.buyer7.convert_income(), 260)
        
    def tearDown(self):
        print('test complete')

    @classmethod
    def tearDownClass(cls):
        print('Class teardown for Credit Rating Conversions')

#unittest.main(argv=[''], verbosity=2, exit=False) 


