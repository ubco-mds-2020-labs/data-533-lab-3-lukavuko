# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import unittest

from Mortgage_Package.financial.debtServiceRatio import *


# %%
class Test_debtServiceRatio_ratio(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Class setup for Debt Service Ratio')

    def setUp(self):
        self.buyer1 = debtServiceRatio(15000, 2400, 720, 360, 4800, 50000, 750000)
        self.buyer2 = debtServiceRatio(20000, 2400, 720, 360, 4800, 50000, 750000)
        self.buyer3 = debtServiceRatio(30000, 2400, 720, 360, 4800, 50000, 750000)
        self.buyer4 = debtServiceRatio(40000, 2400, 720, 360, 4800, 50000, 750000)
        self.buyer5 = debtServiceRatio(50000, 2400, 720, 360, 4800, 50000, 750000)
        self.buyer6 = debtServiceRatio(100000, 2400, 720, 360, 4800, 50000, 750000)
        self.buyer7 = debtServiceRatio(10000000, 2400, 720, 360, 4800, 50000, 750000)
        print('start test')

    def test_dsr_gds(self): #testcase1: Max annual mortgage payment
        self.assertEqual(self.buyer1.gds(), 1680)
        self.assertEqual(self.buyer2.gds(), 3280)
        self.assertEqual(self.buyer3.gds(), 6480)
        self.assertEqual(self.buyer4.gds(), 9680)
        self.assertEqual(self.buyer5.gds(), 12880)
        self.assertEqual(self.buyer6.gds(), 28880)
        self.assertEqual(self.buyer7.gds(), 50000)
        #self.assertTrue(self.buyer1.downpayment > self.buyer1.gds.gds_max_mortgage_annual)

    def test_dsr_tds(self): #testcase2
        self.assertNotEqual(self.buyer1.tds(), 1680)
        self.assertNotEqual(self.buyer2.tds(), 3280)
        self.assertNotEqual(self.buyer3.tds(), 6480)
        self.assertNotEqual(self.buyer4.tds(), 9680)
        self.assertNotEqual(self.buyer5.tds(), 12880)
        self.assertNotEqual(self.buyer6.tds(), 28880)
        self.assertEqual(self.buyer7.tds(), 50000)

    def tearDown(self):
        print('test complete')

    @classmethod
    def tearDownClass(cls):
        print('Class teardown for Debt Service Ratio')
        
#unittest.main(argv=[''], verbosity=2, exit=False) 


