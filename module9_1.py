def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        result_value = function(int_list)
        result_name = function.__name__
        results[result_name] = result_value
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))