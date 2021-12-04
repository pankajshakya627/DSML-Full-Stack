'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
'''
# print pattern 

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
def pattern(n):
    x = 0
    for i in range(0,n):
        x += 1
        for j in range(0, i+1):
            print(x, end=" ")
        print("\r")
        
        
pattern(5)



# pattern 02 - 
# *
# * *
# * * *
# * * * *
# * * * * *
def pattern02(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end='')
        print('\r')
    print()        
    
pattern02(5)

# check palindrome
string = input('Enter a string: ')
if string == string[::-1]:
    print('Palindrome')
else:
    print("Not a Palindrome")

# Armstrong number:
n = int(input("Enter a number: "))
s = 0
temp = n
while temp>0:
    d = temp%10
    s += d**3
    temp //= 10 
if n == s:
    print("Armstrong number")
else:
    print("Not Armstrong number")
    
''' 
# lambda function
ans = lambda a,b : a**2 + b**2 + 2*a*b
print(ans(3,3))





