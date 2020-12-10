# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import unittest

from Mortgage_Package.financial.debtServiceRatio import *


# %%
class Test_cr_score(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Class setup for Credit Rating Score')

    def setUp(self):
        self.buyer1 = creditRating(20, 'own', 15000)
        self.buyer2 = creditRating(25, 'rent', 20000)
        self.buyer3 = creditRating(28, 'Own', 30000)
        self.buyer4 = creditRating(30, 'Rent', 40000)
        self.buyer5 = creditRating(35, 'OWN', 50000)
        self.buyer6 = creditRating(40, 'RENT', 100000)
        self.buyer7 = creditRating(50, 'oWn', 10000000)
        print('start test')
        
    def test_cr_score_sum(self): #testcase1
        self.assertEqual(score(self.buyer1), 465)
        self.assertEqual(score(self.buyer2), 400)
        self.assertEqual(score(self.buyer3), 610)
        self.assertEqual(score(self.buyer4), 525)
        self.assertEqual(score(self.buyer5), 665)
        self.assertEqual(score(self.buyer6), 585)
        self.assertEqual(score(self.buyer7), 735)
        
    def test_cr_approval(self): #testcase2
        self.assertTrue(score(self.buyer1) < 500)
        self.assertTrue(score(self.buyer2) < 500)
        self.assertTrue(score(self.buyer3) > 500)
        self.assertTrue(score(self.buyer4) > 500)
        self.assertTrue(score(self.buyer5) > 500)
        self.assertTrue(score(self.buyer6) > 500)
        self.assertTrue(score(self.buyer7) > 500)
        
    def tearDown(self):
        print('test complete')

    @classmethod
    def tearDownClass(cls):
        print('Class teardown for Credit Rating Score')
        
#unittest.main(argv=[''], verbosity=2, exit=False) 


