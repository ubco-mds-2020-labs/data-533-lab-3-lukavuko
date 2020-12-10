#!/usr/bin/env python
# coding: utf-8


from Mortgage_Package.mortgages.mortgage_estimator import *

import unittest

class Test_mortgage_estimator_propertyfilter(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        ## Import dependencies
        import warnings, pandas as pd, numpy as np
        print('!!! Class setup for Test(mortgage_estimator_propertyfilter) !!!')
    
    def setUp(self):
        ## Import property dataset
        self.df = pd.read_csv('vancouver_area_testing_set.csv', header = 0)
        self.df = self.df.loc[:,['Area', 'House Price']]
        
        ## Prior knowns for 4 test sets for the property filter 
        self.downpayment = np.linspace(100000, 600000, 4)
        self.mortgage_rate = np.linspace(1.6, 3.8, 4)
        self.mortgage_term = np.linspace(1, 10, 4)
        self.max_monthly_payment = np.linspace(1500, 11000, 4)
        self.max_loan = np.linspace(100000, 600000, 4)/0.05 
        
        print('~~~ start test ~~~')
        
        
    def test_property_filter(self):
        self.expected1 = [True, 'East Burnaby', 'North Vancouver', 'North Vancouver']
        self.expected2 = [True, 'East Burnaby', 'North Vancouver', 'West Vancouver']
        
        ## Test first case to ensure returned dataframe is empty:
        self.assertTrue(property_filter(property_data = self.df,
                                        downpayment = self.downpayment[0],
                                        mortgage_rate = self.mortgage_rate[0],
                                        max_monthly_payment = self.max_monthly_payment[0],
                                        max_loan = self.max_loan[0]).empty) 
        self.assertTrue(property_filter(property_data = self.df,
                                        downpayment = self.downpayment[0],
                                        mortgage_term = self.mortgage_term[0],
                                        max_monthly_payment = self.max_monthly_payment[0],
                                        max_loan = self.max_loan[0]).empty)
        
        ## Test last three cases where return is a non empty dataframe
        for i in range(1, 4):
            
            ## Testing with known mortgage rate
            self.assertEqual((property_filter(property_data = self.df,
                                             downpayment = self.downpayment[i],
                                             mortgage_rate = self.mortgage_rate[i],
                                             max_monthly_payment = self.max_monthly_payment[i],
                                             max_loan = self.max_loan[i]).iloc[0, 0]), self.expected1[i]) 

            ## Testing with unknown mortgage rate
            self.assertEqual(property_filter(property_data = self.df,
                                             downpayment = self.downpayment[i],
                                             mortgage_term = self.mortgage_term[i],
                                             max_monthly_payment = self.max_monthly_payment[i],
                                             max_loan = self.max_loan[i]).iloc[0, 0], self.expected2[i])

            
    def tearDown(self):
        print('~~~ complete ~~~')  
        
    @classmethod
    def tearDownClass(cls):
        print('!!! Class teardown for Test(mortgage_estimator_propertyfilter) !!!\n\n\n')


#unittest.main(argv=[''], verbosity=2, exit=False)


