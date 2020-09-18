def message(my_dict):
    try:
        return "In {movie}, {name} is a {role}.".format(**my_dict)
    except:
        pass


input_dict = {
    "name": "Chubacca",
    "role": "smuggler",
    "movie": "Star Wars"
}
print(message(input_dict))

def message(my_dict):
    key_list = ["name", "role", "movie"]
    for key in key_list:
        if key not in my_dict:
            return None
    base = "In {}, {} is a {}.".format(my_dict["movie"], my_dict["name"], my_dict["role"])
    return base