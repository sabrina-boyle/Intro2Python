## sabsing
## November 3, 2021
# This is my supplier class where I defined the company name, made a dictionary of the part and its cost, and found the cost of a specific cost while verifying it was in the supplier's database for Assignment 5
import part

class Supplier:
    def __init__(self, company_name):
        self.company_name = company_name
        self.parts = {}
    def add_part(self, part_name, part_cost):
        new_part = part.Part(part_name, part_cost)
        name = new_part.part_name
        price = new_part.part_cost
        self.parts[name] = price
    def find_part(self, part_name):
        part_cost = False
        company_name = False
        if part_name in self.parts:
            part_cost = self.parts[part_name]
            company_name = self.company_name
        return company_name, part_cost
