# l=[[],{},[],1,2,3,[],'!']
# list=[]
# for i in l:
#     if i:
#         list.append(i)
# print(list)

# l=[[1,2,3],[4,5,6],[7,8,9]]
# s=0
# for i in range(3):
#     for j in range(3):
#         if i==j:
#             s+=l[i][j]
# print(s)


# l=[[1,2,3],[4,5,6],[6,8,9]]
# s=0
# for i in range(3):
#     for j in range(3):
#         if i+j==3-1:
#             s+=l[i][j]
# print(s)

# for i in range(1,6):
#     for j in range(1,6):
#         if j<=i:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if j>=6-i:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if j<=6-i:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# for i in range(1,5):
#     for j in range(1,8):
#         if j>=5-i and j<=3+i:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# for i in range(1,5):
#     for j in range(1,8):
#         if j>=i and j<=8-i:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# for i in range(1,5):
#     for j in range(1,8):
#         if j<=5-i or j>=3+i:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if j<=i:
#             print(j,end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if j<=6-i:
#             print(6-j,end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# l=[12,32,2,5,63,20,33,11,7,9,6,1]
# k=10
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==k:
#             print(l[i],l[j])

# s='sharavan'
# d={}
# for i in range(len(s)):
#     if s[i] not in d:
#         d[s[i]]=s.count(s[i])

# print(d)

# l=[1,2,3,5,6,2,1,4,2,6,7,7,8]
# d={}
# for i in l:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
    
# print(d)

# l=['apple','BananA','cherry','tommoto','brinZle',"mango"]
# l1=[]
# n=input('Enter the character to search:-')
# for i in l:
#     if n.lower() in i.lower():
#         l1.append(i)
# print(l1)

# s='mukesh is the chutiya'
# s1=s.split()
# l=''
# for i in s1:
#     for j in i:
#         if s.count(j)==1:
#             l+=j
# print(l)

# n=eval(input('Enter the number:-'))
# if n>0 and type(n)==int:
#     print('natural num')

# l=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# l1=[]
# a=l.index(2)
# for i in range(a,len(l)):
#     for j in range(2,abs(l[i]//2+1)):
#         if l[i]%j==0:
#             break
#     else:
#         l1.append(l[i])
# print(l1)
        
# l=[]
# for i in range(-10,11):
#     for j in range(2,i//2+2):
#         if i%j==0:
#             break
#     else:
#         l.append(i)
# print(l)

# def prime(n):
#     if n>1:
#         for i in range(2,n//2+1):
#             if n%i==0:
#                 print('Not prime')
#                 break
#         else:
#             print('Prime')
#     else:
#         print('Not prime')
# n=int(input("Enter the number:-"))
# prime(n)

# l=[1,2,5,4,2,1,63,4]
# l1=[]
# for i in l:
#     if l.count(i)>=1 and i not in l1:
#         l1.append(i)
# print(l1)


# def fact(n):
#     if n>0:
#         f=1
#         for i in range(n,1,-1):
#             f=f*i
#         return f
#     else:
#         return ('Please enter posite number')
# n=int(input("Enter the number:-"))
# print(fact(n))

# def factor(n):
#     l=[]
#     for i in range(1,n//2+1):
#         if n%i==0:
#             l.append(i)
#     return l

# n=int(input("Enter the number:-"))
# print(factor(n))

# l=[1,2,3,5,7,10,12]
# k=15
# for i in range(0,len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==k:
#             print(l[i],l[j])

# def hcf(n,m):
#     if n>m:
#         maxvalue=n
#     else:
#         maxvalue=m
#     for i in range(1,maxvalue//2+1):
#         if n%i==0 and m%i==0:
#             hcf=i
#     return hcf

# n=int(input("Enter the number1:-"))
# m=int(input("Enter the number2:-"))
# print(hcf(n,m))

# def Arm(n):
#     s=str(n)
#     t=len(s)
#     sm=0
#     for i in s:
#         sm+=int(i)**t
#     print(sm)
#     if sm==n:
#         print('Arm number')
#     else:
#         print("Not arm number")

# n=int(input("Enter the number:-"))
# Arm(n)

# def perfect(n):
#     s=0
#     for i in range(1,n//2+1):
#         if n%i==0:
#             s+=i
#     if s==n:
#         return ('Perfect number')
#     else:
#         return ('Not perfect number')

