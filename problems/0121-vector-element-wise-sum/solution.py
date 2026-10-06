def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	if(len(a) != len(b)):
		return -1
	else:
		output = []
		for a_i,b_i in zip(a,b):
			sum_i = a_i + b_i
			output.append(sum_i)
		return output