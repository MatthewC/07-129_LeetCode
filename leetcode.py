# Write a function that reverses a string. The input string is given as an array of characters s.

class Solution:
	def reverseString(self, s: List[str]) -> None:
		"""
		Do not return anything, modify s in-place instead.
		"""
		s.reverse()



# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		for i in range(len(nums)):
			for j in range(len(nums)):
				if nums[i] + nums[j] == target and not (i == j):
					return [i, j]



# Given an integer x, return true if x is palindrome integer.
class Solution:
	def isPalindrome(self, x: int) -> bool:
		if x < 0:
			return False
		reversedNum = 0
		numSize = 1
		
		while x // (10 ** numSize) != 0:
			numSize += 1
			
		for i in range(numSize):
				num = (x // (10 ** i)) % 10
				reversedNum += num * 10 ** (numSize-i-1)
			
		if reversedNum == x:
			return True
		else:
			return False
		