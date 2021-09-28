def binary_search(list1, x):  
    low = 0  
    high = len(list1) - 1  
    mid = 0  
    while low <= high:  
        mid = (high + low) // 2  
        if list1[mid] < x:  
            low = mid + 1  
        elif list1[mid] > x:  
            high = mid - 1  
        else:  
            return mid  
  
        
    return -1  
  
   
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
print (list1)
x = 21
print ("This the number to search for is ", x)
 
result = binary_search(list1, x)  
  
if result != -1:  
    print("value is present at index", str(result))  
else:  
    print("Element is not present in list1")  
