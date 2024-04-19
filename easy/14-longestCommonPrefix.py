def longestCommonPrefix(strs):
    result = ''
    for i in range(len(strs[0])):
        for j in range(len(strs)):
            if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                return result
        result += strs[0][i]
    return result

print(longestCommonPrefix(["flower","flow","flight"]))  # "fl"
print(longestCommonPrefix(["dog","racecar","car"]))  # ""