# Input a number and the program will generate PI to the nth digit
import math # import the math module which includes pi
def RoundPitoNdigit(Rounddigit):
    if Rounddigit>0 and Rounddigit<10:
        Truncatedpi=round(math.pi,Rounddigit)
        pi=str(Truncatedpi)
    else:
        warning="You did not enter a number between 0 and 10."
        return warning
    return pi
YourN=input("Please Enter the digit that you want to round pi to(1-10):")
try:
    YourN=int(YourN)
    print(RoundPitoNdigit(YourN))
except:
    print("You did not enter an integer")
    
