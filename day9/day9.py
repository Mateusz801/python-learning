# Dictionaries & nesting
# Dictionary consists of "Key" and "Value"
# Creating dictionaries:
# A "key : value" pair is called "entry"
# Elements are identified by keys
# Each key can only have one value
programming_dictionary = {
    "Bug": "Errorus maximus",
    "Function": "A piece of code that you can easily call over and over again",
}

# Retrieve items from dictionaries
print(programming_dictionary["Bug"])

# Watch out for spelling keys, wrong spelling gives "KeyError"
# If keys are strings, you have to call using a string

# Adding new items to dictionary:
programming_dictionary["Loop"] = "The action of doing sth over and over again"
print(programming_dictionary)

# It is useful to create empty dictionary:
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary or add a new entry
programming_dictionary["Bug"] = "A moth in your computer"

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Nesting
# Simple dictionary:
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a Dictionary:
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting a Dictionary in a Dictionary:
expanded_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 14,
    }
}

# Nesting dictionaries in a List
expanded_log = [
    {"country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12,
     },
    {"country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": 14,
     }
]

# Ex1
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)

# Ex2
country = input()  # Add country name
visits = int(input())  # Number of visits
list_of_cities = eval(input())  # create list from formatted string

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(p_country, p_visits, p_list_of_cities):
    travel_log.append({
        "country": p_country,
        "visits": p_visits,
        "cities": p_list_of_cities
    })


# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
