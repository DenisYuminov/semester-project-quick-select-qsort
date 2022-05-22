def partition(l, r, nums):
    # Последним элементом будет точка поворота, а первым элементом - указатель
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            # Замена значений, меньших, чем точка поворота вперед
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    # Наконец, замена последнего элемента на номер, индексированный указателем
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr

def quicksort(l, r, nums):
    if len(nums) == 1:  # Завершающее условие для рекурсии
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi - 1, nums)  # Рекурсивная сортировка левых значений
        quicksort(pi + 1, r, nums)  # Рекурсивная сортировка правых значений
    return nums