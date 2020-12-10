# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
class debtServiceRatio:
    """
    A class used to calculate debt service ratios and determine maximum annual and monthly mortgage payments
    
    ...

    Attributes
    ----------
    income : numeric
        home buyer's annual income
    property_tax : numeric
        home buyer's annual property tax
    heat_cost : numeric
        home buyer's annual heat cost
    car_payment : numeric
        home buyer's annual car payment
    credit_card_payment : numeric
        home buyer's annual credt card payment
    downpayment : int
        home buyer's proposed downpayment
    home_price : int
        home buyer's desired home price
    months : int
        months in one year
    gds_ratio : float
        current ratio for Gross Debt Service
    gds_max_annual_spend : numeric
        calculates home buyer's maximum annual spending available
    gds_max_mortgage_annual : numeric
        calculates home buyer's maximum annual mortgage payments
    gds_max_mortgage_monthly : numeric
        calculates home buyer's maximum monthly mortgage payments
    tds_ratio : numeric
        current ratio for Total Debt Service
    tds_max_annual_spend : numeric
        calculates home buyer's maximum annual spending available
    tds_max_mortgage_annual : numeric
        calculates home buyer's maximum annual mortgage payments
    tds_max_mortgage_monthly : numeric
        calculates home buyer's maximum monthly mortgage payments

    Methods
    -------
    gds()
        Calculates buyer's max annual spending, max annual mortgage payment, and max monthly mortgage payments based on Gross Debt Service Ratio of 32%
    tds()
        Calculates buyer's max annual spending, max annual mortgage payment, and max monthly mortgage payments based on Total Debt Service Ratio of 40%

    """
    
    downpayment = 0

    def __init__(self, income, property_tax, heat_cost, car_payment, credit_card_payment, downpayment, home_price):
        """
        Attributes
        ----------
        income : numeric
        property_tax : numeric
        heat_cost : numeric
        car_payment : numeric
        credit_card_payment : numeric
        downpayment : int
        home_price : int

        """

        self.income = income
        self.property_tax = property_tax
        self.heat_cost = heat_cost
        self.car_payment = car_payment
        self.credit_card_payment = credit_card_payment
        self.downpayment = downpayment
        self.home_price = home_price

    def gds(self, prin = False): #max affordability based on GDS score
        """
        Calculates buyer's max annual spending, max annual mortgage payment, and max monthly mortgage payments based on Gross Debt Service Ratio of 32%
        ...

        Attributes
        ----------

        gds_ratio : float
        months : int
        gds_max_annual_spend = float
        gds_max_mortgage_annual = float
        gds_max_mortgage_monthly = float

        Returns
        -------
        gds_max_mortgage_annual : float
        self.downpayment : float
        
        """
        gds_ratio = 0.32 #change to 0.35
        months = 12

        gds_max_annual_spend = self.income * gds_ratio
        gds_max_mortgage_annual = gds_max_annual_spend - self.property_tax - self.heat_cost
        gds_max_mortgage_monthly = gds_max_mortgage_annual / months
        
        if prin == True:
            print("Max Annual Spending: ${}".format(gds_max_annual_spend))
            print("Max Annual Mortgage Payment: ${}".format(gds_max_mortgage_annual))
            print("Max Monthly Mortgage Payment: ${}".format(gds_max_mortgage_monthly))
        #return (max_annual_spend, max_mortgage_annual, max_mortgage_monthly)

        if self.downpayment > gds_max_mortgage_annual:
            downpayment = gds_max_mortgage_annual
            if prin == True:
                print("Your downpayment: ${}".format(gds_max_mortgage_annual))
            return gds_max_mortgage_annual
        else:
            downpayment = self.downpayment
            if prin == True:
                print("Your downpayment: ${}".format(self.downpayment))
            return self.downpayment #######

    def tds(self, prin = False): #max affordability based on TDS score
        """
        Calculates buyer's max annual spending, max annual mortgage payment, and max monthly mortgage payments based on Total Debt Service Ratio of 40%
        ... 
        
        Attributes
        ----------

        tds_ratio : float
        months : 12
        tds_max_annual_spend = float
        tds_max_mortgage_annual = float
        tds_max_mortgage_monthly = float

        Returns
        -------
        tds_max_mortgage_annual : float
        self.downpayment : float
        
        """
        
        tds_ratio = 0.40 # change to 0.42
        months = 12

        tds_max_annual_spend = self.income * tds_ratio
        tds_max_mortgage_annual = tds_max_annual_spend - self.property_tax - self.heat_cost - self.car_payment - self.credit_card_payment
        tds_max_mortgage_monthly = tds_max_mortgage_annual / months
        if prin == True:
            print("Max Annual Spending: ${}".format(tds_max_annual_spend))
            print("Max Annual Mortgage Payment: ${}".format(tds_max_mortgage_annual))
            print("Max Monthly Mortgage Payment: ${}".format(tds_max_mortgage_monthly))

        if self.downpayment > tds_max_mortgage_annual: #
            downpayment = tds_max_mortgage_annual
            if prin == True:
                print("Your downpayment: ${}".format(tds_max_mortgage_annual))
            return tds_max_mortgage_annual #######
        else:
            downpayment = self.downpayment
            if prin == True:
                print("Your downpayment: ${}".format(self.downpayment))
            return self.downpayment #######


# %%
def mortgage_max(buyer_dsr):
    """
    Calculates maximum loan available to offer based on buyer's proposed downpayment and downpayment percent
    ...

    Returns
    -------
    loan : float
        Returns maximum available loan to be offered
    """

    downpayment_percent = 0

    if buyer_dsr.home_price <= 500000:
        downpayment_percent = 0.05
    elif buyer_dsr.home_price > 500000 and buyer_dsr.home_price <= 1000000:
        downpayment_percent = 0.1
    else:
        downpayment_percent = 0.2

        #loan = self.max_dp() / downpayment_percent
    loan = buyer_dsr.downpayment / downpayment_percent
    return loan

def min_dp(buyer_dsr, pri = False):
    """
    Compares Gross Debt Service Ratio and Total Debt Service Ratio and returns expected annual and monthly maximum mortgage payments and minimum downpayment

    Return
    ------
    float
        minimum downpayment
    """
    return min(buyer_dsr.gds(prin = pri), buyer_dsr.tds(prin = pri))


# %%
buyer_dsr = debtServiceRatio(75000, 3600, 2400, 3600, 3000, 30000, 200000)


# %%
mortgage_max(buyer_dsr)


# %%
# max_dp(buyer_dsr, pri = True)


# %%



