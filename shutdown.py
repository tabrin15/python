def shutdown(input):
    if input == "Yes":
     print("sutting down...")
     

    elif input == "No":
       print("Abort shut down...")

    else:
       print("Invalid input")

input = input("Please enter what you want to do")

shutdown(input)