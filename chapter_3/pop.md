
# LIST / ARRAY
## POP METHOD - Popping out elements from a List/Array

`.pop()` it's a method from the List/Array object, it's used to remove the last element from a list, but it also can remove specific elements from your list if you indicate an specific index/position from your list.

### SIMPLE POP, popping out the last element from your list

1. Create a list and refereces it in a variable called `motorcycles`                      
	~~~
	motorcycles = ["Honda", "Yamaha", "Suzuki"] 
	~~~
    - Now print the `motorcycles` variable that references your list/array
   		~~~
   		print(motorcycles)
   		~~~
        - Output
   			~~~
   			["Honda", "Yamaha", "Suzuki"] 
   			~~~
			
2. Use the pop method to remove last element from your list/array and keep it's returning value in a new variable called `last_element`
	~~~
	last_element = motorcycles.pop()   
	~~~
    - Now print the `last_element` variable that references the value removed from the list
    	~~~
      	print(last_element) 
      	~~~
        - Output
			~~~
			Suzuki 
			~~~

3. Print current status of your list              
	~~~
	print(motorcycles) 
	~~~
    - Output
		~~~
		["Honda", "Yamaha"] 
		~~~

### POP SPECIFIC ELEMENT, popping out a specific element from your list

1. Create a list and refereces it in a variable called `animals`                      
	~~~
	animals = ["Frog", "Cat", "Dog"] 
	~~~

      - Now print the `animals` variable that references your list/array
      	~~~
      	print(animals)
      	~~~
        - Output
			~~~
			["Frog", "Cat", "Dog"] 
			~~~
2. Use the pop method to remove last element from your list/array and keep it's returning value in a new variable called `specific_animal`
	~~~
	specific_animal = animals.pop(1)   
	~~~
	
    - Now print the `specific_animal` variable that references the value removed from the list/array
	~~~
	print(specific_animal) 
	~~~
	- Output
		~~~
		Cat 
		~~~

3. Print current status of your list/array                                                       
	~~~
	print(animals) 
	~~~
    - Output
		~~~
		["Frog", "Dog"] 
		~~~