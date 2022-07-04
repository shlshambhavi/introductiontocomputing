#name- shaily shambhavi
#sid- 21102094
#branch- civil


#QUESTION1

def perfect_number(num_1):           #defining a function for perfect number
    if num_1>0:                      #condition for positive number
        i=1
        sum=0
        while i<=num_1:
            if num_1%i==0:           #loop for sum of all divisors
                sum=sum+i
            i=i+1
    if sum/2==num_1:                            #condition for perfect number
        print( num_1,"is a perfect number")        
    else:
        print(num_1,"is not a perfect number")
a=int(input("Enter your number"))    #input your number
perfect_number(a)                    #calling a function

#QUESTION2

def palindrome(str_1):               #defining function for palindrome
    s_1=""
    for i in str_1:                  #Using for loop to access elements of string
        s_1=i+s_1 

    print(s_1)                       #printing reversed string

strng=input("Enter your string")     #input of string

palindrome(strng)                    #calling function

if strng==palindrome(strng):
    print(palindrome(strng),"is a palindrome")    #printing palindrome
else:
    print("not palindrome")                       #printing not palindrome

#QUESTION3
from math import factorial                        #importing factorial function from maths module

def pascal_traingle(n):                           #defining function for printing pascal traingle
    i=0
    while i<n:                                    #intializing while loop
        k=n-i
        j=0
        while j<k:
            print(end=" ")                        #loop for spacing
            j=j+1
        j=0
        while j<=i:
            k=factorial(i)//(factorial(j)*(factorial(i-j)))    #writing expression for elements of pascal traingle
            print(k,end=" ")
            j=j+1
        print()                                   #print for breaking line
        i=i+1

n= int(input("enter number of rows"))             #input number of rows
pascal_traingle(n)                                #calling pascal traingle function

#QUESTION4
def pangram(str_1):
    str_2=str_1.lower()
    for i in str_2:
        for j in range(97,122):
            if i==chr(j):
                print(str_1,"is a pangram")
            
               

strng=input("Enter your string for checking pangram")
pangram(strng)

#Question 5
#Hyphen Seperated Sentence


input_string=str(input("Enter a hyphen separated sentence: "))

li=input_string.split("-") #Splitting the string into a list of strings
li.sort() #Sorting the list using sort function

print("-".join(li))
print()


#Question 6
#Student Data

def student_data(student_id,**kwargs):
    print("Student ID=",student_id)
    if "student_name" in kwargs:
        print("Student Name=",kwargs["student_name"])
    if "student_class" in kwargs:
        print("Student Class=",kwargs["student_class"])

student_data(student_id="21102038")
student_data(student_id="21102038",student_name="Raghav Goel")
student_data(student_id="21102038",student_name="Raghva Goel",student_class="1st Year")
print()


#Question 7

class Student:
    pass 
class Marks:
    pass 
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))
print()

#Question 8
#Print all triplets within an array whose sum is zero


#Question 8
#Print all triplets within an array whose sum is zero

def findTriplets(arr, n):

	found = False
	for i in range(0, n-2):
	
		for j in range(i+1, n-1):
		
			for k in range(j+1, n):
			
				if (arr[i] + arr[j] + arr[k] == 0):
					print(arr[i], arr[j], arr[k])
					found = True
	
			
# If no triplet with 0 sum found in array
	if (found == False):
		print("No triplets exist")
lst = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
	ele = int(input())
	lst.append(ele) 
print(findTriplets(lst,n))

#Question 9
#Parantheses 

class parantheses:
    def find(str):
        a= ['()', '{}', '[]'] 
        while any(i in str for i in a):
            for j in a:
                str = str.replace(j, '') 
        return not str 

s = input("Enter the sequence of parantheses : ")
if parantheses.find(s):
    print(s,"-","is balanced")
else:
    print(s,"-","is unbalanced")#QUESTION1

def perfect_number(num_1):           #defining a function for perfect number
    if num_1>0:                      #condition for positive number
        i=1
        sum=0
        while i<=num_1:
            if num_1%i==0:           #loop for sum of all divisors
                sum=sum+i
            i=i+1
    if sum/2==num_1:                            #condition for perfect number
        print( num_1,"is a perfect number")        
    else:
        print(num_1,"is not a perfect number")
a=int(input("Enter your number"))    #input your number
perfect_number(a)                    #calling a function

#QUESTION2

def palindrome(str_1):               #defining function for palindrome
    s_1=""
    for i in str_1:                  #Using for loop to access elements of string
        s_1=i+s_1 

    print(s_1)                       #printing reversed string

strng=input("Enter your string")     #input of string

palindrome(strng)                    #calling function

if strng==palindrome(strng):
    print(palindrome(strng),"is a palindrome")    #printing palindrome
else:
    print("not palindrome")                       #printing not palindrome

#QUESTION3
from math import factorial                        #importing factorial function from maths module

def pascal_traingle(n):                           #defining function for printing pascal traingle
    i=0
    while i<n:                                    #intializing while loop
        k=n-i
        j=0
        while j<k:
            print(end=" ")                        #loop for spacing
            j=j+1
        j=0
        while j<=i:
            k=factorial(i)//(factorial(j)*(factorial(i-j)))    #writing expression for elements of pascal traingle
            print(k,end=" ")
            j=j+1
        print()                                   #print for breaking line
        i=i+1

n= int(input("enter number of rows"))             #input number of rows
pascal_traingle(n)                                #calling pascal traingle function

#QUESTION4
def pangram(str_1):
    str_2=str_1.lower()
    for i in str_2:
        for j in range(97,122):
            if i==chr(j):
                print(str_1,"is a pangram")
            
               

strng=input("Enter your string for checking pangram")
pangram(strng)

#Question 5
#Hyphen Seperated Sentence


input_string=str(input("Enter a hyphen separated sentence: "))

li=input_string.split("-") #Splitting the string into a list of strings
li.sort() #Sorting the list using sort function

print("-".join(li))
print()


#Question 6
#Student Data

def student_data(student_id,**kwargs):
    print("Student ID=",student_id)
    if "student_name" in kwargs:
        print("Student Name=",kwargs["student_name"])
    if "student_class" in kwargs:
        print("Student Class=",kwargs["student_class"])

student_data(student_id="21102107")
student_data(student_id="21102107",student_name="Vansh Singh")
student_data(student_id="21102107",student_name="Vansh Singh",student_class="1st Year")
print()


#Question 7

class Student:
    pass 
class Marks:
    pass 
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks)) 
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))
print()

#Question 8
#Print all triplets within an array whose sum is zero


#Question 8
#Print all triplets within an array whose sum is zero

def findTriplets(arr, n):

	found = False
	for i in range(0, n-2):
	
		for j in range(i+1, n-1):
		
			for k in range(j+1, n):
			
				if (arr[i] + arr[j] + arr[k] == 0):
					print(arr[i], arr[j], arr[k])
					found = True
	
			
# If no triplet with 0 sum found in array
	if (found == False):
		print("No triplets exist")
lst = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
	ele = int(input())
	lst.append(ele) 
print(findTriplets(lst,n))

#Question 9
#Parantheses 

class parantheses:
    def find(str):
        a= ['()', '{}', '[]'] 
        while any(i in str for i in a):
            for j in a:
                str = str.replace(j, '') 
        return not str 

s = input("Enter the sequence of parantheses : ")
if parantheses.find(s):
    print(s,"-","is balanced")
else:
    print(s,"-","is unbalanced")