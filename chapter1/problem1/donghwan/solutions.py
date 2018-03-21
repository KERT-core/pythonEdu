def solution(nums):
	if nums < 0:
		for i in range(len(nums)-1,0,-1):
			temp += nums[i]
		temp = (-1)*int(temp)
	elif nums = 0:
		return 0
	else:
		nums = str(nums)
		for i in range(len(nums)-1,-1,-1):
			temp += nums[i]
		temp = int(temp)
	return temp