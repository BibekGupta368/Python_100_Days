# #1st process : Highly complicated
# with open("Day 25\weather_data .csv") as weather_data:
#     data = weather_data.readlines()
#     print(data) 



# #2nd process : importing csv : Complicated with the larger amount of data
# import csv
# with open("Day 25\weather_data .csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperature =[]
#     print(data)
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#         print(row)
#     print(temperature)   



# #3rd process : importing pandas: Most easyiest way
# import pandas
# data = pandas.read_csv("Day 25\weather_data .csv")
# print(data)
# print(data["temp"]) 



# #Data Frames: topic 1 : Convert the data to dictionary
# import pandas
# data = pandas.read_csv("Day 25\weather_data .csv")
# print(data)
# data_dict = data.to_dict()     #Convert the data to dictionary
# print(data_dict)




# #Data Frames: topic 2 : Convert the data to list
# import pandas
# data = pandas.read_csv("Day 25\weather_data .csv")
# print(data)
# temp_list = data["temp"].to_list()     #Convert the data to list
# print(temp_list)
# print(len(temp_list))




# #Data Frames: topic 3 : Calculating the  average temperature
# import pandas
# data = pandas.read_csv("Day 25\weather_data .csv")
# print(data)

# """
# #1st method
# temp_list = data["temp"].to_list()     #Convert the data to list
# sum = 0
# for temp in temp_list:
#     sum += temp
# avg = sum / len(temp_list)
# print(avg)

# """

# """----------------------or---------------------------------"""

# """
# #2nd method
# temp_list = data["temp"].to_list()  
# avg = sum(temp_list) / len(temp_list)
# print(avg)

# """

# """----------------------or----------------------------------"""

# """
# #3rd method
# avg = data["temp"].mean()
# print(avg)

# """




# #Data Frames: topic 4 : Calculating the  maxm temperature
# import pandas
# data = pandas.read_csv("Day 25\weather_data .csv")
# print(data)
# maximum = data["temp"].max()
# print(maximum)




# #Data Frames: topic 5: Get data in columns
# import pandas
# data = pandas.read_csv("Day 25\weather_data .csv")
# print(data)
# print("\n")
# print(data["day"])        # or print(data.day)
# print(data["temp"])       # or print(data.temp)
# print(data["condition"])  # or print(data.condition)




# #Data Frames: topic 6: Get data in rows
# import pandas
# data = pandas.read_csv("Day 25\weather_data .csv")
# print(data)
# print("\n")
# print(data[data["day"] == "Monday"])       # or print(data[data.day == "Monday"])
# print(data[data["temp"] == 21])            # or print(data[data.temp == 21])
# print(data[data["condition"] == "Sunny"])  # or print(data[data.condition == "Sunny"])




# #Data Frames: topic 7: Row of data with the maximum temperature
# import pandas
# data = pandas.read_csv("Day 25\weather_data .csv")
# print(data)
# print("\n")
# print(data[data["temp"] == data["temp"].max()])   # or print(data[data.temp == data.temp.max()])




# #Data Frames: topic 8
# import pandas
# data = pandas.read_csv("Day 25\weather_data .csv")
# print(data)
# print("\n")
# monday = data[data["day"] == "Monday"]       # or monday = data[data.day == "Monday"]
# print(monday["condition"])                   # or print(monday.condition) 

 

# #Data Frames: topic 9: Converting the temperature to Fahrenheit
# import pandas
# data = pandas.read_csv("Day 25\weather_data .csv")
# print(data)
# print("\n")
# monday = data[data["day"] == "Monday"]       # or monday = data[data.day == "Monday"]
# monday_temp = monday["temp"]                 # or monday_temp = monday.temp
# monday_temp_f = (monday_temp* 9/5) + 32
# print(monday_temp_f)




# #Data Frames: topic 10: Converting the temperature to Fahrenheit another process
# import pandas
# data = pandas.read_csv("Day 25\weather_data .csv")
# print(data)
# print("\n")
# monday = data[data["day"] == "Monday"]       
# monday_temp = monday.temp[0]               
# monday_temp_f = (monday_temp* 9/5) + 32
# print(monday_temp_f)




# #Data Frames: topic 11: Creating the dataframe from stratch
# import pandas
# data_dict = {
#     "students" : ["Bibek", "Abhay", "Shubham"],
#     "scores" :[96, 87, 84]
# }
# dataframe = pandas.DataFrame(data_dict)   #Convert the dictionary into the Table
# print(dataframe)
# dataframe.to_csv("Day 25\\new_data .csv")    #data.to_csv("Day 25/new_data .csv")  #Push the data to the new_data.csv by automatically creating it inside the Day 25
# for (key,value) in dataframe.items():
#     print(key)
#     print(value)
#     print("\n")
# # for (index,row) in dataframe.iterrows():
# #     print(index)
# #     print(row)
# #     print("\n")






# #Data Frames : topic 12 : Counting the number of each Fur Color in 2018_Central_Park_Squirrel_Census.csv and then pushing it to a new csv ie squirrel_count.csv created automatically
# import pandas
# data = pandas.read_csv("Day 25/2018_Central_Park_Squirrel_Census.csv")

# grey_squirrels = data[data["Primary Fur Color"]== "Gray"]
# grey_squirrels_count = len(data[data["Primary Fur Color"]== "Gray"])

# red_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

# black_squirrels = data[data["Primary Fur Color"] == "Black"]
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

# print(grey_squirrels)
# print(red_squirrels)
# print(black_squirrels)
# print("\n")

# print(grey_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)

# data_dict = {
#     "Fur color" : ["grey", "red", "black"],
#     "count" :[grey_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
# dataframe = pandas.DataFrame(data_dict)   #Convert the dictionary into the Table
# dataframe.to_csv("Day 25\\squirrel_count .csv")    #data.to_csv("Day 25/squirrel_count .csv")  #Push the data to the new_data.csv by automatically creating it inside the Day 25



