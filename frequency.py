mydictionary = {

    'name': 'Tabrin', 
    'Codingal' : 2, 
    'is' : 2, 
    'best' : 2, 
    'for' : 2, 
    'Coding' : 1
}

print()


print(mydictionary['name'])  
print()

print(mydictionary)
print()

print(len(mydictionary))
print()

value = 2
result = 0


for key in mydictionary:
    
    if mydictionary[key] == 2:
        result = result + 1  
      

print("Frequency of 2 is : " + str(result))

