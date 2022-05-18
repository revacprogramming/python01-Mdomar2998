# Conditional Execution

hrs = input("Enter Hours:")
h = float(hrs)
rate=input("enter the rate:")
r=float(rate)
gp=(h*r)
if gp<40:
    print(gp)
elif h>40:
    print(40*r + (h-40)*1.5*r)
