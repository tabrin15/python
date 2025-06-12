try :
    num = int(input("enter your number :"))
    print(num)
except ValueError as ex:
    print("Exception:"), ex

    print("Iam outside the try block")