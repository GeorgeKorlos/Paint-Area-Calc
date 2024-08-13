import math
def paint_calc(height,weight,cover):
    n_cans = (height * weight) / cover
    print(f"You will need {math.ceil(n_cans)} cans of paint")

test_h = int(input())
test_w = int(input())
coverage = 5
paint_calc(height=test_h,weight=test_w,cover=coverage)
