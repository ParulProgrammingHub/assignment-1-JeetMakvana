principle=input("Enter Principle Amount")
time=input("Enter Time")
rate=input("Enter Interest Rate")
def simple_interest(pa,ti,ra):
    si=(principle*rate/100)*time;
    print"The Simple Interest Is",si
simple_interest(pa=principle,ti=time,ra=rate)
