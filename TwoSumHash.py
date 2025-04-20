def TwoSum(arr,target):
    previousMap={} #map value:index
    for i , n in enumerate(arr):
        diff = target-n
        if diff in previousMap:
            return [previousMap[diff],i]
        previousMap[n]=i
    return [-1,-1]
    
arr=[2,8,11,15]
target =19
print(TwoSum(arr,target))
