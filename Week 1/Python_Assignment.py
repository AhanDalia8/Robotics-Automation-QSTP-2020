import math 

def cartToPol():
    print("Enter the X and Y Coordinates: ")
    x = int(input())
    y = int(input())
    r = pow((x**2+y**2),1/2)
    theta = math.atan(y/x)
    r = round(r, 4)
    theta = math.degrees(theta)
    if (x < 0):
        theta = 180 + theta
    elif(y < 0):
        theta = (360 + theta)
    theta = round(theta, 4)
    return (r, theta)
    
def polToCart():
    print("Enter the r and theta values: ")
    r = float(input())
    theta = int(input())
    theta = math.radians(theta)
    x = r*math.cos(theta)
    y = r*math.sin(theta)
    x = round(x, 4)
    y = round(y, 4)
    return (x, y)

print("Choose Conversion:")
print("1. Polar to Cartesian \t 2. Cartesian to Polar ")
choice = int(input())
if (choice == 1):
    (x, y) = polToCart()
    print("The converted coordinates are: ")
    print("(X, Y) = ({}, {})".format(x,y))
elif (choice == 2):
    (r, theta) = cartToPol()
    print("The converted coordinates are: ")
    print("(r, theta) = ({}, {})".format(r,theta))
else:
    print("Incorrect Choice!")
    