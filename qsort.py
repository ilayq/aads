from random import randrange, choice


arr = [randrange(1, 11) for _ in range(10)]
print(arr)


def issorted(arr: list[int]) -> bool:
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

# bad in memory
def qsort_naive(arr: list[int]) -> list[int]:
    if issorted(arr):
        return arr
    if len(arr) <= 1:
        return arr
    else:
        pivot = choice(arr)
        lower = [num for num in arr if num < pivot]
        mid = [num for num in arr if num == pivot]
        upper = [num for num in arr if num > pivot]
        return qsort_naive(lower) + mid + qsort_naive(upper)


def qsort(nums: list, fst, lst) -> None:
    if fst >= lst: return
 
    i, j = fst, lst
    pivot = nums[randrange(fst, lst + 1)]
 
    while i <= j:
        while nums[i] < pivot: i += 1
        while nums[j] > pivot: j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
    qsort(nums, fst, j)
    qsort(nums, i, lst)

asd = qsort_naive(arr)
qsort(arr, 0, len(arr) - 1)
print(asd)
print(arr)

