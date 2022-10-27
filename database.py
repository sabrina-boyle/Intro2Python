## sabsing
## November 3, 2021
# This is my database class where I defined the database list and added supplier's to it as needed, and used user input to find the lowest cost for a part and which supplier offered it for Assignment 5
import supplier

class Database:
    def __init__(self):
        self.database = []
    def add_supplier(self, supplier):
        self.database.append(supplier)
    def find_part(self, selected_name):
        min_cost = -1
        part_cost = False
        company_name = False
        min_company = False
        for s in self.database:
            company_name, part_cost = s.find_part(selected_name)
            if company_name == False:
                continue
            else:
                if min_cost < 0:
                    min_cost = part_cost
                if part_cost <= min_cost:
                    min_cost = part_cost
                    min_company = company_name
                    
        return min_company, min_cost
             
            
        
        
