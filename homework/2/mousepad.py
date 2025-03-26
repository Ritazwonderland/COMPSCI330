'''COLLABORATION:
- Write the names of anyone/anything that you
consulted besides your partner or course materials here:

Worked with #####, ####, and ####, and referenced ##### and ######.
'''

### TODO: FINISH THIS METHOD
def max_revenue(a,b,P):
	'''
	a,b: positive integers denoting the size of the initial neoprene sheet, a x b.
	P[0..a][0..b]: an a x b 2D array where P[i][j] is the price for an i x j mouse pad.
				   In particular, P[0][j] = P[i][0] = 0 for all i,j.

	Returns the maximum cummulative profit possible from cutting the
	initial a x b neoprene sheet into rectangles with vertical and
	horizontal cuts using the prices from P.
	'''
	#for each piece of sub sheet:
	#vertical/horizontal cut: a -> v, a-v / b -> h, b-h
	#max of:
	#	cut: 1->i, 1->j, max{(memo[subsheetA]+memo[subsheetB])} 
	#	doesn't cut: P[subsheet]
	memo = []
	for i in range(a+1):
		memo.append([0]*(b+1))
	for height in range(1,a+1):
		for width in range(1, b+1):
			submax = 0
			maxhw = P[height][width]
			if height > 1:
				for v in range(1, height):
					vsum = memo[v][width] + memo[height-v][width]
					if vsum > submax:
						submax = vsum
			if width > 1:
				for h in range(1, width):
					hsum = memo[height][h] + memo[height][width-h]
					if hsum > submax:
						submax = hsum
			if submax > maxhw:
				maxhw = submax
			memo[height][width] = maxhw
	return memo[a][b]

if __name__=='__main__':
	'''Anything below this line will not be ran by the autograder.
	You may use this space to debug your code.'''

	P = [
			[0, 0,  0,  0,  0,  0],
			[0, 1, 12, 13,  3,  7],
			[0, 8, 27, 30, 11,  9],
			[0, 8,  7,  0,  8, 16],
		]
	
	P1 = [
			[0, 0,  0,  0,  0,  0],
			[0, 1, 1, 1,  1,  1],
			[0, 1, 1, 1, 1,  1],
			[0, 1,  1,  1,  1, 1],
		]

	soln = max_revenue(3, 5, P1)
	print(soln)