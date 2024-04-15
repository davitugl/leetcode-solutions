def romanToInt(s):
    help = {"I": 1, "II": 2, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for i in range(len(s)):
        if i + 1 < len(s) and help[s[i]] < help[s[i + 1]]:
            result -= help[s[i]]
        else:
            result += help[s[i]]
    return result


print(romanToInt("III"))  # 3
print(romanToInt("XIV"))  # 14 
print(romanToInt("MCMXCIV"))  # 1994