def helpf(array, depth):
	ans = 0
	while array:
		first = array.pop(0)
		if type(first) != list:
			ans += first * depth
		else:
			ans += helpf(first, depth + 1)
	return ans

def productSum(array):
    # Write your code here.
	ans = 0
	depth = 1
	while array:
		first = array.pop(0)
		if type(first) != list:
			ans += first * depth
		
		else:
			ans += helpf(first, depth + 1)
	return ans

print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))  # 12