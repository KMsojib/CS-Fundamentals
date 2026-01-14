def main():
    list = ["apple", "banana", "cherry"]

    list = ["apple", "banana", "cherry"]
    print(list)
    
    mylist = ['apple', 'banana', 'cherry']
    print(mylist[1])
    
    list1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
    for x in list1:
        print(x)
        
    
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = []

    for x in fruits:
        if "a" in x:
            newlist.append(x)
    print(newlist)
    
    # List Comprehension
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = [x for x in fruits if "a" in x]
    print(newlist)
    
    # List Comprehension with range
    newlist = [x for x in range(10)]
    print(newlist)
    # List Comprehension with range and condition
    newlist = [x for x in range(10) if x < 5]
    print(newlist)
    
    
    # List Comprehension with function
    def myfunc(x):
        return x.upper()
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = [myfunc(x) for x in fruits]
    print(newlist)
    
    # List Comprehension with function and condition
    def myfunc(x):
        return x.upper()
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = [myfunc(x) for x in fruits if "a" in x]
    print(newlist)
    
    # List Comprehension with function and condition
    def myfunc(x):
        return x.upper()
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = [myfunc(x) for x in fruits if "a" in x]
    print(newlist)
    
    # Sort List Alphanumerically
    fruits = ["banana", "Orange", "Kiwi", "cherry"]
    fruits.sort()
    print(fruits)
    
    # Sort List Alphanumerically, Case Insensitive
    fruits = ["banana", "Orange", "Kiwi", "cherry"]
    fruits.sort(key=str.lower)
    print(fruits)
    
    # Sort List Descending
    fruits = ["banana", "Orange", "Kiwi", "cherry"]
    fruits.sort(reverse=True)
    print(fruits)
    
    # Sort List Descending, Case Insensitive
    
    fruits = ["banana", "Orange", "Kiwi", "cherry"]
    fruits.sort(reverse=True, key=str.lower)
    print(fruits)
    
    thislist = [100, 50, 65, 82, 23]
    thislist.sort(reverse = True)
    print(thislist)
    
    
    # Customize Sort Function
    def myfunc(e):
        return abs(e - 50)
    thislist = [100, 50, 65, 82, 23]
    thislist.sort(key=myfunc)
    print(thislist)
    
    # Copy List
    thislist = ["apple", "banana", "cherry"]
    mylist = thislist.copy()
    print(mylist)
    
    # Join Two Lists
    
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]
    list3 = list1 + list2
    print(list3)
    
    # Join Two Lists with append
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]
    for x in list2:
        list1.append(x)
        
    print(list1)
    
    # Join Two Lists with extend
    
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]
    list1.extend(list2)
    print(list1)
    # List Methods
    thislist = ["apple", "banana", "cherry"]
    thislist.append("orange")
    print(thislist)
    
    thislist = ["apple", "banana", "cherry"]
    thislist.insert(1, "orange")
    print(thislist)
    
    thislist = ["apple", "banana", "cherry"]
    thislist.remove("banana")
    print(thislist) 
    
    thislist = ["apple", "banana", "cherry"]
    thislist.pop(1)
    print(thislist)
    
    thislist = ["apple", "banana", "cherry"]
    thislist.pop()
    print(thislist)
    
    
    # List Methodss
    thislist = ["apple", "banana", "cherry"]
    thislist.clear()
    print(thislist)
    
    thislist = ["apple", "banana", "cherry"]
    thislist.reverse()
    print(thislist)
    
    thislist = ["apple", "banana", "cherry"]
    thislist.sort()
    print(thislist)
    
    thislist = ["apple", "banana", "cherry"]
    thislist.sort(reverse=True)
    print(thislist)
    
    thislist = ["apple", "banana", "cherry"]
    thislist.sort(key=str.lower)
    print(thislist)
    
    
    thislist = ["apple", "banana", "cherry"]
    thislist.sort(key=str.lower, reverse=True)
    print(thislist)
    
    thislist = ["apple", "banana", "cherry"]
    thislist.sort(key=str.lower, reverse=True)
    print(thislist)
    
    thislist = ["apple", "banana", "cherry"]
    thislist.sort(key=str.lower, reverse=True)
    print(thislist)
    
    thislist = ["apple", "banana", "cherry"]
    coutn = thislist.count("apple")
    print(coutn)
    
    
    
if __name__ == "__main__":
    main()