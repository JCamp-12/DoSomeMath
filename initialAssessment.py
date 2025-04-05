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
        # print('true')
        return True
    else:
        # print('false')
        return False

check_third_solution(7)
check_third_solution(-7)


# fourth problem
# solve for x
# 3x+2=x+8
# 
# step 1 - subtract 2 from each side so 3x = x +6
# step 2 - subtract x from each side so 2x = 6
# step 3 - divide each side by 2 so x = 3

def check_fourth_solution(x):
    if 3 * x + 2 == x + 8:
        print('true')
        return True
    else:
        print('false')
        return False

check_fourth_solution(3)
check_fourth_solution(-3)


# Word problem - too EZ... just looking for max bugs left.
# She finds that each bug fix takes 15 minutes, and she’s already spent 45 minutes.
# If she wants to spend no more than 2 hours total fixing bugs today... whats the max bugs she can still fix


