# CS 330: Summer 2024
# Author: Alex Steiger

class FlippableList:

	def __init__(self, lst):
		self._lst = list(lst) # do not access!
		self._count = 0     # do not access!

	def peek(self, i):
		# self._count += 1
		return self._lst[i]

	'''reverses the sublist _lst[i:j]'''
	'''assumes j <= len(_lst)'''
	def flip(self, i, j):
		self._count += max(1,j-i)

		if i >= j-1:
			return

		for k in range((j-i)//2):
			self._lst[i+k], self._lst[j-1-k] = self._lst[j-1-k], self._lst[i+k]

	###### HELPER FUNCTIONS BELOW #######

	'''allows you to call str() directly on a FlippableList for debugging purposes'''
	def __str__(self):
		return str(self._lst)

	'''allows you to call len() directly on a FlippableList for debugging purposes'''
	def __len__(self):
		return len(self._lst)

	'''for debugging purposes, helper function to check if _lst[i:j] is partitioned correctly for pivot "pivot"'''
	'''assumes j <= len(_lst)'''
	def is_parted(self, i, j, pivot):
		lst = self._lst[i:j]

		if len(lst) < 2:
			return True

		last_smaller = i-1
		first_at_least = j

		for k,x in enumerate(lst):
			if x < pivot and k > last_smaller:
				last_smaller = k

			if x >= pivot and k < first_at_least:
				first_at_least = k

		return first_at_least > last_smaller

	'''helper function to check if _lst entirely is sorted'''
	def is_all_sorted(self):
		return self.is_sorted(0,len(self._lst))

	'''helper function to check if _lst[i:j] is sorted'''
	def is_sorted(self, i, j):
		lst = self._lst[i:j]
		return lst == sorted(lst)