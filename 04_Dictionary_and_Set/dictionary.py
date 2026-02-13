dict = {
    "name": "junaid",
    "ph" : "03043082188",
    "lang": ["pyhton", "dart", "C", "C++", "Java"],
    "skills" : ("Flutter", "web", "AI/ML",),
    "info": { # Nesting dictionary
        "fathername": "Aanayatulla",
        "City": "Okara",
        "Brothers": 5
    }
}

print(type(dict))
print(dict["name"], dict["info"]["City"])

# Methods of dictionary
# 01 is keys
print(dict.keys()) # This method return all the keys of dict

# 02 is values
print(dict.values()) # This method return all the values of dict

# 03 is items
print(dict.items()) # This method return all keys and values of dict

# 04 is get
print(dict.get("name")) # Return the key according to value

# 05 is update
updateVal = print(dict.update({"name": "chohan"}))
print(updateVal)