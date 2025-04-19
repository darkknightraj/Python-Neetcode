def contain_duplicate(arr):
    hashset=set()
    for n in  arr:
        if n in hashset:
            return True
        hashset.add(n)
    return False
#arr=[2,3,4,5]
print(contain_duplicate([1,2,3,4])) # Output False
print(contain_duplicate([2,3,4,2,4,5])) #Output True



