#!/usr/bin/env python
# coding: utf-8

# In[13]:


class RealEstate:
    '''
    A class for real estate assets in CAD 
    
    ...
    
    Attributes
    ----------
    prop : str
        Name identifier for the property ('Clearview Residential Home')
        
    price : numeric > 0
        Property value
        
    prop_owner : str
        Name identifier ('Brookfield Asset Management')
        
    prov : str
        Canadian provicial identifier (BC, ON, QC...)

    props_initialized : int
        Number of properties currently initialized in memory (counter)
    
    Methods
    -------
    getProp():
        Returns property name or ID defined by the legal owner.
    
    getPrice():
        Returns asset price.
    
    getPropOwner():
        Returns legal owner of the asset.
    
    getProv():
        Returns Provincial location of the asset.
    '''    
    props_initialized = 0
    
    def __init__(self, prop = None, price = None, prop_owner = None, prov = None):
        "Initializes the real estate asset."
        self.prop = prop
        self.price = price
        self.prop_owner = prop_owner
        self.prov = prov
        RealEstate.props_initialized += 1
    
    def __repr__(self):
        return f'''{self.prop}
    Price: ${self.price}
    Legal owner : {self.prop_owner}
    Province: {self.prov}'''
    
    def __str__(self):
        return f'''{self.prop}
    Price: ${self.price}
    Legal owner : {self.prop_owner}
    Province: {self.prov}'''
    
    def getProp(self):
        "Returns property name or ID defined by the legal owner."
        return self.prop
    
    def getPrice(self):
        "Returns asset price."
        return self.price
    
    def getPropOwner(self):
        "Returns legal owner of the asset."
        return self.prop_owner
    
    def getProv(self):
        "Returns Provincial location of the asset."
        return self.prov


# In[14]:


class Residential(RealEstate):
    '''
    A class for residential real estate assets in CAD.
    
    ...
    
    Attributes
    ----------
    prop : str
        Name identifier for the property ('Clearview Residential Home')
        
    price : numeric > 0
        Property value
        
    prop_owner : str
        Name identifier ('Brookfield Asset Management')
        
    area : str
        Name of residential area
        
    city : str
        Name of city
        
    prov : str
        Canadian provicial identifier (BC, ON, QC...)
        
    sq_footage : int
        Property square footage
    
    year_built : int
        Year property was constructed
        
    Methods
    -------
    getArea():
        Returns area or community the property is located in.
    
    getCity():
        Returns city the property is located in.
    
    getSq_footage():
        Returns square footage of the property.
    
    getYear_built():
        Returns year property was built.
    
    Inherited Methods
    -----------------
    getProp():
        Returns property name or ID defined by the legal owner.
    
    getPrice():
        Returns asset price.
    
    getPropOwner():
        Returns legal owner of the asset.
    
    getProv():
        Returns Provincial location of the asset.
    '''
    
    def __init__(self, prop = None,
                 price = None,
                 prop_owner = None, 
                 area = None,
                 city = None,
                 prov = None, 
                 sq_footage = None,
                 year_built = None):
        "Initializes the real estate asset."
        self.area = area
        self.city = city
        self.sq_footage = sq_footage
        self.year_built = year_built
        RealEstate.__init__(self, prop, price, prop_owner, prov)
        
    def __repr__(self):
        return f'''{self.prop}
    Price: ${self.price}
    Legal owner : {self.prop_owner}
    Area: {self.area}
    City: {self.city}
    Province: {self.prov}
    Square Footage: {self.sq_footage}
    Year Built: {self.year_built}'''
    
    def __str__(self):
        return f'''{self.prop}
    Price: ${self.price}
    Legal owner : {self.prop_owner}
    Area: {self.area}
    City: {self.city}
    Province: {self.prov}
    Square Footage: {self.sq_footage}
    Year Built: {self.year_built}'''
        
    def getArea(self):
        "Returns area or community the property is located in."
        return self.area
    
    def getCity(self):
        "Returns city the property is located in."
        return self.city
    
    def getSq_footage(self):
        "Returns square footage of the property."
        return self.sq_footage
    
    def getYear_built(self):
        "Returns year property was built."
        return self.year_built

## Other real estate sub classes to consider for future projects:
# class Land(RealEstate): 
# class Commercial(RealEstate)
# class Industrial(RealEstate)


# In[ ]:




