az = int(input("Enter First Number: "))
bz = int(input("Enter Second Number: "))

def GCD(a, b):	
    if(b == 0):
        return a
    else:
        return(GCD(b, a%b))
        
answer = GCD(az, bz)
print("Greatest Common Denominator Doth Be:",str(answer)) 