import unittest
tc = unittest.TestCase()
# For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one partition may be [9, 3, 5, 10, 10, 12, 14]

# def pivotArray(arr, pivot):
#     l = 0
#     r = len(arr) - 1
#     while l < r :
#         if arr[l] > pivot:
#             arr.append(arr[l])
#             arr.pop(l)
#             r -= 1
#         else: l+=1
#         if arr[r] > pivot:
#             print("in")
#             arr.insert(0, arr[r])
#             arr.pop(r+1)
#             l += 1
#         else: r -=1
#     return arr

def pivotArray(arr, pivot):
    i = 0
    for j in arr:
        if arr[i] < pivot:
            arr.insert(0, arr[i])
            i += 1
            arr.pop(i)
        elif arr[i] > pivot:
            arr.append(arr[i])
            arr.pop(i)
            if i != 0:
                i+=1
        else: i+=1
    return arr
            
        

arr = [9, 33, 10, 5, 3, 12]
arr = pivotArray(arr, 10)


tc.assertEqual(arr, [3, 5, 9, 10, 33, 12])

arr2 = [9, 12, 3, 5, 14, 10, 10]
arr2 = pivotArray(arr2, 10)
tc.assertEqual(arr2, [5, 9, 3, 10, 10, 14, 12])


arr2 = [9, 12, 3, 5, 14, 10, 10]
arr2 = pivotArray(arr2, 10)
tc.assertEqual(arr2, [5, 9, 3, 10, 10, 14, 12])
            
arr3 = [9, 12, 3, 5, 14, 10, 10]
arr3 = pivotArray(arr3, 14)
tc.assertEqual(arr3, [10, 10, 5, 3, 12, 9, 14])           

arr4 = [9, 12, 3, 5, 14, 10, 10]
arr4 = pivotArray(arr4, 3)
tc.assertEqual(arr4, [3, 14, 10, 12, 10, 9, 5])   