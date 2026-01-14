"""
Python divides the operators in the following groups:

- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators

Python Arithmetic Operators
Arithmetic operators are used with numeric values to perform common mathematical operations:

Operator	Name	        Example	
+	        Addition	    x + y	
-	        Subtraction	    x - y	
*	        Multiplication	x * y	
/	        Division	    x / y	
%	        Modulus	        x % y	
**	        Exponentiation	x ** y	
//	        Floor division	x // y	



Python Assignment Operators
Assignment operators are used to assign values to variables:

Operator	Example	        Same As	
=	        x = 5	        x = 5	
+=	        x += 3	        x = x + 3	
-=	        x -= 3	        x = x - 3	
*=	        x *= 3	        x = x * 3	
/=	        x /= 3	        x = x / 3	
%=	        x %= 3	        x = x % 3	
//=	        x //= 3	        x = x // 3	
**=	        x **= 3	        x = x ** 3	
&=	        x &= 3	        x = x & 3	
|=	        x |= 3	        x = x | 3	
^=	        x ^= 3	        x = x ^ 3	
>>=	        x >>= 3	        x = x >> 3	
<<=	        x <<= 3	        x = x << 3	
:=	        print(x := 3)	x = 3 print(x)

Python Comparison Operators
Comparison operators are used to compare two values:

Operator	Name	                    Example	
==	        Equal	                    x == y	
!=	        Not equal	                x != y	
>	        Greater than	            x > y	
<	        Less than	                x < y	
>=	        Greater than or equal to	x >= y	
<=	        Less than or equal to	    x <= y


Python Logical Operators
Logical operators are used to combine conditional statements:

Operator	    Description	                                            Example	
and 	        Returns True if both statements are true	            x < 5 and  x < 10	
or	            Returns True if one of the statements is true	        x < 5 or x < 4	
not	            Reverse the result, returns False if the result is true	not(x < 5 and x < 10)


"""
def main():
    # Arithmetic Operators
    a = 10
    b = 20
    print("Addition:", a + b)  # Output: 30
    print("Subtraction:", a - b)  # Output: -10
    print("Multiplication:", a * b)  # Output: 200
    print("Division:", a / b)  # Output: 0.5
    print("Modulus:", a % b)  # Output: 10
    print("Exponentiation:", a ** b)  # Output: 100
    
    # Comparison Operators
    print("Equal:", a == b)  # Output: False
    print("Not Equal:", a != b)  # Output: True
    print("Greater than:", a > b)  # Output: False
    print("Less than:", a < b)  # Output: True
    print("Greater than or equal to:", a >= b)  # Output: False
    print("Less than or equal to:", a <= b)  # Output: True
    # Logical Operators
    print("Logical AND:", a > 5 and b < 30)  # Output: True
    print("Logical OR:", a > 15 or b < 30)  # Output: True
    print("Logical NOT:", not(a > 5))  # Output: False
    # Bitwise Operators
    print("Bitwise AND:", a & b)  # Output: 0
    print("Bitwise OR:", a | b)  # Output: 30
    print("Bitwise XOR:", a ^ b)  # Output: 30
    print("Bitwise NOT:", ~a)  # Output: -11
    print("Left Shift:", a << 1)  # Output: 20
    print("Right Shift:", a >> 1)  # Output: 5
    
    # Assignment Operators
    c = 10
    c += 5  # c = c + 5
    print("Addition Assignment:", c)  # Output: 15
    c -= 5  # c = c - 5
    print("Subtraction Assignment:", c)  # Output: 10
    c *= 2  # c = c * 2
    print("Multiplication Assignment:", c)  # Output: 20
    c /= 2  # c = c / 2
    print("Division Assignment:", c)  # Output: 10.0
    c %= 3  # c = c % 3
    print("Modulus Assignment:", c)  # Output: 1.0
    c **= 2  # c = c ** 2
    print("Exponentiation Assignment:", c)  # Output: 1.0
    c //= 2  # c = c // 2
    print("Floor Division Assignment:", c)  # Output: 0.0
    
    # Identity Operators
    
    x = [1, 2, 3]
    y = x
    z = [1, 2, 3]
    print("Identity (is):", x is y)  # Output: True
    print("Identity (is not):", x is not z)  # Output: True
    # Membership Operators
    lst = [1, 2, 3, 4, 5]
    print("Membership (in):", 3 in lst)  # Output: True
    print("Membership (not in):", 6 not in lst)  # Output: True
    # Ternary Operator
    a = 5
    b = 10
    max_value = a if a > b else b
    print("Ternary Operator (max):", max_value)  # Output: 10
    # Lambda Function
    square = lambda x: x ** 2
    print("Lambda Function (square):", square(5))  # Output: 25
    # List Comprehension
    squares = [x ** 2 for x in range(10)]
    print("List Comprehension (squares):", squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    # Dictionary Comprehension
    squares_dict = {x: x ** 2 for x in range(5)}
    print("Dictionary Comprehension (squares):", squares_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    # Set Comprehension
    squares_set = {x ** 2 for x in range(5)}
    print("Set Comprehension (squares):", squares_set)  # Output: {0, 1, 4, 9, 16}
    # Generator Expression
    squares_gen = (x ** 2 for x in range(5))
    print("Generator Expression (squares):", list(squares_gen))  # Output: [0, 1, 4, 9, 16]
    # Map Function
    map_squares = map(lambda x: x ** 2, range(5))
    print("Map Function (squares):", list(map_squares))  # Output: [0, 1, 4, 9, 16]
    # Filter Function
    filter_even = filter(lambda x: x % 2 == 0, range(10))
    print("Filter Function (even):", list(filter_even))  # Output: [0, 2, 4, 6, 8]

if __name__ == "__main__":
    main()