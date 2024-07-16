def max_value(input):
    #遍历所有中位数可能性，找出确定各中位数时的最大平均数
    input = sorted(input)
    maxval = 0
    i = 0
    j = 0
    while(i < len(input)):# 中位数只取一数时
        current_median = input[i]
        if i>0 and i<len(input)-1:
            current_mean = (input[i-1] + input[i] + input[len(input)-1]) / 3
            val = current_mean - current_median
            maxval = max(val, maxval)
        i += 1
    i = 0
    while(i < len(input)):# 中位数取两数平均时
        j = i + 1
        while(j < len(input)):
            current_median = (input[i] + input[j]) / 2
            if i>0 and j<len(input)-1:
                current_mean = (input[i-1] + input[i] + input[j] + input[j+1]) / 4
                val =current_mean - current_median
                maxval = max(val,maxval)
            j += 1
        i += 1
    return maxval

# Examples
print(max_value([1,9,3,5])) # Output: 1.333...
print(max_value([1,3,5,9])) # Output: 1.333...