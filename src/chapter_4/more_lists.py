# Iterateing through lists

## For Loop, Iteration
animals = ["Dog", "Cat", "Bat", "Horse"]

for animal in animals:
    print(animal)


## Iteration based in range method
for index in range(0, 4):
    print(animals[index])


## list method to create a list using range method 
numbers = list(range(1,10))
print(numbers)

## max method
print(max(numbers))

## min method
print(min(numbers))

## sum method
print(sum(numbers))

## create list of squares using append method and range method
squares = []

for value in range(1, 11):
    squares.append(value**2)
print(squares)

## create list of squares using for and range method
squares = [value**2 for value in range(1, 11)]
print(squares)
