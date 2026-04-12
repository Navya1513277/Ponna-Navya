try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
# except ValueError:
#     print("Error: Invalid input! Please enter a number.")
# except Exception as e:
#     print("An unexpected error occurred:", e)
# else:
#     print("No errors occurred.")
finally:
    print("Execution completed.")


# # zero division error :
# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("You cannot divide by zero!")    

# value error:
# try:
#     num = int(input("Enter a number: "))
# except ValueError:
#     print("Invalid input! Please enter an integer.")    


# Multiple exception:
# try:
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     result = num1 / num2
# except (ValueError, ZeroDivisionError) as e:
#     print("Error:", e)    

# finally keyword:
# try:
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter another number: "))
#     result = num1 / num2
# except (ValueError, ZeroDivisionError) as e:
#     print("Error:", e)