def spy_game(nums):
    found_0 = False
    found_0_0 = False
    found_0_0_7 = False
    
    for num in nums:
        if num == 7 and found_0 and found_0_0:
            return True
        elif num == 0:
            if not found_0:
                found_0 = True
            elif found_0 and not found_0_0:
                found_0_0 = True
        else:
            found_0 = False
            found_0_0 = False
    return False
numbers = list(map(int, input().split()))

print( spy_game(numbers))
