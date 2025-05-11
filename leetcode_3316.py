def closest(x,y,z):
    if abs(z-y) >abs(z-x):
        return  1
    elif abs(z-y) == abs(z-x):
        return 0
    else:
        return 2

x = 2  # indicate person 1
y=5 # indicate person 2
z=6 #indicate person 3 which will not move 
result = closest(x,y,z)
print(result)

