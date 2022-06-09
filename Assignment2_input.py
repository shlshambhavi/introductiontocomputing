#Assignment 2
#Name : Shaily Shambhavi
#SID : 21102094(CIVIL)



#question 1

#given- take input as 'Python is a case sensitive language'
#(a)
print("question 1")
string = str("Python is a case sensitive language")
print("INPUT STRING = ",string)
print("(Answer of a)")
length=len(string)
print(length)
print

#(b)
print("(Answer of b)")
reverse_string=string[length::-1]
print(reverse_string)

#(c)
print("(Answer of c)")
new_string=string[10:26]
print(new_string)

#(d)
print("(Answer of d)")
#replace 'a case sensitive' with 'oject oriented'
replaced_string=string[0:10]+'object oriented'+string[26:35]
print(replaced_string)

#(e)
print("(Answer of e)")
index_a=string.find('a')
print(index_a)

#(f) first check the index of white spaces and then write the new string by not using those index
print("(Answer of f)")
remove_whitespaces=string.replace(" ","")
print(remove_whitespaces)




#question 2
print("question 2")
name='Shaily Shambhavi'
SID=21102094
department_name="Civil"
CGPA='8.7'

print("Hey,%s Here!"%(name))
print("My SID is %d"%(SID))
print("I am from %s department and my CGPA is %s"%(department_name,CGPA))




# question 3
print("question 3")
a = 56
b = 10
#A
print("Answer of A")
print(a & b)
#B
print("Answer of B")
print(a | b)
#C
print("Answer of C")
print(a ^ b)
# D
print("Answer of D")
print(a << 2)
print(b << 2)
# E
print("Answer of E")
print(a >> 2)
print(b >> 4)




# question 4
#check whether word name is in the string given by user or not 
print("question 4")
string = str(input("Enter the string: "))
if("name" in string):
    print("Yes\n")
else:
    print("No\n")




#question 5
#to check whether the given input lengths can form a triangle or not
print("question 5")
side_1_of_triangle=int(input("Give a number:"))
side_2_of_triangle=int(input("Give a number:"))
side_3_of_triangle=int(input("Give a number:"))

if(side_1_of_triangle+side_2_of_triangle>side_3_of_triangle and side_2_of_triangle+side_3_of_triangle>side_1_of_triangle and side_1_of_triangle+side_3_of_triangle>side_2_of_triangle):
    print("The triangle is possible")
else:
    print("The triangle is not possible")




#question 6
print("question 6")
# Count number of bits to be flipped
# to convert A into B
 
# Function that count set bits
def countSetBits( n ):
    count = 0
    while n:
        count += 1
        n &= (n-1)
    return count
     
# Function that return count of
# flipped number
def FlippedCount(a , b):
 
    # Return count of set bits in
    # a XOR b
    return countSetBits(a^b)
    
a=int(input("First no:\n"))
b=int(input("second no:\n"))
print(FlippedCount(a,b))

