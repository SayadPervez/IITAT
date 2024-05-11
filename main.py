import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

def calculateTaxOldRegime(salary):
    tax = 0
    if(salary<=2_50_000):
        pass # no tax poor fellow
    elif(2_50_001<=salary<=5_00_000):
        salary = salary-2_50_000
        tax += (5/100)*salary
    elif(5_00_001<=salary<=10_00_000):
        tax += 12_500
        salary = salary-5_00_000
        tax += (20/100)*salary
    elif(salary>=10_00_001):
        tax += 1_12_500
        salary = salary-10_00_000
        tax += (30/100)*salary
    return tax

def calculateTaxNewRegime(salary):
    salary = salary - 50_000 # 50 k Standard Deduction
    tax = 0
    if(salary<=3_00_000):
        pass # no tax poor fellow
    elif(3_00_001<=salary<=6_00_000):
        salary = salary-3_00_000
        tax += (5/100)*salary
    elif(6_00_001<=salary<=9_00_000):
        tax += 15_000
        salary = salary-6_00_000
        tax += (10/100)*salary
    elif(9_00_001<=salary<=12_00_000):
        tax += 45_000
        salary = salary-9_00_000
        tax += (15/100)*salary
    elif(12_00_001<=salary<=15_00_000):
        tax += 90_000
        salary = salary-12_00_000
        tax += (20/100)*salary
    elif(salary>=15_00_001):
        tax += 1_50_000
        salary = salary-15_00_000
        tax += (30/100)*salary
    return tax

def plot_tax_comparison(my_salary, deductableInvestments=0):

    if(my_salary - deductableInvestments <=0):
        print("Black Money huh ?")

    if(my_salary==None or my_salary<=5_00_000):
        salary_range = range(2_50_000, 7_50_000, 5000)
    else:
        salary_range = range(my_salary - 4_50_000 , my_salary + 4_50_000 , 5000)

    old_taxes = [calculateTaxOldRegime(salary) for salary in salary_range]    
    new_taxes = [calculateTaxNewRegime(salary) for salary in salary_range]

    plt.figure(figsize=(10, 6))
    plt.plot(salary_range, new_taxes, label="New Regime Tax", color="blue")
    plt.xlabel("Salary (₹) - Standard Deduction (₹ deductableInvestments)")
    plt.ylabel("Tax (₹)")
    plt.title("Comparison of Tax Regimes")

    old_taxes_ppf = [calculateTaxOldRegime(salary-deductableInvestments) for salary in salary_range]
    plt.plot(salary_range, old_taxes_ppf, label="Old Regime Tax - deductableInvestments", color="orange")
    plt.plot(salary_range, old_taxes, label="Old Regime Tax", color="red")

    plt.axvline(x=my_salary, color='green', linestyle='--')


    ax = plt.gca()
    ax.xaxis.set_major_formatter(FormatStrFormatter('%d'))
    ax.xaxis.set_major_locator(plt.MaxNLocator(10))

    plt.legend()
    plt.grid(True)

    plt.text(0.95, 0.05, 
        f"Your Net Income = {my_salary}\nAmount after Investments = {my_salary - deductableInvestments}\nWith Old Regime, Your Tax = {calculateTaxOldRegime(my_salary)}\nWith Old Regime, given investments, Your tax = {calculateTaxOldRegime(my_salary - deductableInvestments)}\nWith New Regime, Your Tax = {calculateTaxNewRegime(my_salary)}", 
         horizontalalignment='right', verticalalignment='bottom', 
         transform=ax.transAxes, fontsize=10)

    plt.scatter(my_salary, calculateTaxOldRegime(my_salary - deductableInvestments), color='Orange', s=50)
    plt.scatter(my_salary, calculateTaxOldRegime(my_salary), color='Red', s=50)
    plt.scatter(my_salary, calculateTaxNewRegime(my_salary), color='Blue', s=50)

    plt.show()


my_ctc = int(input("Enter your CTC = "))
my_psp = int(input("Enter your PSP = "))
my_net_income = my_ctc + my_psp

inp = input("Enter your Tax saving Investment (0 by default) = ")
try:
    deductableInvestments =  int(inp)
except Exception as e:
    deductableInvestments = 0

plot_tax_comparison(my_net_income, deductableInvestments)