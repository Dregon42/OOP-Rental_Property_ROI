class ROI():
    
    def __init__(self, total_income = 0, total_expenses = 0, cash_flow = 0, total_investment = 0):
        self.total_income = total_income
        self.total_expenses = total_expenses
        self.cash_flow = cash_flow
        self.total_investment = total_investment

    def roi(self):
        return float((self.cash_flow * 12) / self.total_investment) * 100
    
class Calculate(ROI):

    def __int__(self, total_income, total_expenses, cash_flow, total_investment):
        super().__init__(total_income, total_expenses, cash_flow, total_investment)
        

    def income(self):
        # print("Monthly Income")
        rental = int(input("Rent income? "))
        laundry = int(input('Laundry income? '))
        storage = int(input('Storage income? '))
        misc = int(input('Misc. income? '))
        self.total_income += rental + laundry + storage + misc
        print(f'Your monthly income: {self.total_income}')


    def expense(self):
        # print('Monthly Expenses')
        tax = int(input('Monthly taxes? '))
        insurance = int(input('Monthly insurance cost? '))
        utlities = int(input('Monthly utility cost? '))
        vacancy = int(input('Vacancy savings(rental income * 5%)'))
        repair = int(input('Monthly savings for repairs? '))
        capEx = int(input('Monthly savings for future renovations? '))
        property_management = int(input('Mothly cost for property manager? '))
        mortgage = int(input('Monthly mortgage payment? '))
        self.total_expenses = tax + insurance + utlities + vacancy + repair + capEx + property_management + mortgage
        print(f'Your monthly expenses: {self.total_expenses}')


    def cashFlow(self):
        self.cash_flow = self.total_income - self.total_expenses

    def investment(self):
        down_payment = int(input('Down payment '))
        closing_cost = int(input('Closing cost '))
        rehab = int(input('Rehab budget '))
        misc = int(input('Misc investment cost '))
        self.total_investment = down_payment + closing_cost + rehab + misc



test_property = Calculate()


def run():
    print("INCOME")
    test_property.income()
    print("EXPENSES")
    test_property.expense()
    print("CASH FLOW")
    test_property.cashFlow()
    print('INVESTMENT')
    test_property.investment()
    print(f'Property ROI: {test_property.roi()}')


run()
