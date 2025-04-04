# first question
# 1. Solve the equation x + 3 = 7
# x+3=7⇒x=4

def check_solution(x):
    if x + 3 == 7:
        # print('true')
        return True

check_solution(4)


# second Question
# 2. solve the equation 2x - 5 = 9
# 
# step 1 - add the 5 to both sides so 2x = 14
# step 2 - divide each side by 2 so x = 7

def check_second_solution(x):
    if 2 * x - 5 == 9:
        # print('true')
        return True
    else:
        # print('false')
        return False

check_second_solution(7)


# third question
# solve for x
# x^2 == 49
# 
# step 1 - square each side so x =7

def check_third_solution(x):
    if x**2 == 49:
        print('true')
        return True
    else:
        print('false')
        return False

check_third_solution(7)
check_third_solution(-7)