from random import choice
"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """this will be our base class"""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False

    #get_base_price method:
    #this will choose random integer between 5 and 9
    #use this random integer in get_total
    def get_base_price(self):
        
        self.base_price = choice(range[5:10])
        return self.base_price

    def get_total(self):
        """Calculate price."""

        if self.species == "Christmas melon":
            int(self.base_price) = self.base_price * 1.5

        total = (1 + self.tax) * self.qty * self.base_price

        if self.order_type == "international" and self.qty < 10:
            total = total + 3

        return total

        #if christmas_melon:
        #   it will 1.5 times as much

        #if international_order and less than 10 melons:
        #    a flat fee of $3 added to total cost

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""        
        super(DomesticMelonOrder, self).__init__(species, qty)

        self.order_type = "domestic"
        self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty)
        """Initialize melon order attributes"""

        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """This is a government melon"""

    def __init__(self, species, qty):
        self.tax = 0
        self.passed_inspection = False

    def mark_inspection(self, passed):
        self.passed_inspection = True 
