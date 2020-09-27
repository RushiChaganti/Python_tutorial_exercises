# Function has a signature.

def first_function():
    print("My First Function")

# greeting is called as parameter.
def first_function_with_param(greeting):
    print(greeting)

# greeting is called as parameter.
def first_function_with_params(greeting1, greeting2):
    print(greeting1 + " " + greeting2)

def product(num1, num2):
    result = num1 * num2
    return result


# Invoking a function
first_function()
first_function_with_param("Hello World")
first_function_with_params("Jaya", "Guru Datta")
product_result = product(3,4)
print(product_result)
