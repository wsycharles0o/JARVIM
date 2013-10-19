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

def swipe_left_recognize(prev, curr):
	
	p1 = prev[1]
	p2 = prev[2]
	p3 = prev[3]
	p4 = prev[4]
	p5 = prev[5]

	c1 = curr[1]
	c2 = curr[2]
	c3 = curr[3]
	c4 = curr[4]
	c5 = curr[5]

	timespan = curr[0] - prev[0]

	scalar = 1

	if c1 && c2 && c3 && c4:
		#showing your palm
		#calculate the vectors
		v1 = tuple(map(operator.sub, c1, p1))
		v2 = tuple(map(operator.sub, c2, p2))
		v3 = tuple(map(operator.sub, c3, p3))
		v4 = tuple(map(operator.sub, c4, p4))

		if v1[0] < 0 && v2[0] < 0 && v3[0] < 0 && v4[0] < 0:
			# the whole hand is moving left
			return scalar*((v1[0] + v2[0] + v3[0] + v4[0])/4)/timespan

	return -100



def swipe_right_recognize(prev, curr):
	p1 = prev[1]
	p2 = prev[2]
	p3 = prev[3]
	p4 = prev[4]
	p5 = prev[5]

	c1 = curr[1]
	c2 = curr[2]
	c3 = curr[3]
	c4 = curr[4]
	c5 = curr[5]

	timespan = curr[0] - prev[0]

	scalar = 1

	if c1 && c2 && c3 && c4:
		#showing your palm
		#calculate the vectors
		v1 = tuple(map(operator.sub, c1, p1))
		v2 = tuple(map(operator.sub, c2, p2))
		v3 = tuple(map(operator.sub, c3, p3))
		v4 = tuple(map(operator.sub, c4, p4))

		if v1[0] > 0 && v2[0] > 0 && v3[0] > 0 && v4[0] > 0:
			# the whole hand is moving left
			return scalar*((v1[0] + v2[0] + v3[0] + v4[0])/4)/timespan

	return -100

def expand_recognize(prev, curr):
	
		