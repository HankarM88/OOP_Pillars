
# Create a Point class that create objects of Points having coordinates(x,y)

class Point:
    # A Point instance models a 2D point with x and y coordinates

    def __init__(self, x = 0, y = 0):
        #Initializer, which creates the instance variables x and y with default of (0, 0)
        self.x = x
        self.y = y

    def __str__(self):
        # Return a descriptive string for this instance
        return f'({self.x}, {self.y})'

    def __repr__(self):
        #Return a command string to re-create this instance
        return f'Point({self.x}, {self.y})'

    def __add__(self, other):
        #Override the '+' operator: create and return a new instance
        p = Point(self.x + other.x, self.y + other.y)
        return p

    def __mul__(self, factor):
        #Override the '*' operator: modify and return this instance
        self.x *= factor
        self.y *= factor
        return self

# Testing
if __name__ == '__main__':
    A = Point()
    print(f'A : {repr(A)}')      # (0.00, 0.00)
    #affect values to the cordinates
    A.x = 5
    A.y = 6
    print(f'A : {repr(A)}')      # (5.00, 6.00)
    #create the Point B
    B = Point(3, 4)
    print(f'B : {repr(B)}')     # (3.00, 4.00)
    S=A+B
    print(f'Sum of A and B : {S}')
    print(f'A + B :{repr(S)}') # (8.00, 10.00) Same as A.__add__(B)
    print(f'3*B : {B * 3}')  # (9.00, 12.00) Same as A.__mul__(B)
    print(f'B : {B}')      # (9.00, 12.00) Changed
    #let's create four points in the plan nd check if they shape a Parallelogram
    A = Point(5,4)
    B = Point(2, 2)
    C = Point(-1,4)
    D = Point(2,6)
    print(B.x-A.x==C.x-D.x)
    print(B.y-A.y==C.y-D.y)
    # check if ABCD is aparallelogram
    if(B.x-A.x==C.x-D.x) & (B.y-A.y==C.y-D.y):
        print('ABCD is a Parallelogram')
    else:
        print('ABCD is not Parallelogram')
