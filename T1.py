def min_subsequences(source, target):
    subsequences_count = 0
    i, j = 0, 0
    subseq_list = [] #子串列表
    while j < len(target):
        subseqs_matched = False
        temp = j
        for subseq in subseq_list :#先查看子串列表有无匹配
            i = 0
            subseq_matched = True
            while i < len(subseq) and j < len(target):
                if source[i] != target[j]:
                    subseq_matched = False
                    break
                j += 1
                i += 1
            if subseq_matched :
                subseqs_matched = True
                break
        if subseqs_matched :
            break
    #子串列表无匹配再新增一个最长子串
        i = 0
        j = temp
        subsequences_count += 1
        current_char_matched = False
        temp_subseq = ''
        while i < len(source) and j < len(target):
            if source[i] == target[j]:
                temp_subseq+=source[i]
                j += 1
                current_char_matched = True
            i += 1
        if temp_subseq != '':
            subseq_list.append(temp_subseq)#将新子串加入子串列表
        if not current_char_matched:
            return -1
    return subsequences_count


# Examples
print(min_subsequences("abc", "abcbc"))  # Output: 2
print(min_subsequences("abc", "acdbc"))  # Output: -1
print(min_subsequences("xyz", "xzyxz"))  # Output: 3
print(min_subsequences("xyz", "xyzxyz"))  # Output: 1