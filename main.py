# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))
#
# dat_dict = data.to_dict()
# print(dat_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# # average = sum(temp_list) / len(temp_list)
# # print(average)
#
# print(data["temp"].mean() ) # this method calculate the average number from given numbers
# print(data["temp"].max())  #this method finds the max value

# print(data["condition"])
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

data_dict = {
             "Students" : ["Behruz" , "Bekzod" , "Humayun"] ,
             "Score": [80 , 78 , 95]
             }
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")



























