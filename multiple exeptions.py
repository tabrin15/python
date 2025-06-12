try:
    num1 = int(input("Enter a number:"))
    num2 = int(input("Enter a number: "))
    result = num1/num2
    print("Rsult is :",result) 
    print("Result is :",result)

except ZeroDivisionError:
    print ("Dvision by zero is not allowed")
except ValueError:
    print("Please enter numerial value")
except NameError as ex:
    print("The  exception is ", ex)

except:
    print("Some error occured")
finally:
    print("I will execute no matter what happens")