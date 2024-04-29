def strStr(heystack, needle):
    if needle not in heystack:
        return -1
    return heystack.index(needle)

print(strStr("sadbutsad", "sad"))
print(strStr("leetcode", "leeto"))
    