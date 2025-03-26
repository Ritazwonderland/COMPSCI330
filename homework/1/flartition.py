from flippable_list import FlippableList
import random # useful for testing purposes and included example code below

'''COLLABORATION:
- Write the names of anyone/anything that you
consulted besides your partner or course materials here:

TODO: Include colloration notes.
'''

### TODO: FINISH THIS METHOD
def flartition(f, i, j, p):
	'''
	f: FlippableList object
	i: index
	j: index
	p: "pivot" value

	Modifies f._lst[i:j] (where f._lst is its represented list of integers) STRICTLY VIA f.flip OPERATIONS
	so that all elements less than p appear before all elements at least p, then returns the index of
	the first element at least p. If all elements in f._lst[i:j] are less than p, then j is returned.
	'''
	
	'''	
	#base case
	left = f.peek(i)
	right = f.peek(j-1)
	if j-i == 2:
		if left<p and right<p:
			return j
		if left>=p and right>=p:
			return i-1
		if left>right:
			f.flip(i,j)
		return i+1

	if j-i == 1:
		if left<p:
			return i+1
		else:
			return i
	'''
	if j - i <= 1:
        # Base case: single element or empty range
		return i if f.peek(i) >= p else i + 1
	
	#recursive case
	leftend = flartition(f,i,(i+j)//2,p)
#	print(leftend)
	rightend = flartition(f,(i+j)//2, j, p)
#	print(rightend)
	f.flip(leftend,rightend)
#	print(leftend + rightend - (i+j)//2)
	return leftend + rightend - (i+j)//2



if __name__=='__main__':
	'''Anything below this line will not be ran by the autograder.
	You may use this space to debug your code.'''
	"""test = FlippableList([3,4,5,7,1,2,8])
	flartition(test, 1, 6, 6)
	for i in range(len(test)): print(test.peek(i))"""


	n = 8

	# Example of creating a FlippableList
	L = list(range(1,n+1)) # create a list [1, 2, ..., n]
	a = FlippableList(L)  # create a FlippableList object representing the given list L

	# Example of flip() operation
	print('Before flip(2,5): {}'.format(str(a)))
	a.flip(2,5)
	print('After flip(2,5): {}'.format(str(a)))
	print()

	# Example of checking whether flartition works correctly:
	L = [4, 9, 330, 1, 2, 5, 8, 16]
	a = FlippableList(L)
	print('Before flartition(a, 2, 7, 6): {}'.format(str(a)))
	flartition(a, 2, 7, 6)
	print('After  flartition(a, 2, 7, 6): {}'.format(str(a)))
	print('Is it correct? {}'.format(a.is_parted(2,7,6)))
	print()