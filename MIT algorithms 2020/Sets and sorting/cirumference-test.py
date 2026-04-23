import math

a = float(input())
b = int(input())

def circumference(a,b):
    assert type(a) and type(b) in [int,float]
    circ = (2 * a )// b
    print(circ)


if __name__ == '__main__':
    
    z = circumference(a,b)
    