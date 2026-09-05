# 7. WAP todemonstrate woking with dictionaries in Python.
details = {                         # creating a dictionary
    "name" : "Bruce Wayne",
    "age" : 35,
    "city" : "Gotham",
    "occupation" : "Businessman"
}
print("Original dictionary:", details)
print("Length of original dictionary:", len(details))    # length of the dictionary
print("Keys in the dictionary:", details.keys())          # keys of the dictionary
print("Values in the dictionary:", details.values())      # values of the dictionary
print("Items in the dictionary:", details.items())        # items of the dictionary
print("Accessing value for key 'name':", details["name"]) # Accessing value for a specific key
details["age"] = 36                                        # Updating value for a specific key
print("Updated dictionary:", details)
details["superhero"] = "Batman"                            # Adding a new key-value pair
print("Dictionary after adding new key-value pair:", details)
details.update({"occupation": "Philanthropist"})    # Updating value for a specific key using update() method
print("Dictionary after updating 'occupation' key:", details)
print("Is 'city' key present in the dictionary?", "city" in details)  # Checking if a key is present
details.pop("occupation")                          # Removing a key-value pair using pop() method
print("Dictionary after removing 'occupation' key:", details)
details.setdefault("hobby", "Martial Arts")   # Adding a new key-value pair using setdefault() method
new_details = details.copy()                                        # Copying the dictionary
print("Copied dictionary:", new_details)
del details["city"]                                        # Deleting a key-value pair
print("Dictionary after deleting 'city' key:", details)