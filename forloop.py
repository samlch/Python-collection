# 1# list1=[2,3,4,5]

# for i in list1:
#     print(i)

# names=['sandhya','divya','suvarnalata']

# 2# for name in names:
#     print(name)

# lis2=['python is very easy language']

# for i in lis2:
#     print(i)

# 3

# list3=[2,3,4,5,6]
# name =[i*4 for i in list3]
# print(name)

# 4 square pattern

# n=5

# for i in range(n): -- rows
#     for j in range(n): -- columns
#      print('$',end=' ')
#     print()


# 5 left increasing pattern:
    
# n=5

# for i in range(n):
#     for j in range(i+1):
#         print('*',end=' ') 
#     print()  
    

# n=5

# for i in range(n):
#     for j in range(i,n):
#         print('*',end=' ') 
#     print()  

# n1=[]

# for x in range(1500,2701):
#     if (x % 7==0) and (x ^ 5==0):
#         n1.append(str(x))
#     print(','.join(n1))    
    
    

# n=5

# for i in range(n):
#     for j in range(i+1):
#         print('*',end=' ') 
#     print()  
# for i in range(n,0,-1):
#     for j in range(i-1):
#         print('*',end=' ') 
#     print()  

# user=input("enter the word:")
# for char in range(len(user) -1,-1,-1):
#     print(user[char],end='')

# numbers =(1,2,3,4,5,6,7,8,9)

# count_odd=0
# count_even=0

# for x in numbers:
#      if x%2==0:
#         count_even +=1
#      else:
#          count_odd +=1
# print("Number of even number is:",count_even)  
# print("Number of odd number is:",count_odd)        
         

# datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

# for item in datalist:
#     print("Type of", item, "is", type(item))


# for x in range(6):         ---query
#     if (x==3 or x==6):
#         continue
#     print(x,end=' ')
# print("\n")    

#fibonnaci series.

# x,y =0,1
# while y<50:
#     print(y)
#     x,y=y, x+y  

# fizzbuzz

# for fizzbuzz in range(51):
#     if fizzbuzz % 3==0 and fizzbuzz % 5 ==0:
#         print("Fizzbuzz")
#     elif fizzbuzz % 3 ==0:
#         print("fizz")
#         continue
#     elif fizzbuzz % 5 ==0:
#         print("buzz")
#         continue
#     print("Fizzbuzz")

#month

# months =['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

# months =input("enter the name of month:")

# if months =="february":
#     print("No of days is: 28/29 days")
# elif months in ("April", "June", "September", "November"):
#     print("No of days is: 30 days")
# elif months in ("January", "March", "May", "July", "August", "October", "December"):
#     print("No. of days: 31 days")
# else:
#     print("wrong month name")    
    

#integer

def sum (x,y):
    sum =x+y
    if sum in range (15,20):
       return 20:
    else:
        return sum
print(10,6)    
    