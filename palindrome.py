def palindrome(string):
	num = len(string) - 1
	second_half = ''
	mid = len(string) - 1
	while (num > mid/2):
		second_half += string[num]
		num -=1
    first_half = string[0:len(string)/2]
	if first_half == second_half:
		return True
	else:
		return False

print palindrome("aoooa")