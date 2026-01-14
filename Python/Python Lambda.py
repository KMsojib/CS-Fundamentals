def main():
    x = lambda a : a + 10
    print(x(5))
    
    x = lambda a, b : a * b
    print(x(5, 6))

if __name__ == "__main__":
    main()