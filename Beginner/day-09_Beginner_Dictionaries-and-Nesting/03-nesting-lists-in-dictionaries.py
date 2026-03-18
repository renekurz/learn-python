capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary
travel_log_nested_list = {
    "France": [
        "Paris",
        "Lille",
        "Dijon"
    ],
    "Germany": [
        "Stuttgart",
        "Berlin"
    ],
}

# Print Lille
print(travel_log_nested_list["France"][1])

# Nested Dictionary
travel_log_nested_dictionary = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "num_times_visited": 8,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "num_times_visited": 5,
    },
}

# Print Stuttgart
print(travel_log_nested_dictionary["Germany"]["cities_visited"][2])