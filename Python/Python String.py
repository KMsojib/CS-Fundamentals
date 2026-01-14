def main():   
    print("This is a string")
    
    # Assigning a string to a variable
    a = "Hello"
    print(a)
    
    # Multiline Strings
    a = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""
    print(a)
    
    # String are array
    a = "Hello, World!"
    print(a[1])
    
    # Looping through a string
    for x in "banana":
        print(x)
        
    # String Length
    a = "Hello, World!"
    print(len(a))
    
    # Check String
    a = "Hello, World!"
    if "H" in a:
        print("Yes, 'H' is present.")
        
    # String Slicing
    a = "Hello, World!"
    print(a[2:5])
    
    # String Methods
    a = "Hello, World!"
    print(a.lower())
    print(a.upper())
    print(a.strip()) # removes whitespace from the beginning and the end
    print(a.replace("H", "J"))
    print(a.split(",")) # returns a list
    
    # String Concatenation
    a = "Hello"
    b = "World"
    c = a + " " + b
    print(c)
    
    # String Formatting
    age = 36
    txt = "My name is John, and I am {}"
    print(txt.format(age))
    
    # Escape Characters
    txt = "We are the so-called \"Vikings\" from the north."
    print(txt)
    
    # String Methods
    a = "Hello, World!"
    print(a.capitalize())
    print(a.casefold())
    print(a.center(20))
    print(a.count("l"))
    print(a.endswith("!"))
    print(a.find("World"))
    print(a.index("World"))
    print(a.isalnum())
    print(a.isalpha())
    print(a.isdigit())
    print(a.islower())
    print(a.isupper())
    print(a.join("Hello"))
    print(a.lstrip())
    print(a.rstrip())
    print(a.splitlines())
    print(a.swapcase())
    print(a.title())
    print(a.zfill(20))
    
    # String Comparison
    a = "Hello"
    b = "Hello"
    if a == b:
        print("Both strings are equal")
    else:
        print("Both strings are not equal")
    
if __name__ == "__main__":
    main()