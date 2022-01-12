# Number 0
def longestSubstringWithoutDuplication(string):
	longest_substring= ''
	current= ''
	i= 0
	j= i
	if len(string) == 1:
		return string[0]
	while i < len(string):
		if j == len(string):
			i+= 1
			j= i
		elif string[j] in current:
			if len(current) > len(longest_substring):
				longest_substring= current
			current= ''
			i+= 1
			j= i
		else:
			current+= string[j]
			j+= 1
	return longest_substring