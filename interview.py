# Python Program to check Armstrong Number

# def Arm(n):
#     strg=str(n)
#     length=len(strg)
#     sum=0
#     for i in strg:
#         sum+=int(i)**length
#     if n==sum:
#         print("Arm number")
#     else:
#         print("not arm number")

# Arm(int(input("Enter the number:-")))

# Python program to print all Prime numbers in an Interval

# def prime(n):
#     list=[]
#     for i in n:
#         if i>1:
#             for j in range(2,i//2+1):
#                 if i%j==0:
#                     break
#             else:
#                 list.append(i)
#     return list

# l=[-1,-5,0,-6,4,7,-10,-11,-7,7,11,13,9,1,-17]
# print(prime(l))

# Python Program for n-th Fibonacci number

# def fibonocci(n):
#     a=0
#     b=1
#     if n<0:
#         print("Incorrect value")
#     elif n==0:
#         print(a)
#     elif n==1:
#         print(b)
#     else:
#         for i in range(2,n):
#             c=a+b
#             a=b
#             b=c
#         return c
# n=int(input("Enter number:-"))
# print(fibonocci(n))


# FibArray = [0, 1]
 
# def fibonacci(n):
#     if n<0:
#         print("Incorrect input")
#     elif n<= len(FibArray):
#         return FibArray[n-1]
#     else:
#         temp_fib = fibonacci(n-1)+fibonacci(n-2)
#         FibArray.append(temp_fib)
#         return temp_fib
#     print(FibArray)
 
# # Driver Program
 
# print(fibonacci(9))

# a,b=0,1
# n=int(input("Enter the limit:-"))
# if n<=1:
#     print("incorrect")
# print(a,b,end=' ')
# for i in range(2,n):
#     c=a+b
#     a=b
#     b=c
#     print(b,end=' ')

# Python Program for How to check if a given number is Fibonacci number?

# import math
# def isPerfectsquare(n):
#     s=int(math.sqrt(n))
#     return s*s==n

# x=int(input("Enter the number:-"))
# result1=5*x*x+4
# results2=5*x*x-4

# if isPerfectsquare(result1) or isPerfectsquare(results2):
#     print("febonacci number")
# else:
#     print('Not')

# Program to print ASCII Value of a character

# n=input("Enter the char:-")
# print(ord(n))

# Python Program for Sum of squares of first n natural numbers

# def SumOfSquare(n):
#     s=0
#     for i in range(1,n+1):
#         s+=i*i
#     print(s)

# n=int(input("Enter the number:-"))
# SumOfSquare(n)

# Python program to interchange first and last elements in a list

# l=[1,2,3,4,5,6,7]
# t=len(l)
# l[0],l[t-1]=l[t-1],l[0]
# print(l)

# Python program to find second largest number in a list

# l=[45,2,5,6,1,3,5,1,3,6,2,45,42,42]
# l.sort()
# large=l[-1]
# for i in range(-1,-1-len(l),-1):
#     if l[i]<large:
#         large=l[i]
#         break
# print(large)

# l=[45,2,5,6,1,3,5,1,3,6,2,42,42,45]
# s=set(l)
# a=s.remove(max(s))
# print(max(s))

# l=[45,2,5,6,11,3,5,1,30,60,2,55,-60]
# list=[]
# n=int(input("Enter the number:-"))
# l.sort(reverse=True)
# for i in range(n):
#     list.append(l[i])
# print(list)
# print(l)

# def func(list,n):
#     new_list=[]
#     for i in range(0,n):
#         max1=0
#         for j in range(len(list)):
#             if list[j]>max1:
#                 max1=list[j]
#         list.remove(max1)
#         new_list.append(max1)
#     print(new_list)

# list=[45,2,5,6,1,3,5,1,3,6,2]
# n=int(input("enter the number:-"))
# func(list,n)

# list=[45,2,5,60,1,3,5,1,3,6,2]
# large=list[0]
# for i in list:
#     if i>large:
#         large=i
# print(large)

# Python program to print all even numbers in a range

# def even(start,end):
#     list=[]
#     for i in range(start,end+1):
#         if i%2==0:
#             list.append(i)
#     print(list)

# a=int(input("Enter the starting number"))
# b=int(input("Enter the ending number"))
# even(a,b)

