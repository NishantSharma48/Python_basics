p=int(input("The principal is"))
t=int(input('The time period is'))
r = int(input('The rate of interest is'))
# calculates the compound interest
a=p*(1+(r/100))**t  # formula for calculating amount
ci=a-p  # compound interest = amount - principal amount
# printing compound interest value
print(ci)