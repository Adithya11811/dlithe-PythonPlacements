def power_Set(s):
    res = [[]]
    for elem in s:
        res.extend([sub+[elem] for sub in res])

    return [set(sub) for sub in res]

inp = {1,2,3}
powerSet = power_Set(inp)
print("Power Set:", powerSet)