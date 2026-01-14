def main():
    # Casting
    x = 1  # int
    y = 2.8  # float
    z = 1j  # complex

    # Convert to int
    a = int(x)
    print(a, type(a))

    # Convert to float
    b = float(x)
    print(b, type(b))

    # Convert to complex
    c = complex(x)
    print(c, type(c))

    # Convert to string
    d = str(x)
    print(d, type(d))

if __name__ == "__main__":
    main()