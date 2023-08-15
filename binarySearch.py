def findEl(lst, el):
    mid = len(lst) // 2
    
    if len(lst) == 0:
        return False
    elif lst[mid] == el:
        return True
    elif el > lst[mid]:
        return findEl(lst[mid + 1:], el)
    else:
        return findEl(lst[:mid], el)

my_list = (3, 4, 6, 4, 3, 5, 6, 4, 3, 6, 6, 4)
element_to_find = 5
found = findEl(my_list, element_to_find)

if found:
    print(f"Element {element_to_find} found in the list.")
else:
    print(f"Element {element_to_find} not found in the list.")
