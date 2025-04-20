def twoSum(arr,target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i]+arr[j]==target):
                return i,j
    return -1

arr=[3,3]
target =9
print(twoSum(arr,target))
