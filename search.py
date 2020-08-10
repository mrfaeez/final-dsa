def Search(array, lower, higher, x): 
    if higher >= lower: 
  
        center = (higher + lower) // 2
  
        if array[center] == x: 
            return center 
  
        elif arr[center] > x: 
            return Search(array, lower, center - 1, x) 
  
        else: 
            return Search(array, center + 1, higher, x) 
  
    else: 
        return -1
  

arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  

result = Search(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index", str(result)) 
else: 
    print("Element is not present in array") 
