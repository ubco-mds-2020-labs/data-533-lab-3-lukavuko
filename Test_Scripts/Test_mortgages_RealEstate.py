#!/usr/bin/env python
# coding: utf-8


from Mortgage_Package.mortgages.mortgages import *

import unittest

class Test_mortgages_RealEstate(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('!!! Class setup for Test(mortgages_RealEstate) !!!')
    
    def setUp(self):
        self.prop1 = RealEstate(prop = 'Clearview Residential Five Story Apartment',
                                price = 4800000,
                                prop_owner = 'Brookfield Asset Management',
                                prov = 'ON')
        self.prop2 = RealEstate(prop = 'Surrey Community Centre',
                                price = 1905000,
                                prop_owner = 'City of Vancouver',
                                prov = 'BC')
        print('~~~ start test ~~~')

    
    def test_getProp(self):
        self.assertEqual(self.prop1.getProp(), 'Clearview Residential Five Story Apartment')
        self.assertEqual(self.prop2.getProp(), 'Surrey Community Centre')
        
        ## Change values
        self.prop1.prop = 'X'
        self.prop2.prop = 'Y'
        
        self.assertNotEqual(self.prop1.getProp(), 'Clearview Residential Five Story Apartment')
        self.assertNotEqual(self.prop2.getProp(), 'Surrey Community Centre')
    
    
    def test_getPrice(self):
        self.assertEqual(self.prop1.getPrice(), 4800000)
        self.assertEqual(self.prop2.getPrice(), 1905000)
        self.assertEqual(self.prop1.getPrice() + self.prop2.getPrice(), 4800000 + 1905000)
        
        ## Change values
        self.prop1.price = 0
        self.prop2.price = 0
        
        self.assertNotEqual(self.prop1.getPrice(), 4800000)
        self.assertNotEqual(self.prop2.getPrice(), 1905000)
   

    def test_getPropOwner(self):
        self.assertEqual(self.prop1.getPropOwner(), 'Brookfield Asset Management')
        self.assertEqual(self.prop2.getPropOwner(), 'City of Vancouver')
        
        ## Change values
        self.prop1.prop_owner = 'X'
        self.prop2.prop_owner = 'Y'
        
        self.assertNotEqual(self.prop1.getPropOwner(), 'Brookfield Asset Management')
        self.assertNotEqual(self.prop2.getPropOwner(), 'City of Vancouver')
        
        
    def test_getProv(self):
        self.assertEqual(self.prop1.getProv(), 'ON')
        self.assertEqual(self.prop2.getProv(), 'BC')
    
        ## Change values
        self.prop1.prov = 'X'
        self.prop2.prov = 'Y'
        
        self.assertNotEqual(self.prop1.getProv(), 'ON')
        self.assertNotEqual(self.prop2.getProv(), 'BC')
        
        
    def tearDown(self):
        print('~~~ complete ~~~')  
        
    @classmethod
    def tearDownClass(cls):
        print('!!! Class teardown for Test(mortgages_RealEstate) !!!\n\n\n')

#unittest.main(argv=[''], verbosity=2, exit=False)