# Remove multiple elements from a list in Python

# l=[11, 5, 17, 18, 23, 50]
# del l[1:5]
# print(l)

# Python – Remove empty List from List

# test_list = [5, 6, [], 3, [], [], 9]
# l=[]
# for i in test_list:
#     if i:
#         l.append(i)
#     else:
#         pass
# print(l)

# Python | Program to print duplicates from a list of integers

# list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# l=[]
# for i in list:
#     if i not in l:
#         l.append(i)
# print(l)

# Python program to find Cumulative sum of a list

# list = [10, 20, 30, 40, 50]
# l=[]
# s=0
# for i in range(len(list)):
#     s+=list[i]
#     l.append(s)
# print(l)

# Python | Sum of number digits in List

# list=[12, 67, 98, 34]
# l=[]
# for i in list:
#     r=i%10
#     q=i//10
#     s=r+q
#     l.append(s)
# print(l)

# list=[12, 67, 98, 34,123,5]
# l=[]
# for item in list:
#     s=0
#     for digit in str(item):
#         s+=int(digit)
#     l.append(s)
# print(l)

# break the list 

# my_list = ['geeks', 'for', 'geeks', 'like',
#            'geeky','nerdy', 'geek', 'love',
#                'questions','words', 'life']
# l=[]

# for i in range(0,len(my_list),3):
#     x=i
#     a=my_list[i:i+3]
#     l.append(a)
# print(l)

# Sort the values of first list using second list in Python

# list1=['a','b','c','d','e','f','g','h','i']
# list2=[0,1,1,0,1,2,2,0,1]
# list3=[]
# l=list(set(list2))
# l.sort()
# for i in l:
#     for j in range(len(list2)):
#         if list2[j]==i:
#             list3.append(list1[j])
# print(list3)

# Remove elements larger than a specific value from a list in Python

# l=[12,54,63,23,11,322,45,2,5,7]
# list=[]
# value=int(input("Enter the number:-"))
# for i in l:
#     if i<=value:
#         list.append(i)
# print(list)

# s="Welcome to lucknow"
# vcount=0
# for i in s:
#     if i in "AEIOUaeiou":
#         vcount+=1
# print(vcount)

# l=[[1,2],[3,4]]
# import copy
# a=copy.deepcopy(l)
# print(a)

# Python program to check whether the string is Symmetrical

# s=input("Enter the string:-")
# if len(s)%2!=0:
#     print('not symetrical')
# else:
#     s1=''
#     s2=''
#     for i in range(0,len(s)//2):
#         s1+=s[i]
#     print(s1)
#     for j in range(len(s)//2,len(s)):
#         s2+=s[j]
#     print(s2)
#     if s1==s2:
#         print('symetric')
#     else:
#         print('not symetric')

# Ways to remove i’th character from string in Python      

# s= "GeeksForGeeks"
# s1=''
# n=int(input("Enter the num:-"))
# for i in range(len(s)):
#     if i==n-1:
#         continue
#     else:
#         s1+=s[i]
# print(s1)

# Python – Words Frequency in String Shorthands

# s="Welcome to the home and welcome is to ram and ram is the boy"
# d={}
# l=s.split()
# for i in l:
#     if i in d:
#         d[i.lower()]+=1
#     else:
#         d[i.lower()]=1
# print(d)

# Python – Convert Snake case to Pascal case

# s='welcome_to_home_ram'
# a=s.replace('_',' ').title().replace(' ','')
# print(a)

# Python | Count the Number of matching characters in a pair of string

# str1='abcdef'
# str2='defghia'
# t=()
# for i in str1:
#     if i in str2:
#         t+=(i,)
# print(t)

# Remove all duplicates from a given string in Python

# s="Welcome to goa"
# string=''
# for i in s:
#     if i not in string:
#         string+=i
# print(string)

# Python – Least Frequent Character in String

# s='geekofgeeks'
# for i in s:
#     if s.count(i)==1:
#         print(i)
#         break

# for max 

# s='geekofgeeks'
# d={}
# maxvalue=0
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# res=max(d,key=d.get)
# print(res)

# Python program for removing i-th character from a string

# s="Welcome to home"
# k=4
# a=s[0:4]+s[5:]
# print(a)