# n=int(input("Enter the number:-"))
# print(perfect(n))

# s="sharavan is very hansomefdgssfffffff aaaaaaaaaaaaaaaaaa"
# l=s.split()
# l1=[]
# for i in l:
#     l1.append(len(i))
# m=max(l1)
# for j in l:
#     if len(j)>=m:
#         print(j)

# s="sharavan is very hansomefdgssssss aaaaaaaaaaa"
# l=s.split()
# max=l[0]
# for i in range(len(l)):
#     if len(l[i])>len(max):
#         max=l[i]
# print(max)

# l=['shravan','mukesh','amit']
# for i in range(0,len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)

# l=['apple','Banan','cherry','tommoto','brinZle',"mango"]
# l1=[]
# n=input("Enter the char:-")
# for i in l:
#     if n.lower() in i.lower():
#         l1.append(i)
# print(l1)

# import random
# a=random.randint(1,100)
# a=random.randrange(1,100)
# a=random.random()
# l=[12,54,32,6,87]
# a=random.choice(l)
# random.shuffle(l)
# l=random.uniform(1,5)
# print(l)

# def square(n):
#     return n*n

# n=int(input("Enter the number:-"))
# print(square(n))

# def reverse(n):
#     rev=0
#     while n>0:
#         r=n%10
#         rev=(rev*10)+r
#         n=n//10
#     return rev

# n=int(input("Enter the number:-"))
# print(reverse(n))

# def factor(n):
#     l=[]
#     for i in range(1,n//2+1):
#         if n%i==0:
#             l.append(i)
#     return l

# n=int(input("Enter the number:-"))
# print(factor(n))

# def prime(n):
#     for i in range(2,n+1):
#         for j in range(2,i//2+1):
#             if i%j==0:
#                 break
#         else:
#             print(i,end=' ')

# n=int(input("Enter the number:-"))
# prime(n)

# with open('text.txt','r') as obj:
#     a=obj.read()
#     l=a.split()
#     print(l)

# with open('shravi.txt','w') as obj:
#     l='''welcome to india 
# my name is sharavan kushwaha
# i have complated batchelor of engineering
# for iet agra'''
#     obj.writelines(l)
#     obj.close()

# with open('text.txt','r') as obj:
#     a=obj.read()
#     ucount=lcount=dcount=splcount=0
#     for i in a:
#         if i>='A' and i<='Z':
#             ucount+=1
#         elif i>='a' and i<='z':
#             lcount+=1
#         elif i>'0'and i<='9':
#             dcount+=1
#         else:
#             splcount+=1

#     print(ucount,lcount,dcount,splcount)

#     obj.close()

# with open ('text.txt','r') as obj:
#     a=obj.readlines()
#     print('number of line =',len(a))
#     obj.seek(0)
#     data=obj.read()
#     l=data.split()
#     print(len(l))

# obj=open('text.txt','r')
# a=obj.read()
# l=a.split()
# for i in l:
#     print(i.title(),end=' ')

# class Studennt():
#     def __init__(self):
#         self.__name=''
#         self.__setname("Ravo")
#     def getname(self):
#         return self.__name
#     def __setname(self,name):
#         self.__name=name
# obj=Studennt()
# # obj.setname('Sharavan')
# a=obj.getname()
# print(a)

# class student:
    
#     def __init__(self,name,age,add):
#         self.name=name
#         self.age=age
#         self.add=add
#         self.a='Amit'
    
# obj=student('sharavan',26,'Lucknow')
# print(obj.a)

# class Vehical:
#     def displayA(self):
#         print('Hello A')
# class Car(Vehical):
#     def displayB(self):
#         print("hello B")
# class Bike(Vehical):
#     def displayC(self):
#         print('Hello C')

# obj=Car()
# obj1=Bike()
# obj.displayA()
# obj1.displayC()
# obj.displayB()

# a,b=0,1
# n=int(input("Enter the limit:-"))
# print(a,b,end=' ')
# for i in range(2,n+1):
#     c=a+b
#     print(c,end=' ')
#     a=b
#     b=c
# kkkk
# for i in range(1,11):
#     print(i*2)
    
















































































































































        



















    
            


































































































        

















































        





























































































