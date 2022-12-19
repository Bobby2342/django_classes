
# # # def my_function(fname):
# # #     print(fname +" khanal")
    
# # # my_function("Bobby")
# # # my_function("Sandy")
# # # my_function("Kumar")


# # # def func_name():

# # #     print()

# # # func_name()


# # #func_name() => funtion execution 
# # #func_name => call by reference 



# # def profile(name, contact, address): 
# #                #----parameters----#
# #     print(f"Name: {name}")
# #     print(f"Contact: {contact}")
# #     print(f"Address: {address}")

# # #positional arguments
# # profile("ram", "ktm" , "987890",) 
# #         #------arguments-------#

# # #-----------------------------keyword arguments-----------------#
# # profile(name="ram",address="ktm", contact="987890")
# # #--------------------------------------------------------------#

# # #---------default arguments-------------------------------#
# # def exponent (base , power=1):
# #     print(base**power)

# # exponent(5)
# #  #-------------------------------------------------------#         

# # #-----------function without return type or with return type----#

# # def addition(num1,num2):
# #     print(num1+num2)

# # def product (num1,num2):
# #     return(num1*num2)

# # res = addition (10,12)
# # print(f'Addition:{res}')
# # ans= product(10,12)
# # print(f"Product:{ans}")

# # def example(**a):
# #     for i in a:
# #         print(i)
# # example(1,2,3,4,5)

# # def example_two(**b):
# #     print(b)

# # example_two(name="Ram",contact="1234",address="Ktm")

# def profile(name, contact, address):  
#                #----parameters----#
#     print(f"Name: {name}")
#     print(f"Contact: {contact}")
#     print(f"Address: {address}")
# a={"name":"Ram","contact":"1234","address":"Ktm"}
# profile(**a)


