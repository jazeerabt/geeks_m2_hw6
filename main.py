def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(unsorted_list)

print("Отсортированный список:", sorted_list)



def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

search_list = [11, 12, 22, 25, 34, 64, 90]
# element_to_find = 22
# result = binary_search(search_list, element_to_find)
# if result != -1:
#     print(f"Элемент {element_to_find} найден в позиции {result}")
# else:
#     print(f"Элемент {element_to_find} не найден в списке")

element_to_find = 56
result = binary_search(search_list, element_to_find)
if result != -1:
    print(f"Элемент {element_to_find} найден в позиции {result}")
else:
    print(f"Элемент {element_to_find} не найден в списке")