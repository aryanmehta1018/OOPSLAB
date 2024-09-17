import math
def distance(x1,x2,y1,y2):
    return math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
x1=int(input("Enter x1:"))
y1=int(input("Enter y1:"))
x2=int(input("Enter x2:"))
y2=int(input("Enter y2:"))
print("%.6f"%distance(x1,x2,y1,y2))
