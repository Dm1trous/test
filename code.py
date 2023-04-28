from collections import Counter
def anagrams(str1, str2):
	return Counter(str1) == Counter(str2)
anagarms("abc1", "1bac")
print ("Some print")
