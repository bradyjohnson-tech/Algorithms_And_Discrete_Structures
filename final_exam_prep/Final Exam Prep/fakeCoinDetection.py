def find_fake(coins): # this is wrong
    # Base case with only one coin
    if len(coins) == 1:
        return 0

    mid = len(coins) // 2
    left = coins[:mid]
    right = coins[mid:]

    if sum(left) < sum(right):
        return find_fake(left)
    elif sum(left) > sum(right):
        return find_fake(right) + mid
    else:
        if len(coins) % 2 != 0:
            return len(coins) - 1

# Test the function
coins = [1, 1, 1, 0.9, 1, 1, 1]  # 0.9 represents the fake coin
fake_index = find_fake(coins)
print('The fake coin is at position:', fake_index + 1) #



# returns wong value
# O(log(n)) => the number of weighs needed to find the fake coin
# This problem recursive relation and stop conditions are:
# ○ T(n) = 1 + T(n/2) (worst case)
# ○ T(3) = T(2) = 1