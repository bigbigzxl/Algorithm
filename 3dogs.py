#! /usr/bin/env python
# -*- coding: utf-8 -*-
def getfirstonebit(num):
	return num & ~(num - 1)


def findTwoDogger(array, length):
	a_XOR_b = 0
	firstonebit = 0
	a = 0
	b = 0
	for i in range(length):
		a_XOR_b ^= array[i]
	assert a_XOR_b != 0
	firstonebit = getfirstonebit(a_XOR_b)
	for i in range(length):
		if array[i] & firstonebit:
			a ^= array[i]
	b = a_XOR_b ^ a
	print("a = %d, b = %d" % (a, b))


def findoneDogger(array, length):
	a_XOR_b_XOR_c = 0
	c = 0
	firstonebit = 0
	for i in range(length):
		a_XOR_b_XOR_c ^= array[i]
	for i in range(length):
		# 使用异或排除掉不相干的元素
		# 简化为getFirstOneBit(a ^ b) ^ getFirstOneBit(a ^ c) ^ getFirstOneBit(b ^ c);
		firstonebit ^= getfirstonebit(a_XOR_b_XOR_c ^ array[i])
	for i in range(length):
		if getfirstonebit(a_XOR_b_XOR_c ^ array[i]) == firstonebit:
			c ^= array[i]
	print("c = %d" % (c))
	return c


if __name__ == "__main__":
	# 先找出一个来，然后再找出另外两个
	array1 = [9, 5, 8, 9, 5, 8, 1, 2, 3]
	c = findoneDogger(array1, len(array1))
	
	array2 = [9, 5, 8, 9, 5, 8, 1, 2, 3, c]
	findTwoDogger(array2, len(array2))