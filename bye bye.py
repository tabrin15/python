valid = False
while not False:

   
try:

number = int(input("Enter a number:"))
while number%2 ==0:
    print("bye")
  valid = True
    


except ValueError:
    print("Invalid")