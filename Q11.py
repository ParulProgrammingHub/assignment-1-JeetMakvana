principle=input("Enter The Principle Amount")
rate=input("Enter The Interest Rate")
time=input("Enter The Time In Years")
def compound_interest(pr,rt,ti):
    i=1
    final =0
    while(i<=ti):
        ci=pr*rt/100
        pr=pr+ci
        final=final+ci
        i =i+1
    print"The Compound Interest Is",final
compound_interest(pr=principle,rt=rate,ti=time)
