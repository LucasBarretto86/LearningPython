# Learning Python

- [Learning Python](#learning-python)
  - [Hello World](#hello-world)
  - [Math operators](#math-operators)
    - [Basic operations](#basic-operations)
      - [Sum](#sum)
      - [Subtraction](#subtraction)
      - [Multiplication](#multiplication)
      - [Division](#division)
      - [Module](#module)
      - [Power](#power)
    - [Equations](#equations)
    - [Long numbers](#long-numbers)
  - [Strings](#strings)
    - [String transformation / Cases](#string-transformation--cases)
      - [Titlecase](#titlecase)
      - [Uppercase](#uppercase)
      - [Lowercase](#lowercase)
    - [String interpolation](#string-interpolation)
    - [Adding tab to a string](#adding-tab-to-a-string)
    - [Adding line breaker to a string](#adding-line-breaker-to-a-string)
    - [Strip method](#strip-method)
      - [Right side strip method](#right-side-strip-method)
      - [Left side strip method](#left-side-strip-method)
  - [Primitive types](#primitive-types)
  - [Variables](#variables)
    - [values assignments](#values-assignments)
    - [Multiple value assignments](#multiple-value-assignments)
  - [Constants](#constants)
  - [Comments](#comments)
  - [List](#list)
    - [Accessing values](#accessing-values)
    - [Modifying values](#modifying-values)
    - [Avoiding no index due to list length](#avoiding-no-index-due-to-list-length)
    - [Appending method](#appending-method)
    - [Insert method](#insert-method)
    - [Pop method](#pop-method)
    - [Sort method - Permanently](#sort-method---permanently)
    - [Sort method - Temporarily](#sort-method---temporarily)
    - [Reverse method](#reverse-method)
    - [length method](#length-method)
    - [Removing method](#removing-method)
    - [del statement](#del-statement)
    - [Iterating through list](#iterating-through-list)
      - [Looping through list](#looping-through-list)
      - [Using range method](#using-range-method)
    - [list method to create a list using range method](#list-method-to-create-a-list-using-range-method)
    - [max method](#max-method)
    - [min method](#min-method)
    - [sum method](#sum-method)
    - [create list of squares using append method and range method](#create-list-of-squares-using-append-method-and-range-method)
    - [create list of squares using for and range method](#create-list-of-squares-using-for-and-range-method)
  - [Slices](#slices)
    - [Slice from index X to length Y, [index:length]](#slice-from-index-x-to-length-y-indexlength)
    - [Slice from index X to an unknown length](#slice-from-index-x-to-an-unknown-length)
    - [Looping through slice](#looping-through-slice)
    - [Copying list through slice](#copying-list-through-slice)
  - [Tuples, lists with immutable values](#tuples-lists-with-immutable-values)
    - [parentheses are optional](#parentheses-are-optional)
    - [Accessing tuples values](#accessing-tuples-values)
  - [Conditional operators](#conditional-operators)
    - [Equal](#equal)
    - [Difference](#difference)
    - [Greater](#greater)
    - [Lesser](#lesser)
    - [Greater or Equal](#greater-or-equal)
    - [Lesser or Equal](#lesser-or-equal)
    - [If statements](#if-statements)
      - [Ternary operator | if_test_false,if_test_true](#ternary-operator--if_test_falseif_test_true)
      - [If else in line | [on_true] if [expression] else [on_false]](#if-else-in-line--on_true-if-expression-else-on_false)
    - [if else block](#if-else-block)
    - [if else in chain](#if-else-in-chain)
    - [Compare operators](#compare-operators)
    - [and](#and)
    - [or](#or)
  - [Dictionary](#dictionary)
    - [Assign new keys and values](#assign-new-keys-and-values)
    - [Removing dictionary value](#removing-dictionary-value)
    - [Method get()](#method-get)
    - [Method items()](#method-items)
    - [Method keys()](#method-keys)
    - [Method values()](#method-values)
    - [List of Dictionary](#list-of-dictionary)
    - [List inside a Dictionary](#list-inside-a-dictionary)
    - [Dictionary inside a Dictionary](#dictionary-inside-a-dictionary)
  - [Handling user input](#handling-user-input)
    - [String input](#string-input)
    - [Multiple lines prompt input](#multiple-lines-prompt-input)
    - [Number input](#number-input)
    - [Input examples](#input-examples)
      - [modular even odd test](#modular-even-odd-test)
      - [Building dictionary using input](#building-dictionary-using-input)
  - [While loop](#while-loop)
    - [Using also input()](#using-also-input)
    - [Using flag](#using-flag)
    - [Break loop](#break-loop)
    - [between](#between)
    - [While in for lists checking conditional value](#while-in-for-lists-checking-conditional-value)
    - [while to handle dictionary](#while-to-handle-dictionary)
  - [Modules](#modules)
  - [Class](#class)
  - [Handling files](#handling-files)
  - [Snippet](#snippet)
    - [Reading files](#reading-files)

## Hello World

```py
print("Hello Python World!")
```

## Math operators

### Basic operations

| Sym | Operation      |
| :-- | :------------- |
|  +  | Sum            |
|  -  | Subtraction    |
|  *  | Multiplication |
|  /  | Division       |
|  %  | Module         |
|  ^  | Power          |

#### Sum

```py
# 2 + 2 = 4
print(2 + 2)

# Output
# 4
```

#### Subtraction

```py
# 2 - 2 = 0
print(2 - 2)

# Output
# 0
```

#### Multiplication

```py
# 2 * 2 = 4
print(2 * 2)

# Output
# 4
```

#### Division

```py
# 2 / 2 = 1
print(2 / 2)

# Output
# 1
```

#### Module

```py
# 5 % 4 = 1
print(5 % 4)

# Output
# 1
```

#### Power

```py
# 3**2 = 9
print(3**2)

# Output
# 9
```

### Equations

```py
# (3 + 5) *4 = 32
print((3  + 5)* 4)

# 3 + 5 *4 = 23
print(3 + 5* 4)
```

### Long numbers

```py
print("\nUniverse age")
print(14_000_000_000)
```

## Strings

```py
message = "Hello Python World!"
print(message)
```

### String transformation / Cases

#### Titlecase

```py
warning = "atTenTion pleAse"
print(warning.title())

# Output

# Attention Please
```

#### Uppercase

```py
warning = "atTenTion pleAse"
print(warning.upper())
# Output

# ATTENTION PLEASE
```

#### Lowercase

```py
warning = "atTenTion pleAse"
print(warning.lower())
# Output

# attention please
```

### String interpolation

```py
name = "First Name"
last_name = "Surname"
full_name = f"{last_name.upper()}, {name.title()}"
message = f"I like your {full_name}"

print(message)

# Output 

# I like your First Name Surname
```

### Adding tab to a string

```py
print("\tPython")

# Output

#    Python
```

### Adding line breaker to a string

```py
print("Language:\nPython\nC\nJavascript\n")

# Output

# Language:
# Python
# Javascript
```

### Strip method

```py
string_with_extra_space = " python "
print(string_with_extra_space.strip())

# Output

# python
```

#### Right side strip method

```py
string_with_extra_space = "    python    "
print(string_with_extra_space.rstrip())

# Output

#    python
```

#### Left side strip method

```py
string_with_extra_space = "    python    "
print(string_with_extra_space.lstrip())

# Output

# python
```

## Primitive types

| type     | Representation                |
| :------- | :---------------------------- |
| string   | "Text"                        |
| int      | 1                             |
| float    | 1.2                           |
| complex  | 2+3j                          |
| list     | [1,2,3,4]                     |
| tuple    | (1,2,3,4)                     |
| range    | range(1, 5)                   |
| dict     | {"name": "Lucas", "age": 35}  |
| bool     | False                         |
| bytes    | 100101001                     |

```py
print(type(str_variable))
print(type(int_variable))
print(type(float_variable))
print(type(complex_variable))
print(type(list_variable))
print(type(range_variable))
print(type(dict_variable))
print(type(bool_variable))
print(type(bytes_variable))

# Output

# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'complex'>
# <class 'list'>
# <class 'range'>
# <class 'dict'>
# <class 'bool'>
# <class 'int'>
```

## Variables

### values assignments

```py
#String variable
my_string = "Some sentence"
print(my_string)

#Integer variable
my_integer = 1
print(my_integer)

# Float variable
my_float = 1.2
print(my_float)

# Output

# Some sentence
# 1
# 1.2
```

### Multiple value assignments

```py
x, y, z = 1, 2, 3

print(x)
print(y)
print(z)

# Output

# 1
# 2
# 3
```

## Constants

Constants are not really constants in Py, so it's more like convention

```py
MAX_CONNECTIONS =  5000
print(MAX_CONNECTIONS)

MAX_CONNECTIONS =  1
print(MAX_CONNECTIONS)

# Output

# 5000
# 1
```

## Comments

```py
print("Comments")
print("Will print")

# print("Won't print because is commented")

# Output

# Comments
# Will print
```

## List

Basically lists are arrays on Py

```py
names = ["Lucas", "Rafael", "Daniel"]
print(names)

# Output

# ['Lucas', 'Rafael', 'Daniel']
```

### Accessing values

```py
names = ["Lucas", "Rafael", "Daniel"]
print(names[2])

# Output

# Daniel
```

### Modifying values

```py
print(names)

names[2] = "Camila"
print(names)

# Output

# names = ["Lucas", "Rafael", "Daniel"]
```

### Avoiding no index due to list length

```py
numbers = [1, 2, 3, 4, 5]
print(numbers[-1])

numbers.remove(4)
print(numbers[-1])

# Output

# 5
# 5
```

### Appending method

```py
animals = ["Dog", "Cat", "Frog"]
print(animals)

animals.append("Monkey")
print(animals)

# Output

# ['Dog', 'Cat', 'Frog']
# ['Dog', 'Cat', 'Frog', 'Monkey']
```

### Insert method

```py
letters = ["A", "C", "D"]
print(letters)

letters.insert(1, "B")
print(letters)

letters.insert(4, "E")
print(letters)

# Output

# ['A', 'C', 'D']
# ['A', 'B', 'C', 'D']
# ['A', 'B', 'C', 'D', 'E']
```

### Pop method

```py
motorcycles = ["Honda", "Yamaha", "Suzuki"]
last = motorcycles.pop()
print(last)
print(motorcycles)

# Output

# Suzuki
# ['Honda', 'Yamaha']
```

### Sort method - Permanently

```py
fruits = ["Mango", "Banana", "Orange","Grape"]
print(fruits)

fruits.sort()
print(fruits)

# Output

# ['Mango', 'Banana', 'Orange', 'Grape']
# ['Banana', 'Grape', 'Mango', 'Orange']
```

### Sort method - Temporarily

```py
veggies = ["Tomato", "Carrot", "Onion", "Broccoli"]
sorted_veggies = sorted(veggies)

print(veggies)
print(sorted_veggies)

# Output

# ['Tomato', 'Carrot', 'Onion', 'Broccoli']
# ['Broccoli', 'Carrot', 'Onion', 'Tomato']
```

### Reverse method

```py
print(sorted_veggies.reverse())
```

### length method

```py
print(len(sorted_veggies))
```

### Removing method

```py
colors = ["Red", "Gold", "Black"]
print(colors)

colors.remove("Black")
print(colors)
```

### del statement

```py
names = ["Lucas", "None", "Someone"]
print(names)

del names[2]
print(names)

name = "Lucas"
print(name)

del name
print(name)
```

### Iterating through list

#### Looping through list

```py
animals = ["Dog", "Cat", "Bat", "Horse"]

for animal in animals:
    print(animal)
```

#### Using range method

```py
for index in range(0, 4):
    print(animals[index])

```

### list method to create a list using range method

```py
numbers = list(range(1,10))
print(numbers)

```

### max method

```py
print(max(numbers))
```

### min method

```py
print(min(numbers))
```

### sum method

```py
print(sum(numbers))
```

### create list of squares using append method and range method

```py
squares = []

for value in range(1, 11):
    squares.append(value**2)
print(squares)
```

### create list of squares using for and range method

```py
squares = [value**2 for value in range(1, 11)]
print(squares)
```

## Slices

### Slice from index X to length Y, [index:length]

```py
names = ["Lucas", "Mariano", "Roberto", "Reginaldo", "Gilberto"]
print(names)
print(names[1:5])

```

### Slice from index X to an unknown length

```py
integers = list(range(0, 101))
print(integers[90:])
```

### Looping through slice

```py
for value in integers[:10]:
    print(value)

for value in integers[-11:]:
    print(value)
```

### Copying list through slice

```py
colors = ["Blue", "Red", "Yellow", "Black", "Pink"]
print(colors)

colors_copy = colors[:] # Copy with slice
colors_backup = colors

colors.pop()
print(colors)
print(colors_backup)
print(colors_copy) 
```

Since it's copy from the value and not from reference isn't effected by changes on the colors

## Tuples, lists with immutable values

```py
statuses = ("Pending", "Confirmed", "Processing", "Cancelled")
print(statuses)
```

### parentheses are optional

```py
levels = "EASY", "MEDIUM", "HARD", "HARDEST"
print(levels)
```

### Accessing tuples values

```py
print(statuses[1])
```

## Conditional operators

### Equal

```py
print( 5 == 5)
```

### Difference

```py
print( "A" != "a")
```

### Greater

```py
print( 5 > 4)
```

### Lesser

```py
print( 3 < 4)
```

### Greater or Equal

```py
print( 5 >= 4)
print( 5 >= 5)
```

### Lesser or Equal

```py
print( 3 <= 4)
print( 4 <= 4)
```

### If statements

#### Ternary operator | [if_test_false,if_test_true](test)

```py
a, b, = 10, 20
print( (b, a) [a < b] )
```

#### If else in line | [on_true] if [expression] else [on_false]

```py
name = "Lucas"

print("Yes it is" if name == 'lucas' else "No it isn't")

```

### if else block

```py
name = "Test"

if name == 'Test':
    result = "It's a test"
else:
    result = "Nothing"

print(result)
```

### if else in chain

```py
age = 12

if age < 4:
 price = 0
elif age < 18:
 price = 25
elif age < 65:
 price = 40
elif age >= 65:
 price = 20

print(price)
```

### Compare operators

### and

```py
age = 15

if age >= 12 and age < 18:
    print("Teenager")
else:
    print("Not Teenager")

age = 11
```

### or

```py
if age < 12 or age > 18:
    print("Not Teenager")
else:
    print("Teenager")
```

## Dictionary

Kinda like Hash in Ruby or event kinda of struct

```py
alien_0 = {"color": "green", "points": 5}

print(alien_0["color"])
print(alien_0["points"])
print(alien_0)
```

### Assign new keys and values

```py
alien_0["x"] = 25
alien_0["y"] = 0

print(f"Alien y = {alien_0['y']}, Alien x = {alien_0['x']}")
```

### Removing dictionary value

```py
print(alien_0)

del alien_0["color"]

print(alien_0)
```

### Method get()

```py
print(alien_0.get("color", "Value not found"))
```

### Method items()

```py
for key, value in alien_0.items():
    print(key, value)
```

### Method keys()

```py
print(alien_0.keys())
```

### Method values()

```py
print(alien_0.values())
```

### List of Dictionary

```py
players = [
    {"health": 100},
    {"health": 80},
    {"health": 50},
    {"health": 20},
]

for player in players:
    print(player["health"])
```

### List inside a Dictionary

```py
zoo = {"animals": ["Elephant", "Monkey", "Tiger", "Lion"]}

print(zoo["animals"][2])
```

### Dictionary inside a Dictionary

```py
player = {"skills": {"Strength": 10, "Charisma": 0, "Dexterity": 5, "Lucky": -5}}

print(player["skills"]["Lucky"])
```

## Handling user input

### String input

```py
name = input("Tell me what's you age my little friend: ")
print(f"Welcome {name}")
```

### Multiple lines prompt input

```py
message = f"{name} this is a very long message that we gonna use as example,\n"
message += "to allow as yo use multiple lines to do an input. What do you think?\n"
message += "Isn't that great? [Y/N]"

prompt = input(message)
print(prompt)
answer = prompt[:1][0].lower()

if(answer == "y"):
    print("I knew it, we are awesome\n\n")
elif(answer == "n"):
    print("Oh that isn't right\n\n")
else:
    print("Try again dude!\n\n")
```

### Number input

```py
sum = input("2 + 2 = ")

if(int(sum) == 4):
    print("well done!\n\n")
else:
    print("Bastard!\n\n")
```

### Input examples

#### modular even odd test

```py
num = input("Inform a number to check if it's even or odd:")

if(int(num) % 2 != 0):
    result = "odd"
else:
    result = "even"

print(f"{num} is {result}")
```

#### Building dictionary using input

Simple polling system to create a dictionary of users based in questions and responses
It will use while loop, for loop, list, dictionary, input and if statements

```py
users = []

questions = {
    "name": "What's your name?",
    "age": "How old are you?",
    "color": "What's your favorite color?"
}

polling_status_active = True

while polling_status_active:
    new_user = {}

    for attr, question in questions.items():
        answer = input(f"{question} (q = Quit)\n")

        if answer.lower() == "q" and len(answer) == 1:
            polling_status_active = False
            break
        else:
            new_user[attr] = answer
    
    if len(new_user) > 0:
        users.append(new_user)

    print(users)       
```

## While loop

```py
current_number = 1

while current_number <= 5:
    print(current_number)
    current_number += 1

```

### Using also input()

```py
message = ""

while message != "Yes, I do":
    message = input("I love you Someone! Do you love me too?\n")
    print(message)

```

### Using flag

```py
active = True

while active:
    message = input("Type 'q' to quit operation:\n")

    if(message.lower() == "q"):
        active = False
```

### Break loop

```py
while True:
    message = input("Type 'q' to quit operation:\n")

    if(message.lower() == "q"):
        break
```

### between

```py
guests = []

invitees = ["JuJu", "Dudu", "Babu", "ZonZon"]

while invitees:
    guests.append(invitees.pop())

print(guests)

```

### While in for lists checking conditional value

```py
animals = ["Dog", "Bee", "Monkey", "Bee", "Cat", "Elephant", "Bee", "Kangaroo", "Bee"]

while "Bee" in animals:
    animals.remove("Bee")

print(animals)
```

### while to handle dictionary

```py
player = {"x": 0, "y": 0}

target = 300

while target > player["x"]:
    player["x"] += 10

print(player)
```

## Modules

## Class

## Handling files

## Snippet

### Reading files

```py
BUFFER_SIZE = 1024

def download_length(response, output, length):
    times = length / BUFFER_SIZE
    if length % BUFFER_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFFER_SIZE))
        print("Download %d" % (((time * BUFFER_SIZE)/length)*100))

def download(response, output):
    total_downloaded = 0
    while True:
        data = response.read(BUFFER_SIZE)
        total_downloaded += len(data)
        if not data:
            break
        output.write(data)
        print("Downloaded {bytes}".format(bytes = total_downloaded))

import io
import sys
import urllib.request as request 
```
