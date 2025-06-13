#Topic1
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
print(capitals)
print(capitals["France"])
print(travel_log)
print(travel_log["France"])
print(travel_log["France"][1])

# Topic2 : List inside List
nested_list = ["A", "B",["C", "D"]]
print(nested_list[2])
print(nested_list[2][1])

# Topic3 : Dictionary inside Dictionary
travel_log = {
    "France":{
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12 
    },
    "Germany":{
        "cities_visited":["Berlin", "Hamburg", "Stuttgart",],
        "total_visits": 12 
    },
}
print(travel_log)
print(travel_log["Germany"])
print(travel_log["Germany"]["cities_visited"][2])




# bid = {
#     "Bibek": 98
# }
# print(bid["Bibek"])
