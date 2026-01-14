def my_function():
  print("Hello from a function")

# Argument function
def my_function(fname):
  print(fname + " Refsnes")

# Without argument function
def my_function(fname = "Sojib"):
  print(fname + " Refsnes")


def main():
    my_function()
    my_function("Sojib")
    my_function("Sojib", "Rafiq")
    
if __name__ == "__main__":
    main()