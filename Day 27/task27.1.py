# #Topic : 1st
# def foo(a, b=4, c=6): 
#     print(a, b, c)
# foo(1)



# #Topic : 2nd
# def foo(a, b=4, c=6): 
#     print(a, b, c)
# foo(4, 9)



# #Topic : 3rd
# def foo(a, b=4, c=6): 
#     print(a, b, c) 
# foo(1, 7, 9)



# #Topic : 4th
# def foo(a, b=4, c=6):
#     print(a, b, c)
# foo(20, c=6)



# #Topic : 5th
# def add(*args):
#     print(args)
#     print(type(args))
#     sum = 0
#     for n in args:
#         sum += n
#     return sum

# result = add(1,2,3,4,5,6)
# print(result)




# #Topic : 6th
# def calculate(**kwargs):
#     print(kwargs)
#     print(type(kwargs)) 
#     for (key,value) in kwargs.items():  #or for key,value in kwargs.items():
#         print(key)
#         print(value)
# calculate(add = 3, multiply = 5)



# #Topic : 7th
# def calculate(n,**kwargs):
#     print(kwargs)
#     print(type(kwargs)) 
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
# calculate(2,add = 3, multiply = 5)




# #Topic : 8
# def bar(spam, eggs, toast='yes please!', ham=0):
#     print(spam, eggs, toast, ham)
 
# bar(1, 2)




# #Topic : 9
# def bar(spam, eggs, toast='yes please!', ham=0):
#     print(spam, eggs, toast, ham)
 
# bar(toast='nah', spam=4, eggs=2)



# #Topic : 10
# def all_aboard(a, *args, **kw): 
#     print(a, args, kw)
 
# all_aboard(4, 7, 3, 0, x=10, y=64)