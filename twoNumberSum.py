# solution1

def twoNumberSum(array, targetSum):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []

# solution2

def twoNumberSum(array, targetSum):
    d = {}
    for v in array:
        if d.get(v) == None:
            d[v] = 0
        else:
            d[v] += 1
    for v in array:
        if d.get(targetSum-v) != None:
            if v == targetSum - v:
                if d[targetSum-v] > 0:
                    return [v, targetSum-v]
                else:
                    continue
            else:
                return [v, targetSum-v]
    return []

# solution 3 - after sorting 