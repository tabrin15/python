def factorial(x):
    '''this is a recursive function to find the factorial of an integer'''
    

    
   if   x==0 or x==1:
   return 1

   else:
   return x*factorial(x-1)


print(factorial._doc_)
print("the factorial of 0:", factorial(0))
print("the factorial of 1:", factorial(1))
print("the factorial of 2:", factorial(2))
print("the factorial of 3:", factorial(3))
print("the factorial of 4:", factorial(4))
print("the factorial of 5:", factorial(5))
print("the factorial of 6:", factorial(6))


