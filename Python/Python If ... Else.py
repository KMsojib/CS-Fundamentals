def main():

    # Python Conditions and If statements
    """ 
    Equals: a == b
        Not Equals: a != b
        Less than: a < b
        Less than or equal to: a <= b
        Greater than: a > b
        Greater than or equal to: a >= b
    """
    
    age = 20
    if age > 18:
        print("You are eligible to vote.")
    elif age == 18:
        print("You are just eligible to vote.")
    else:
        print("You are not eligible to vote.")

    
    # Less than & Greater than
    num1 = 10
    num2 = 20
    if num1 < num2:
        print(f"{num1} is less than {num2}")
    elif num1 == num2:
        print(f"{num1} is equal to {num2}")
    else:
        print(f"{num1} is not less than {num2}")
    
    


if name == "__main__":
    main()