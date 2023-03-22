# My solution
class Solution:
    def romanToInt(self, s: str) -> int:
        dict_value = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        if s in dict_value:
            return dict_value[s]
        value = 0
        switch = 0
        for i in range(len(s)-1):
            if switch == 1:
                switch = 0
                continue
            if dict_value[s[i]] < dict_value[s[i+1]]:
                switch = 1 
                value = value + dict_value[s[i+1]] - dict_value[s[i]]
            else:
                value = value + dict_value[s[i]]
        if switch == 0:
            value = value + dict_value[s[len(s)-1]]
        return value

# Better solution
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
        return sum(map(lambda x: roman_to_integer[x], s))   