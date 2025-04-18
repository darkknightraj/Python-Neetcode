def contains_duplicate(arr):
    if len(arr) != len(set(arr)):
        return True
    return False
    
arr=[1,2,3,4]
print(contains_duplicate(arr)) #False

