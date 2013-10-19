import operator
"""
@func Recognize()

1--thumb
2--index
3--middle
4--palm
5--back

@param frame prev = [point p0, [point p1, [...]]];
@param frame curr = [point p0, [point p1, [...]]];
@type point = (int x, int y, int a, int timestamp); 0<=x<=1, 0<=y<=1, 0<=a<=1

"""

def localize(prev, curr):
	return prev[1], prev[2], prev[3], prev[4], curr[1], curr[2], curr[3], curr[4]

def swipe_left_recognize(prev, curr):
	p1, p2, p3, p4, c1, c2, c3, c4 = localize(prev, curr)

	timespan = curr[0] - prev[0]

	scalar = 0.1

	if c1[0] and c2[0] and c3[0] and c4[0] and p1[0] and p2[0] and p3[0] and p4[0]:
		#showing your palm
		#calculate the vectors
		v1 = tuple(map(operator.sub, c1, p1))
		v2 = tuple(map(operator.sub, c2, p2))
		v3 = tuple(map(operator.sub, c3, p3))

		if v1[0] < 0 and v2[0] < 0 and v3[0] < 0:
			# the whole hand is moving left
			return scalar * ((v1[0] + v2[0] + v3[0]) / 3) / timespan

	return -5

def swipe_right_recognize(prev, curr):
	p1, p2, p3, p4, c1, c2, c3, c4 = localize(prev, curr)

	timespan = curr[0] - prev[0]

	scalar = 0.1

	if c1[0] and c2[0] and c3[0] and c4[0] and p1[0] and p2[0] and p3[0] and p4[0]:
		#showing your palm
		#calculate the vectors

		#TEST CODE!!!!!!! REMEMBER TO DELETE
		print "YEAH!!!"

		v1 = tuple(map(operator.sub, c1, p1))
		v2 = tuple(map(operator.sub, c2, p2))
		v3 = tuple(map(operator.sub, c3, p3))

		if v1[0] > 0 and v2[0] > 0 and v3[0] > 0:
			# the whole hand is moving left
			return scalar * ((v1[0] + v2[0] + v3[0]) / 3) / timespan

	return -5

def expand_recognize(prev, curr):
	pass
		