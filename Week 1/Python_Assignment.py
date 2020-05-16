import math 

def cartToPol():  #Function for converting from Cartesian to Polar
    print("Enter the X and Y Coordinates: ") #prompt to ask X and Y as inputs from user
    x = int(input())
    y = int(input())
    r = pow((x**2+y**2),1/2)  #calculation of r
    theta = math.atan(y/x)  #calculation of theta
    r = round(r, 4)      #all values are rounded upto 4 dp 
    theta = math.degrees(theta)    #theta displayed in degrees for simplicity purposes
    if (x < 0):     #To check which quadrant the coordinates lie in, and accordingly put value of theta
        theta = 180 + theta
    elif(y < 0):
        theta = (360 + theta)
    theta = round(theta, 4)
    return (r, theta)    #returning both r and theta
    
def polToCart():       #Function for converting from polar to Cartesian    
    print("Enter the r and theta (in degrees) values: ")   # Prompt to ask r and theta as inputs from user
    r = float(input())
    theta = int(input())
    theta = math.radians(theta)    #theta converted to radians for calculation purposes
    x = r*math.cos(theta)   #formulae for calculating X and Y  coordinates   
    y = r*math.sin(theta)
    x = round(x, 4)
    y = round(y, 4)
    return (x, y)  #returning both, X annd Y

print("Choose Conversion:")
print("1. Polar to Cartesian \t 2. Cartesian to Polar ")   #Display to ask Which conversion 
choice = int(input())
if (choice == 1):    #If-else ladder used for choosing which function to call, according to user input
    (x, y) = polToCart()     #calling the polar to cartesian function
    print("The converted coordinates are: ")
    print("(X, Y) = ({}, {})".format(x,y))     #displaying the final answer
elif (choice == 2):
    (r, theta) = cartToPol()    ##calling the cartesian to polar function
    print("The converted coordinates are: ")
    print("(r, theta) = ({}, {})".format(r,theta))     #displaying the final answer     
else:
    print("Incorrect Choice!")
    