# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import unittest

from Mortgage_Package.financial.debtServiceRatio import *


# %%
class Test_debtServiceRatio_mortgage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Class setup for Mortgage Offer and Minimum Downpayment')

    def setUp(self):
        self.buyer1 = debtServiceRatio(150000, 2400, 720, 360, 4800, 50000, 250000)
        self.buyer2 = debtServiceRatio(200000, 2400, 720, 360, 4800, 50000, 500000)
        self.buyer3 = debtServiceRatio(300000, 2400, 720, 360, 4800, 50000, 750000)
        self.buyer4 = debtServiceRatio(400000, 2400, 720, 360, 4800, 50000, 1000000)
        self.buyer5 = debtServiceRatio(500000, 2400, 720, 360, 4800, 50000, 2000000)
        self.buyer6 = debtServiceRatio(1000000, 2400, 720, 360, 4800, 50000, 4000000)
        self.buyer7 = debtServiceRatio(10000000, 2400, 720, 360, 4800, 50000, 8000000)
        print('start test')

    def test_mortgage_max(self): #testcase1
        self.assertEqual(mortgage_max(self.buyer1), 1000000)
        self.assertEqual(mortgage_max(self.buyer2), 1000000)
        self.assertEqual(mortgage_max(self.buyer3), 500000)
        self.assertEqual(mortgage_max(self.buyer4), 500000)
        self.assertEqual(mortgage_max(self.buyer5), 250000)
        self.assertEqual(mortgage_max(self.buyer6), 250000)
        self.assertEqual(mortgage_max(self.buyer7), 250000)

    def test_min_dp(self): #testcase2
        self.assertEqual(min_dp(self.buyer1), 44880)
        self.assertEqual(min_dp(self.buyer2), 50000)
        self.assertEqual(min_dp(self.buyer3), 50000)
        self.assertEqual(min_dp(self.buyer4), 50000)
        self.assertEqual(min_dp(self.buyer5), 50000)
        self.assertEqual(min_dp(self.buyer6), 50000)
        self.assertEqual(min_dp(self.buyer7), 50000)

    def tearDown(self):
        print('test complete')

    @classmethod
    def tearDownClass(cls):
        print('Class teardown for Mortgage Offer and Minimum Downpayment')
        
#unittest.main(argv=[''], verbosity=2, exit=False)


