def solution(nums):
	if nums == []:
		return 0
	else:
		temp = []
		temp.append(nums[0])
		for i in range(0,len(nums)):
			a = 0
			for j in range(0,len(temp)):
				if nums[i] == temp[j]:
					a = 1
			if a == 0:
				temp.append(nums[i])
		
	return len(temp)



if __name__ == "__main__":
	a = solution([1,2,2])
	print(a)