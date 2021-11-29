# Functions
def say_hello():
    print("Hello!")


say_hello()


# Parameters / Arguments
def say_hello_to(someone):
    print(f"Hello, {someone}!")


say_hello_to("XiaoJiao")


# Return simple value
def sum(x, y):
    result = x + y
    return result


print(sum(2, 2))


# Default Parameters / Arguments
def smile(smilling=True):
    if smilling:
        print("You are happy")
    else:
        print("You are sad")


smile()
smile(False)


# Join list values with filter to remove None values
def full_name(name, last_name, middle_name=None):
    params = [name, middle_name, last_name]

    return " ".join(filter(lambda element: element != None, params))


print(full_name("Lucas", "Silva"))
print(full_name("Lucas", "Silva", "Barretto e"))


# Named parameters
def set_user_name(first_name="", middle_name="", last_name=""):
    params = [first_name, middle_name, last_name]

    return " ".join(filter(lambda element: len(element) > 1, params))


print(set_user_name(first_name="Jorge"))
print(set_user_name(middle_name="Ben"))
print(set_user_name(last_name="Jor"))
print(set_user_name("Jorge", "Ben", "Jor"))
print(set_user_name("Jorge", "Ben"))
print(set_user_name("Jorge", "", "Jor"))

