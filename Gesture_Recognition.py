import operator
import math
"""
@func Recognize()

1--thumb(red)
2--index(green)
3--palm(blue)
4--back(sth)


@global int Dcy: natural decay rate

@param frame prev = [point p0, [point p1, [...]]];
@param frame curr = [point p0, [point p1, [...]]];
@type point = (int x, int y, int a, int timestamp); 0<=x<=1, 0<=y<=1, 0<=a<=1


@gesture

palm gestures(1, 2, 3 shown together):
1) Swipe left: 
   1, 2, 3 move to left together
   action: Ctrl-tab

2) Swipe right: 
   1, 2, 3 move to right together
   action: Ctrl-shift-tab

3) Push Up: 
   1, 2, 3 move up together
   action: Show Desktop

4) Expand:
   1 moves to the left
   2 moves up
   distance with 3 increases

5) Shrink
   1 moves down
   2 moves up
   distance with 3 distance

mouse gesture:
1) Click

2) Double Click

"""

dcy = 2

def localize(prev, curr):
	return prev[1], prev[2], prev[3], curr[1], curr[2], curr[3]

def swipe_right_recognize(prev, curr):
	p1, p2, p3, c1, c2, c3 = localize(prev, curr)

	timespan = curr[0] - prev[0]

	scalar = 100

	if c1[0] and c2[0] and c3[0] and p1[0] and p2[0] and p3[0]:
		#showing your palm
		#calculate the vectors
		v1 = tuple(map(operator.sub, c1, p1))
		v2 = tuple(map(operator.sub, c2, p2))
		v3 = tuple(map(operator.sub, c3, p3))
		#if v1[0] < 0 and v2[0] < 0 and v3[0] < 0:
			# the whole hand is moving left
		return -scalar * ((v1[0] + v2[0] + v3[0]) / 3) / timespan - dcy

	return -dcy

def swipe_left_recognize(prev, curr):
	p1, p2, p3, c1, c2, c3 = localize(prev, curr)

	timespan = curr[0] - prev[0]

	scalar = 100

	if c1[0] and c2[0] and c3[0] and p1[0] and p2[0] and p3[0]:
		#showing your palm
		#calculate the vectors

		v1 = tuple(map(operator.sub, c1, p1))
		v2 = tuple(map(operator.sub, c2, p2))
		v3 = tuple(map(operator.sub, c3, p3))

		#if v1[0] > 0 and v2[0] > 0 and v3[0] > 0:
			# the whole hand is moving left
		return scalar * ((v1[0] + v2[0] + v3[0]) / 3) / timespan - dcy

	return -dcy


def swipe_up_recognize(prev, curr):
	p1, p2, p3, c1, c2, c3 = localize(prev, curr)

	timespan = curr[0] - prev[0]

	scalar = 100

	if c1[1] and c2[1] and c3[1] and p1[1] and p2[1] and p3[1]:
		#showing your palm
		#calculate the vectors
		v1 = tuple(map(operator.sub, c1, p1))
		v2 = tuple(map(operator.sub, c2, p2))
		v3 = tuple(map(operator.sub, c3, p3))
		#if v1[0] < 0 and v2[0] < 0 and v3[0] < 0:
			# the whole hand is moving left
		return scalar * ((v1[1] + v2[1] + v3[1]) / 3) / timespan - dcy

	return -dcy


def distance(p1, p2):
	return math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))

def expand_recognize(prev, curr):
	p1, p2, p3, c1, c2, c3 = localize(prev, curr)

	timespan = curr[0] - prev[0]

	scalar = 100

	if c1[0] and c2[0] and c3[0] and p1[0] and p2[0] and p3[0]:
		#showing palm
		prev_d1 = distance(p1, p3)
		prev_d2 = distance(p2, p3)
		curr_d1 = distance(c1, c3)
		curr_d2 = distance(c2, c3)

		diff_1 = curr_d1 - prev_d1
		diff_2 = curr_d2 - prev_d2

		return scalar * (diff_1 + diff_2)/timespan - dcy

		

	return -dcy

def shrink_recognize(prev, curr):
	p1, p2, p3, c1, c2, c3 = localize(prev, curr)

	timespan = curr[0] - prev[0]

	scalar = 100

	if c1[0] and c2[0] and c3[0] and p1[0] and p2[0] and p3[0]:
		#showing palm
		prev_d1 = distance(p1, p3)
		prev_d2 = distance(p2, p3)
		curr_d1 = distance(c1, c3)
		curr_d2 = distance(c2, c3)

		diff_1 = curr_d1 - prev_d1
		diff_2 = curr_d2 - prev_d2

		return -scalar * (diff_1 + diff_2)/timespan - dcy

		

	return -dcy










		