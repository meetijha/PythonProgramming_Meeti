def tax_rate_Calculator(sal):
    taxRate=0
    if(sal<30000):
        taxRate=5
    elif(30000<=sal<70000):
        taxRate=15
    else :
        taxRate=25
    return taxRate

sal=int(input("Enter salary : "))
taxRate=tax_rate_Calculator(sal)
print("Tax Rate =",taxRate)