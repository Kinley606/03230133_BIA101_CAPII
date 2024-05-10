#This code defines the constructor (__init__) method of the Deduction class, 
#which initializes the object's attributes pf_contribution, gis_contribution, and no_children with the values passed as arguments
class Deduction:
    def __init__(self, pf_contribution, gis_contribution, no_children):
        self.pf_contribution = pf_contribution
        self.gis_contribution = gis_contribution
        self.no_children = no_children

# This can validate pf_contribution for government contract employees
    def get_pf_deduction(self, annual_salary, emp_type, org_type):
        if org_type == 'government' and emp_type == 'contract' and self.pf_contribution != 0:
            raise ValueError("PF contribution for government contract employees is 0.")
        return self.pf_contribution

# 5% Group Insurance Scheme contribution
    def get_gis_deduction(self, annual_salary):
        gis_contribution = 0.05 * annual_salary  
        return gis_contribution

 #deductions for children (Nu. 350,000 per child)
    def get_child_deduction(self):
        child_deduction = 350000 * self.no_children 
        return child_deduction
#This code calculates the total deductions by summing up deductions
    def get_total_deductions(self, annual_salary, emp_type, org_type):
        pf_deduction = self.get_pf_deduction(annual_salary, emp_type, org_type)
        gis_deduction = self.get_gis_deduction(annual_salary)
        child_deduction = self.get_child_deduction()
        return pf_deduction + gis_deduction + child_deduction

#This code defines the constructor (__init__) method of the employee class
class Employee:
    def __init__(self, name, annual_salary, emp_type, org_type):
        self.name = name
        self.annual_salary = annual_salary
        self.emp_type = emp_type
        self.org_type = org_type

    def get_employee_details(self):
        return f"Name: {self.name}, annual_Salary: {self.annual_salary}, Employee Type: {self.emp_type}, Organization Type: {self.org_type}"

#This code defines the constructor (__init__) method of the personal income tax calculator class
class Personal_Income_Tax_Calculator:
    def __init__(self, employee, deduction):
        self.employee = employee
        self.deduction = deduction
        self.tax_slabs = [
            (0, 300000, 0),
            (300001, 400000, 0.1),
            (400001, 650000, 0.15),
            (650001, 1000000, 0.2),
            (1000001, 1500000, 0.25),
            (1500001, float('inf'), 0.3)
        ]

# This code calculates the taxable income by subtracting the total deductions
    def calculate_taxable_income(self):
        total_deductions = self.deduction.get_total_deductions(self.employee.annual_salary, self.employee.emp_type, self.employee.org_type)
        taxable_income = self.employee.annual_salary - total_deductions
        return taxable_income


 # This code check if the taxable income is below the minimum threshold and return 0 in that case.
    def calculate_tax(self):
        taxable_income = self.calculate_taxable_income()
        if taxable_income < 300000: 
            return 0 

#This code computes the tax amount by progressively taxing different income ranges at different rates based on the given tax brackets
        tax = 0
        tax_amount = 0
        for bracket_start, bracket_end, tax_rate in self.tax_slabs:
            if taxable_income > bracket_end:
                tax += (bracket_end - tax_amount) * tax_rate
                tax_amount = bracket_end
            else:
                tax += (taxable_income - tax_amount) * tax_rate
                break

        # Surcharge at the rate of 10% shall be levied on (PIT)
        # if the annual Personal Income Tax is equal to or more than Nu. 1,000,000
        if tax >= 1000000:
            tax *= 0.1  # 10% surcharge

        return tax

# Asking for user input to calulate the tax for particular users or employee 
name = input('Enter your name: ')
annual_salary = float(input("Enter your annual salary income: "))
emp_type = input("Enter your employee type (regular/contract): ")
org_type = input("Enter your organization type (government/private/corporate): ")
no_children = int(input("Enter the number of children: "))
pf_contribution = float(input("Enter your PF contribution: "))
gis_contribution = 0.05 * annual_salary  # 5% GIS contribution

# Creating instances of the classes for employee and deduction
employee = Employee(name, annual_salary, emp_type, org_type)
deduction = Deduction(pf_contribution, gis_contribution, no_children)
tax_calculator = Personal_Income_Tax_Calculator(employee, deduction)

#calculates the personal income tax amount by calling the calculate_tax method,
#and then prints the total tax amount payable along with the currency unit.
tax_payable = tax_calculator.calculate_tax()
print(f"Total tax amount payable by {employee.name} is Nu. {tax_payable}")