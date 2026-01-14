def main():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)

    # Looping through a string
    for ch in "apple":
        print(ch)
    
    # Break statement
    target = 10
    for x in range(20):
        if x == target:
            print("Found the target!")
            break
    else:
        print("Target not found.")
    
    # Range function
    for x in range(5):
        print(x)
    
if __name__ == "__main__":
    main()