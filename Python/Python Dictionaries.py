def main():
    # Create a dictionary with some initial values
    my_dict = {
        "name": "Alice",
        "age": 30,
        "city": "New York",
        "University": "MIT",
        "cgpa": 3.8,
    }
    print("Initial dictionary:", my_dict)
    
    # Dictionary Items
    print("Dictionary items:", my_dict.items())
    
    # Dictionary Keys
    print("Dictionary keys:", my_dict.keys())
    
    # Dictionary Length
    print("Length of dictionary:", len(my_dict))
    
    # Dictionary Items - Data Types
    print("Data types of dictionary items:")
    for key, value in my_dict.items():
        print(f"Key: {key}, Value: {value}, Type of value: {type(value)}")
    
    
    # Adding a new key-value pair
    my_dict["country"] = "USA"
    print("Dictionary after adding a new key-value pair:", my_dict)
    
    # Dictionary Methods
    print("Dictionary methods:")
    print("Keys:", my_dict.keys())
    print("Values:", my_dict.values())
    print("Items:", my_dict.items())
    print("Get method (age):", my_dict.get("age"))
    print("Pop method (removing age):", my_dict.pop("age"))
    print("Dictionary after pop:", my_dict)

if name == "__main__":
    main()