#def main():
    #from math import sqrt
import math

def calcular_PEMDAS():
    a= 4
    b= 5
    oper1= (2*(3/4) + 4*(2/3) - 3*(1/5) + 5*(1/2))
    oper2= ((2*(math.sqrt(35))**2) + (4*(math.sqrt(36))**3) - (6*(math.sqrt(49))**2))
    oper3= ((a**3 + 2*b**2) / (4*a))
    oper4= ((2*(a+b)**2 + 4*(a-b)**2)) / ((a)*(b)**2)
    oper5= (math.sqrt((a+b)**2 + 2**(a+b)) / (2*a+2*b)**2)
      
          
    print (round (oper1,4))
    print (round (oper2,4))
    print (round (oper3,4))
    print (round (oper4,4))
    print (round (oper5,4))
       
calcular_PEMDAS()
