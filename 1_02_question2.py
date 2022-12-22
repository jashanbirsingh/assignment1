a=float(input("Please enter your gross income: "))
b=int(input("Please enter the number of dependents: "))
#All taxpayers are allowed a standard deduction of $10,000
stand_ded=10000
#For each dependent, a taxpayer is allowed an additional $3,000 deduction
depend_ded=3000

#Total taxable income=gross income-standard deduction -(dependent deduction * No.of dependents)
Total_income=a-stand_ded-(depend_ded*b)

#Tax =Taxable  income * Tax rate
Tax=(Total_income*20)/100

print("taxable_income",Total_income)
print("tax",Tax)