# Python | Check if a given string is binary string or not

# s='01010100101a'
# for i in s:
#     if i not in '01':
#         print('No')
#         break
# else:
#     print('Yes')

# Python – Replace multiple words with K

# s = 'Geeksforgeeks is best for geeks and CS'
# l= ["best", 'CS', 'for']
# r='gfg'
# list=s.split()
# list1=[]
# for i in list:
#     if i in l:
#         i=r
#     else:
#         i=i
#     print(i,end=' ')

# Python | Permutation of a given string using inbuilt function

# from itertools import permutations
# def permutation(n):
#     permlist=permutations(n)
#     for i in list(permlist):
#         print(''.join(i))

# permutation('ABC')

# d={'ram':[1,2,5,4],'abs':[2,8,74,15,3],'is':[1,4,5,8,3,9],'to':[45,2,5,7]}
# list1=[]
# for i in d.values():
#     list1.extend(i)
# l=list(set(list1))
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)

# l=[[1,2,3],[4,5,6],[7,8,9]]
# s=0
# for i in range(3):
#     for j in range(3):
#         if i==j:
#             s+=l[i][j]
# print(s)


# l=[[1,2,3],[4,5,6],[7,8,9]]
# s=0
# for i in range(3):
#     for j in range(3):
#         if j==2-i:
#             s+=l[i][j]
# print(s)

# d={'a':100,'b':200,'c':300}
# s=0
# for i in d.values():
#     s+=i
# print(s)
    
# d={'a':100,'b':200,'c':300,'d':'ram'}
# # d.pop('d')
# # print(d)
# dict1={}

# for i in d.keys():
#     if i!='d':
#         dict1[i]=d[i]
# print(dict1)


# list = [{"name": "Nandini", "age": 20},{"name": "Manjeet", "age": 20},{"name": "Nikhil", "age": 19}]
# from operator import itemgetter
# print(sorted(list,key=itemgetter('age','name')))

# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}
# dict1.update(dict2)
# print(dict1)

# d={'name':['jan','feb','march'],'month':[1,2,3]}
# dict={}
# l=list(d.values())
# a=l[0]
# b=l[1]
# for i in range(len(a)):
#     dict[b[i]]=a[i]
# print(dict)

# def primfactor(n):
#     for i in range(2,n+1):
#         for j in range(2,i//2+1):
#             if i%j==0:
#                 break
#         else:
#             if n%i==0:
#                 print(i,end=' ')

# primfactor(int(input("Enter the number:-")))

# d={'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
# dict={}
# a=sorted(d)
# for i in a:
#     dict[i]=d[i]
# # print(dict)
# b=sorted(d.values())
# for i in d:
#     dict[i]=d[i]

# print(dict)

###########################################################################################
# def decor_func(result_func):
#     def destinction(marks):
#         for m in marks:
#             if m>=75:
#                 print('distinction')
#         result_func(marks)
#     return destinction



# @decor_func
# def result(marks):
#     for m in marks:
#         if m>=33:
#             pass
#         else:
#             print("fail")
#             break
#     else:
#         print("pass")

# l=[75,45,65,35,89,59]
# result(l)

########################################################################################################

# l=[[],{},[],1,2,3,[1,2,3],"!"]
# list=[]
# for i in l:
#     if i:
#         list.append(i)
# print(list)

# def sum():
#     global s
#     a=10
#     b=20
#     s=a+b
#     print(s)

# sum()
# print(s)

# l=[1,2,3,4]
# list=l.copy()
# list[0]=12
# print(list)
# print(l)

# class Vehical:
#     def __init__(self):
#         self.speed=int(input("enter the speed"))

# class Car(Vehical):
#     def displayA(self):
#         print(self.speed)

# obj=Car()
# obj.displayA()

# class Father:
#     money=1000
#     def show(self):
#         print("parent class instance method")

#     def showmoney(self):
#         print("parent class class method",self.money)

#     def stat(self):
#         a=10
#         print("parent class static method",a)

# class Child(Father):
#     def display(self):
#         print("child class instance")

# c=Child()
# c.display()
# c.show()
# c.showmoney()
# c.stat()
















































































































        



























































































































































    























































    






























































































            





























































































