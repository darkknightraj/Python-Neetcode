def contain_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]==arr[j]):
                return True
    return False
print(contain_duplicate([1, 2, 3, 4,4, 5])) # True 
print(contain_duplicate([1,1,2,3,3,5])) #True
print(contain_duplicate([1,2,3,4,5])) # False
