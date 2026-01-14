 # Python Data Types
# Python has various built-in data types that can be categorized into several groups.
# Here are the main categories of data types in Python:
"""
1. Text Type:	str
2. Numeric Types:	int, float, complex
3. Sequence Types:	list, tuple, range
4. Mapping Type:	dict
5. Set Types:	set, frozenset
6. Boolean Type:	bool
7. Binary Types:	bytes, bytearray, memoryview
8. None Type:	NoneType

"""



def main():
    
    print("Python Data Types\n")
    print("======================== 1. Text Type: str =========================")
    text = "Hello, World!"  
    print(f"Text Type (str): {text}\n")

    print("======================== 2. Numeric Types: int, float, complex ========================")
    integer_num = 42  
    float_num = 3.14 
    complex_num = 1 + 2j 
    print(f"Numeric Types - int: {integer_num}, float: {float_num}, complex: {complex_num}\n")
    
    print("======================== 3. Sequence Types: list, tuple, range ========================")
    sample_list = [1, 2, 3]
    sample_tuple = (4, 5, 6)
    sample_range = range(7, 10)
    print(f"Sequence Types - list: {sample_list}, tuple: {sample_tuple}, range: {list(sample_range)}\n")

    print(" ======================== 4. Mapping Type: dict ========================")
    sample_dict = {"name": "Alice", "age": 25}
    print(f"Mapping Type (dict): {sample_dict}\n")
    
    print("======================== 5. Set Types: set, frozenset ========================")
    sample_set = {1, 2, 3}
    sample_frozenset = frozenset([4, 5, 6])
    print(f"Set Types - set: {sample_set}, frozenset: {sample_frozenset}\n")
    
    print("======================== 6. Boolean Type: bool ========================")
    sample_bool = True
    print(f"Boolean Type (bool): {sample_bool}\n")
    
    print("======================== 7. Binary Types: bytes, bytearray, memoryview ========================")
    sample_bytes = b"hello" 
    sample_bytearray = bytearray(5)
    sample_memoryview = memoryview(bytes(5))
    print(f"Binary Types - bytes: {sample_bytes}, bytearray: {sample_bytearray}, memoryview: {sample_memoryview.tolist()}\n")
    
    print("8. None Type: NoneType\n")
    sample_none = None
    print(f"None Type (NoneType): {sample_none}\n")

if __name__ == "__main__":
    main()