import sys


def solution(array,p=None,q=None):
    c = 1
    for i in array[p:q+1]:
        c*=i
    print(f'Multiplication is {1000000000}') if c>1000000000 else print(f'Multiplication is {c}')

    print(f'Array is {array}')



a = input('Enter value using a coma : ')
array = [float(i) if float(i)<10000.0 and float(i)>-10000 else sys.exit('Give value between 10000 and -10000') for i in a.split(',')]

p = int(input("Enter value of P to slice the array : "))
q = int(input("Enter value of Q to slice the array : "))

solution(array, p, q)