#########Swap two numbers without using third variable
a=int(input())
b=int(input())
a,b=b,a
print(a)
print(b)
OUTPUT:
2
4
4
2
###MODEL-2
a=int(input())
b=int(input())
a=a+b
b=a-b
a=a-b
print(a)
print(b)
OUTPUT:
4
5
5
4
###MODEL-3:
a=int(input())
b=int(input())
a=a^b
b=a^b
a=a^b
print(a)
print(b)
OUTPUT:
2
3
3
2
###USING MATCH#####

a=int(input())
b=int(input())
n=int(input())
match n:
    case 1:
        print(a+b)
    case 2:
        print(a-b)
    case 3:
        print(a/b)
    case 4:
        print(a%b)
    case 5:
        print(a*b)
    case 6:
        print(a//b)
    case 7:
        print("EXIT")
OUTPUT:
1
1
7
EXIT
###### COMBINING TWO STRINGS
a=input()
match a:
    case "hello":
        print("Hello All")
    case "Bye":
        print("Bye All")
    case other:
        print("Invalid Input")
 OUTPUT:
hello
Hello All
                                 LIST-[] IN PYTHON

1.#######Write a program to get n number of values in separate line for set and print the values with space separation.###
#Enter your code
a={}
c=[]
n=int(input())
for i in range(0,n,+1):
    b=int(input())
    c.append(b)
a=set(c)
print(a)
##Sample Input:##
5
3
1
4
5
2

##Sample Output:##
1 2 3 4 5 

2.####Write a program to create a list and display it.####
#code:
a=[]
n=int(input())
for i in range(0,n,+1):
    b=int(input())
    a.append(b)
for i in (a):
    if i==n:
        print(i)
    else:
        print(i,end=" ")
Sample Input:
4 
1
2
3
4

Output:
1 2 3 4
3.###Write a Python Program to find the largest number in a list####
#code:
a=[]
n=int(input())
for i in range(0,n,+1):
    b=int(input())
    a.append(b)
for i in a:
    print(max(a))
Sample Input:
5
1
2
3
6
5

Sample Output:
6
                       TUPLE IN PYTHON

1.####Write a program to get the tuple elements and print it.###
#code:
a=()
e=[]
n=int(input())
for i in range(0,n,+1):
    b=int(input())
    e.append(b)
a=tuple((e))
print((a))
Sample Input:
3
20
10
30

Sample Output:
(20, 10, 30)

2.####Write a program to get the tuple elements in a single line separated by spaces and print the number of elements in the given tuple.###
#code:
b=()
a=[int(a) for a in input().split()]
b=tuple(a)
print(len(b))
Sample Input:
10 20 30

Sample Output:
3

3.####Write a program to get the tuple values in a single line separated by space and count the nuber of times the given x value is present in the given tuple.###
#code:
a=()
n=[int(n) for n in input().split()]
d=int(input())
a=tuple(n)
for i in a:
    x=a.count(d)
    print(x)
Sample Input:
1 2 3 1 2 3 4 1 2 1
1

Sample Output:
4


