# #Topic 1
# def format_name(f_name,l_name):
#     name1 = f_name.title()
#     name2 = l_name.title()
#     print(name1)
#     print(name2)
#     print(f"{name1}{name2}")
# format_name("bibek ","GUPTA") 

# #Topic 2
# def format_name(f_name,l_name):
#     name1 = f_name.title()
#     name2 = l_name.title()
#     return f"{name1}{name2}"
# formated_string = format_name("bibek ","GUPTA") # or print(format_name("bibek ","GUPTA"))
# print(formated_string)

# #Topic 3
# def function_1(text):
#     return text + text

# def function_2(text):
#     return text.title()

# output1 = function_1("hello")
# print(output1)

# output2 = function_2(output1)  # or output2 = function_2(function_1("hello"))
# print(output2)

# #Topic 4 : Multiple return values
# def format_name(f_name,l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide the valid inputs"
#     else:
#         name1 = f_name.title()
#         name2 = l_name.title()
#         return f"Result:{name1} {name2}"
# f_name = input("What is your first name: ") #string type
# l_name = input("What is your last name: ")  #string type
# formated_string = format_name(f_name,l_name) 
# print(formated_string)

#Topic 5
def my_function(a):
    if a < 40:
        return
        print("Terrible")   #This line never got printed because of return in the upper line
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))