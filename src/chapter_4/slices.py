# Slices

## Slice from index X to length Y, [index:length]
names = ["Lucas", "Mariano", "Roberto", "Reginaldo", "Gilberto"]
print(names)
print(names[1:5])

## Slice from index X to an unknown length
integers = list(range(0, 101)) 
print(integers[90:])

## Looping through slice
for value in integers[:10]:
    print(value)

for value in integers[-11:]:
    print(value)

## Copying list through slice
colors = ["Blue", "Red", "Yellow", "Black", "Pink"]
print(colors)

colors_copy = colors[:] # Copy with slice
colors_backup = colors

colors.pop()
print(colors)
print(colors_backup)
print(colors_copy) 

# Since it's copy from the value and not from reference isn't effected by changes on the colors
