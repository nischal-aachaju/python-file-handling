
try :
    num=int(input("Enter number: "))
    print(1/num)

except  ZeroDivisionError:
    print("You cant divided by Zero")
except ValueError:
    print("Pleae input number")
finally:
    print("Calculation accomplished")
    