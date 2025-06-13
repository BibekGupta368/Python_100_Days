# #By closing the file at the end
# file = open("D:\Python 100 Days\Day 24\Day 24.1\my_file.txt")   # Copy Using Path location ie Absolute Path
# contents = file.read()
# print(contents)
# file.close()  #Inorder to free up the resources that computer has take while executing the above commands



# #Without closing the file at the end
# with open("Day 24\Day 24.1\my_file.txt") as file:    #Copy Using Relative Path location
#     contents = file.read()
#     print(contents)



# #Appending
# with open("D:\Python 100 Days\Day 24\Day 24.1\my_file.txt",mode = "a") as file:
#     file.write("\nBye")
  


# #Writing
# with open("D:\Python 100 Days\Day 24\Day 24.1\my_file.txt",mode = "w") as file:
#     file.write("Bye")
  


# #Reading(By default given) :It gives the error as we push the text only in the writable and appendable format
# with open("D:\Python 100 Days\Day 24\Day 24.1\my_file.txt",mode = "r") as file:  # or with open("D:\Python 100 Days\Day 24\my_file.txt") as file:
#     file.write("Bye")
  


# #Automatically inserting the file that doesn't exists before in appendable format
# with open("D:\Python 100 Days\Day 24\Day 24.1\_file.txt",mode = "a") as file:
#     file.write("Bye")



# #Automatically inserting the file that doesn't exists before in writable format
# with open("D:\Python 100 Days\Day 24\Day 24.1\_file.txt",mode = "w") as file:
#     file.write("Bye")



# #Relative File Path example:
# with open("new_file.txt") as file:    #Cpoy Using Relative Path location
#     contents = file.read()
#     print(contents)
