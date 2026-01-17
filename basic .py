# msg = "hello all"
# print(msg[::-1])

# # greet = "welcome to oist"
# # print(greet.upper())

# # print(greet.lower())
# # print(greet.title())

# age="67"
# print(age.isdigit())

# # list__

# marks=[45,78,98,34,22]
# print(marks[::4])
# marks.append(93)
# marks.append(54)
# #marks.append(67)
# marks.pop()
# print(marks)




# point= [23,13,24]
# x, y, z = point
# print(x,y,z)




# marks=[45,67,87,12,10]
# marks.insert(45,12)
# print(marks)


# # marks=[12,33,14,16,45]
# marks.remove(12)
# marks.sort(reverse=False)
# print(marks)


# data= [21,23,56,[34,25,66,36],76]
# print(data[3][2])


# msg=input("enter your message")
# revMsg = msg[::-1]
# if msg == revMsg:
#     print("true")
# else:
#     print(False)    




name=input("enter your name")
age=int(input("age bata"))

if age>=18 and name=="dhruv":
    print("welcome dhruv")
elif age==18 and name!="dhruv":
        print("no entry")
        name=input("enter your name again")

else:
    print("no entry")    

