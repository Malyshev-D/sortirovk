def bubble_sort(a):
    n = len(a)
    nesort = True
    while nesort:
        nesort = False
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                nesort = True
        n -= 1

def vibor_sort(a):
    for i in range(len(a) - 1):
        imin = i
        for j in range(i + 1, len(a)):
            if a[j] < a[imin]:
                imin = j
            a[i], a[imin] = a[imin], a[i]
def quick_sort(a):
    if len(a) <= 1:
        return(a)
    pivot = a[len(a) // 2]
    levo = [x for x in a if x < pivot]
    mid = [x for x in a if x == pivot]
    pravo = [x for x in a if x > pivot]

    return quick_sort(levo) + mid + quick_sort(pravo)

def insert_sort(a):
    for i in range(1, len(a)):
        x = a[i]
        j = i - 1
        while j >= 0 and a[j] > x:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = x

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    left_list_length, right_list_length = len(left_list), len(right_list)

    for i in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list

def merge_sort(mas):
    if len(mas) <= 1:
        return mas
    mid = len(mas) // 2
    left_list = merge_sort(mas[:mid])
    right_list = merge_sort(mas[mid:])
    return merge(left_list, right_list)
