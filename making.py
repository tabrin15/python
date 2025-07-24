class Car:

    def __init__(self):
        print('Car created')

    def __del__(self):
        print("Destructer called")

def Created_obj():
    print('Making object...')
    obj = Car()
    print('Function end..')
    return obj 
print()

print('Calling created_obj() function')
obj = Created_obj()
print('Program End...')