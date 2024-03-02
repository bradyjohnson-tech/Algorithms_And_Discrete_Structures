# def is_divisible_by_3(num):
#     if num < 0:
#         return False
#     elif num / 3 == 0:
#         return True
#     else:
#         return is_divisible_by_3(num - 3)
#
#
# print(is_divisible_by_3(6))


import math

log_2 = math.log(2)
log_3_over_2 = math.log(2) / math.log(3/2)

log_base_change = log_2 / log_3_over_2
print(log_base_change)
