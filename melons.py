"""Classes for melon orders."""
import random
from datetime import datetime

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    # Children classes require the following attributes:
    tax = None
    country_code = None
    order_type = None

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
        # self.time = datetime.now()
        # self.day = datetime.weekday(self.hour)
        
    def get_base_price(self):
        """Generate a Splurge random base price number"""

        base_price = random.randint(5, 9)

        # if self.hour >= 8 and self.hour <= 11 and self.day in range(0, 5):
        #     base_price += 4

        return base_price

    def get_total(self, base_price):
        """Calculate price, including tax."""

        if self.species == "Christmas melon":
            base_price *= 1.5 
        
        total = (1 + self.tax) * self.qty * base_price

        if self.country_code != "USA" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08
    country_code = "USA"


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)
        self.country_code = country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A goverment (non-US, non-internation) melon order."""
    passed_inspection = False


    def mark_inspection(self, passed):
        """Record if the order has passed inspection"""
        self.passed_inspection = True