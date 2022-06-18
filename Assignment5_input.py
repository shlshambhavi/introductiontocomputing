#QUESTION1

string_1=input("Enter string to be reversed")   #Enter your string to be reversed
string_2=""                                     #Empty string

for i in string_1:
    string_2=i+string_2                         #Using loop reversing string 
print(string_2)

#QUESTION2

low_lmt = int(input("Enter your lower limit"))                     #Lower limit in range
upp_lmt = int(input("Enter your upper limit"))                     #Upper limit in range
num = int(input("enter your number"))                              #Number for divisibility
list_1 =[]
for i in range(low_lmt,upp_lmt+1):
    if i%num==0:                                                   #Loop for finding number with which it is divisble
        list_1.append(i)
print("Numbers with which given range is divisible are",list_1)

#QUESTION3
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)(s-b)(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)


#QUESTION4

for i in range(5):
    for j in range(i+1):
        print('*',end="")                                       #loop for upper lower traingle
    print()
for i in range(4):
    for j in range(4-i):
        print('*',end="")                                       #Loop for lower lower traingle
    print()

#QUESTION 5

rows=int(input("Enter the no of rows: ")) #No of rows is taken as input from the user
m=65 #ASCII code of A is 65
for i in range(rows):
    for j in range(i+1):
        if m>90:
            m=65
        print(chr(m),end='')
        m+=1 
    print()
print()

#Question 6
#To print prime numbers in given range

#We take range of numbers as input from the user
x1,x2=input("Enter the range of numbers: ").split()
x1=int(x1)
x2=int(x2)
for i in range(x1,x2,1):
    c=0
    n=1
    while n<=i:
        if i%n==0:
            c+=1
            n+=1
            continue
        n=n+1        
    if c==2:
        print(i)
print()

#Question 7
#To print numbers that are multiple of 7 and divisible by 11 in the range 1-500
for i in range(1,500):
    if i%7==0 and i%11==0:
        print(i)
print()

#Question 8

list=[] #we take an empty list to store the integer values input by the user
for i in range(0,10,1):
    n=int(input(f"Enter {i+1} number: "))
    list.append(n)
print(list)

#a)
print("Positive numbers are: ")
for i in range(10):
    if list[i]>0:
        print(list[i])

#b)
print("Negative numbers are: ")
for i in range(10):
    if list[i]<0:
        print(list[i])

#c)
print("Odd numbers are: ")
for i in range(10):
    if list[i]%2!=0:
        print(list[i])

#d)
print("Even numbers are: ")
for i in range(10):
    if list[i]%2==0:
        print(list[i])

#e)
count=dict()
for no in list:
    if no in count:
        count[no]+=1
    else:
        count[no]=1

print("No of times each number occurs in the List:")
print(count)
print()


#Question 9
#Count the number of occurrence of each word in the list input by the user

str=input("Enter a string: ")
#Empty dictionary is created to 
counts = dict()
#We split the input string into words and store it in in a list
words = str.split(' ')
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)