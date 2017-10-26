n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

no_of_swap = 0
is_sorted = False
last_sorted_index = len(a) -1

while not is_sorted:
    is_sorted = True
    for i in range(last_sorted_index):
        if a[i] > a[i+1]:
            is_sorted = False
            val = a[i+1]
            a[i+1] = a[i]
            a[i] = val
            no_of_swap += 1
    last_sorted_index -= 1

first_element = a[0] if len(a) > 0 else ""
last_element = a[-1] if len(a) > 0 else ""
print("Array is sorted in {} swaps.".format(no_of_swap))
print("First Element: {}".format(first_element))
print("Last Element: {}".format(last_element))
