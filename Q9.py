maths=input("Enter marks of Maths")
physics=input("Enter marks of Physics")
chemistry=input("Enter marks of Chemistry")
biology=input("Enter marks of Biology")
english=input("Enter marks of English")
mean=(maths+physics+chemistry+biology+english)/5
perc=mean*100
print"mean=",mean
if(perc<=35):
    print"fail"
else:
    print"pass"
