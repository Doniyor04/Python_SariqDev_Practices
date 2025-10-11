numbers = range(1, 11)

def isEven(nums):
	if nums:
		evenNums = list(filter(lambda num: num % 2 == 0, nums))
	else:
		return "Ro'yxat bo'sh"
	return evenNums
