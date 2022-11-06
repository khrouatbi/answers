def max_area(array: list):
    """
    :type array: list 
    :rtype: bool
    """
    #define a left and a right pointer
    l = 0
    r = len(array) -1
    area = 0
     
    while l < r:
        min_area= min(array[l], array[r]) * (r - l)
        area = max(area, min_area)
     
        if array[l] < array[r]:
            l += 1
        else:
            r -= 1

    return area
 

#test cases
a = [1,1]
b= [1, 1, 1]
c = [1,8,6,2,5,4,8,3,7]

print(max_area(a))
print(max_area(b))
print(max_area(c))