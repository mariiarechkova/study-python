def solution(s):
        new_s = list(s)
        l = len(new_s)
        result = []
        for i in range(l):
            try:
                if i % 2 == 0:
                    result.append(new_s[i] + new_s[i + 1])
            except:
                result.append(new_s[i] + "_")
        print(result)




solution('abcde')