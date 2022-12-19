# # # # # # # def outer():#-------------global
# # # # # # #     print("I am outer function") #--------local
# # # # # # #     def inner():
# # # # # # #         print("I am inner function")#------local
# # # # # # #     inner()

# # # # # # # outer()#---------------global

# # # # # # # def welcome():
# # # # # # #     print("Welcome everyone!")

# # # # # # # print(f"Welcome everyone!")
# # # # # # # a= welcome
# # # # # # # print(f"a:{a}")
# # # # # # # a()

# # # # # # def product(num1,num2):
# # # # # #     return num1*num2

# # # # # # p=product 
# # # # # # print(p(20,10))


# # # # # def welcome(name):
# # # # #     print(f"Wwlcome {name}!")

# # # # # def bye(name):
# # # # #     print(f"Bye bye {name}!")

# # # # # def greet_person(func):
# # # # #     func("Ram")

# # # # # greet_person(welcome)
# # # # # greet_person(bye)

# # # # def outer():
# # # #     # print("I am outer function")
# # # #     def inner():
# # # #         print("I am inner function")
# # # #     return inner
# # # # i=outer()
# # # # i()

# # # def increment(num):
# # #     def increase_by ( factor):
# # #          return num+factor 
# # #     return increase_by 

# # # inc = increment(20)
# # # print(inc(50))
# # def my_decorator(func):

# #      def wrapper():
# #         print("I called before example.")
# #         func()
# #         print("I called after example.")
# #      return wrapper

# # @my_decorator
# # def example():
# #     print("I am example")
    
# # # example()
# # def smart_division(func):
# #     def wrapper(a,b):
# #         if b == 0:
# #            return "can not divided by zero"
# #         else:
# #             return func(a,b)
# #     return wrapper

# # @smart_division        
# # def division(a ,b ):
# #     return a/b 

# # print(division(10,5))
# # print(division(10,0))

# #built-in higher order function

# #lambda x,y:x+y

# # a=lambda x,y : x+y 
# # print(a(10,12))

# #map(func, iterable_object)

# # a = [1,2,3,4,5]

# # out = map(lambda n:n+1,a)
# # print(list(out))

# #filter (func,iterable) #----bolean condition ----filtration#

# num = [1,2,3,4,5,6,7,8,9,10]

# filter(lambda n:n%2== 0,num)
# print(list(out))


# student_marks=[
#     {"name": "Ram","score":82},
#     {"name": "sita","score":80},
#      {"name": "hari","score":78},
#      {"name": "shyam","score":12},
#      {"name": "bharat","score":98},
#      {"name": "gopal","score":78},

 

# ]

# student_marks=filter(lambda i:i.get("score")>=40,student_marks)

# print(list(student_marks))


main =[]
even = []
odd = []
duplicate = []

#take user input 15 times in int 
# append all user input in main list
# append even number in even list 
# append odd number in odd list 
# append duplicate entry duplicate list 

main = []

for i in range(5):
    main.append(input('Enter your inputs: '))
    if  i in main:
        duplicate.append(i)
    else:
        if i%2 == 0:
            even.append(i)
        else:
                odd.append(i)
    main.append(i)

print(main)
print(even)
print(odd)
print(duplicate)

     



# for i in main :
#     if i%2 == 0 :
#        even.append(i)

#     print(" even number is: ",even)

# print(even)








