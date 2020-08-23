is_male = True
is_tall = True

if is_male and is_tall:
    print("you are a tall male")
elif is_male or is_tall:
    print("you are a male or tall or both")
elif not is_male and is_tall:
    print("you are a tall not male")
else:
    print("you neither mall nor tall")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(30, 4, 5))
