# def pelindrome(s):
#     s1=''
#     for i in range(-1,-1-len(s),-1):
#         s1+=s[i]
#     if s1==s:
#         print('Pelindrome')
#     else:
#         print("Not Pelindrome")

# pelindrome("malayalaM")

# from itertools import permutations
# l=[]
# def Permu(s):
#     perlist=permutations(s)
#     for i in list(perlist):
#         l.append(''.join(i))
#     print(l)

# Permu('ABCD')

# s="ABC"
# l=[]
# for i in range(0,len(s)):
#     for j in range(i+1,len(s)+1):
#         print(s[i:j+2])

# s="Welcome to home"
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

# s='Welcome tommmmmmmmmmm the lucknowss'
# l=s.split()
# large=l[0]
# # print(t)
# for i in l:
#     if len(i)>len(large):
#         large=i
# print(large)

# s1="abcd"
# s2="acdbs"
# l1=sorted(s1)
# l2=sorted(s2)
# if l1==l2:
#     print("yes")
# else:
#     print("no")

# l=[5,-1,0,1,2,3,4,5,6,7,8,9]
# list=[]
# for i in l:
#     if i>1:
#         for j in range(2,i//2+1):
#             if i%j==0:
#                 break
#         else:
#             list.append(i)

# print(list)

# def prime(n):
#     for i in range(2,n//2+1):
#         if n%i==0:
#             print('not prime')
#             break
#     else:
#         print("prime")

# n=int(input("Enter the number:-"))
# prime(n)

# l=["Mango",'banana','apple','cherry','pineapple']
# s=input("Enter the charecter:-")
# for i in l:
#     if s.lower() in i.lower():
#         print(i)

# l=[1,2,5,3,'ram','srk','amit','srk',4,20,3,1]
# list=[]
# for i in l:
#     if i not in list:
#         list.append(i)
# print(list)

# l=[1,'2',[3,'4',5,[6,7]]]
# list=[]
# l1=[]
# for i in l:
#     if type(i)==int:
#         list.append(i)
#     else:
#         list.extend(i)
# for j in list:
#     if type(j)==int:
#         l1.append(j)
#     else:
#         l1.extend(j)
# print(l1)

# l=[1,2,3,'ram',5,'shyam']
# l.remove('ram')
# print(l)

# l=[1,2,'srk','',{},[],(),{1,2},True]
# d={}
# for i in l:
#     if type(i) in d:
#         d[i]+=i
#     else:
#         d[i]=1
# print(d)

# n=input("Enter the number:-")
# if n>='1' and n<='9' and n.isdigit():
#     print("Natuaral")
# else:
#     print("No")

# l=[1,2,5,4,6,3,7,2,5,8]
# k=10
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]+l[j]==k:
#             print(l[i],l[j])

# l=[1,2,5,4,6,3,7,2,5,8]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)

# l=[1,2,3,4,5,6,7,8,9,5,6]
# list=[]
# for i in range(0,len(l),2):
#     list.append(l[i:i+2])
# print(list)

# s="welcome to home"
# l1=[]
# l=s.split()
# for i in l:
#     l1.append(i.title())
# print(l1)
# print(' '.join(l1))


# l1=['a','b','c','d','e','f','g','h','i']
# l2=[0,1,1,0,1,2,2,0,1]
# list1=[]
# a=list(set(l2))
# a.sort()
# # print(a)
# for i in a:
#     for j in range(len(l2)):
#         if l2[j]==i:
#             list1.append(l1[j])
# print(list1)


































































    





































































