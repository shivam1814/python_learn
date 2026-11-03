# youtube video :- https://youtu.be/q3AuP01daL4?si=PSJ4FDh7gmLmpa8T


# print("hello world","shivam here")
# print("hello" + "world")

# name = "shivam"
# age = 25
# print(name,age)
# name = "ajay"
# age = 15
# isStudent = True
# print(name,age)
# print(type(name))
# print(type(isStudent))

# input / output
# name = input("enter name: ")
# print("hello :",name)

# type conversion & type casting
# age = input("enter age : ")
# new_age = int(age) + 1 # this is type casting
# print(new_age)

# a = int(input("enter number 1:"))
# b = int(input("enter number 2:"))
# print("sum is :",a+b)

# name ="Shivam"
# print(name.upper())
# print(name)
# replace
# print(name.find("i"))
# print(name.replace("v","b"))
# check for presence
# print('S' in name)

# print(2+3)
# print(2-3)
# print(2*3)
# print(2/3)
# print(2//3)
# print(5%3)
# print(5**3)

# operator precendence
# ans = 2+5*3
# print(ans)
# ans = (2+5)*3
# print(ans)

# comparison
# print(2 > 5)
# print(2 >= 5)
# print(2 < 5)
# print(2 <= 5)
# print(2 == 5)
# print(2 != 5)
# print(2 == 5)

# stt1 = 3 > 5
# stt2 = 3 > 2
# print(stt1 or stt2)
# print(stt1 and stt2)
# print(not stt2)

# if-else
# age = int(input("enter age : "))
# if age >= 18:
#     print("you are eligible")
# else:
#     print("you are not eligible")


# a = float(input("enter number 1 : "))
# b = float(input("enter number 2 : "))
# op = input("Enter operator (+,-,*,/,%,**) : ")

# if op == '+':
#     print(a+b)
# elif op == '-':
#     print(a-b)
# elif op == '*':
#     print(a*b)
# elif op == '/':
#     print(a/b)
# elif op == '%':
#     print(a%b)
# elif op == '**':
#     print(a**b)
# else:
#     print("invalid operator")

# print(range(5)) # 0 1 2 3 4
#1 to 5
# range(1,6)

# range(startValue ,  endValue, stepValue)
# range(start=1,stop=5,step=1)

#################### IMP ####################
#############################################
#############################################
# print(3 * "$") # <---- this means $ will print 3 times
#################### IMP ####################
#############################################
#############################################


# loops
# counter = 1
# print("counter initial")
# while counter <= 5:
#     print("coutner - ",counter)
#     counter +=1
# print("counter stops")


# i = 1
# while i <= 5:
#     print(i * "*")
#     i += 1

# 0 to 4
# for i in range(5):
#     print(i)

# for i in range(2,11):
#     if i%2 == 0:
#         print(i)


# for i in range(2,11,2):
#     print(i)


# multiple of 3 to 21 [1 to 50]
# for i in range(1,51):
#     if(i == 21):
#         break
#     if(i % 3 == 0):
#         print(i)

# print("loop break")

# print odd no from 1 to 20
# for i in range(1,21):
#     if i%2 != 0:
#         print(i)

# print table of 57
# for i in range(1,11):
#     print(i*57)


# list
# marks = [1,2,3,4,'A',10.5]
# print(marks , type(marks), len(marks))
# # index
# print(marks[2])
# print(marks[-1]) # last index
# print(marks[-2]) # second last index

# print(marks[0:3]) # [0:3] -> 0 is included and 3 is excluded
# print(marks[-3:-1])
# print(marks[-3:]) # [-3:] -> 3rd last element se last element tak
# print(marks[:]) # full list print

# for score in marks:
#     print(score) 
# print("------")

# marks.append(10)
# for score in marks:
#     print(score)
# print("------")

# marks.insert(0,'ABC')
# for score in marks:
#     print(score)
# print("------")

# marks.clear()
# print(marks,len(marks))


# tuple - immutable
# marks = (90,91,92,93,94,95,95)
# print(marks,type(marks))
# print(marks[2])
# print(marks.count(95))
# print(marks.index(95))


# set - unique items collections
# marks = {98,97,95,96,95,96}
# print(len(marks),marks)
# for mark in marks:
#     print(mark)


# dictionary -> key => value
# marks = {"maths":99,"physics":97,"maths":789}
# print(marks,type(marks))
# print(marks["maths"])
# print(marks["physics"])

# marks["english"] = "33"
# print(marks)

# for key in marks:
#     print(key,marks[key])



# function
# def sum(a,b):
#     print(a+b)

# sum(10,20)

# def calculate_gst(price):
#     newPrice = price + (price*0.18)
#     return newPrice

# print(calculate_gst(100))

# from math import sqrt
# import random

# # print(dir(math))
# print(sqrt(16))

# print(random.random()) # 0 to 1
# print(random.randint(10,20)) # from a to b , a & b included


# excercise -> guessing game
# import random

# def play_game():
#     lucky_num = random.randint(1,50)

#     while True:
#         user_num = int(input("Please enter num : "))
#         if user_num == lucky_num:
#             print("you won!! Game over")
#             break
#         elif user_num < lucky_num:
#             print("too low")
#         else:
#             print("too high")

#     print("Thanks for playing")


# play_game()


