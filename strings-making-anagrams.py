def number_needed(a, b):
    a_dict = {}
    b_dict = {}
    for i in range(len(a)):
        key = a_dict.get(a[i])
        if key:
            a_dict[a[i]] += 1
        else:
            a_dict[a[i]] = 1
            
    for i in range(len(b)):
        key = b_dict.get(b[i])
        if key:
            b_dict[b[i]] += 1
        else:
            b_dict[b[i]] = 1
    
    a_keys = a_dict.keys()
    b_keys = b_dict.keys()
    common_keys = list(filter(lambda x: x in b_keys, a_keys))
    a_not_common_keys = list(filter(lambda x: x not in b_keys, a_keys))
    b_not_common_keys = list(filter(lambda x: x not in a_keys, b_keys))
    
    # count not common keys deletion
    a_total_delete = sum(list(map(lambda x: a_dict[x], a_not_common_keys)))
    b_total_delete = sum(list(map(lambda x: b_dict[x], b_not_common_keys)))
    
    total = 0
    # Finding the diff
    for key in common_keys:
        a_value = a_dict[key]
        b_value = b_dict[key]
        
        total += (max(a_value, b_value) - min(a_value, b_value))
        
    return total + a_total_delete + b_total_delete

a = input().strip()
b = input().strip()

print(number_needed(a, b))
