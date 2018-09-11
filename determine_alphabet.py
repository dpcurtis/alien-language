def get_ordered_pair(first, second):
	"""
	This scans two words until a character difference is found. Then returns
	the characters that were matched. The lower being the character that comes
	before the upper.
	:param first:
	:param second:
	:return: lower, upper pair
	"""
	lower = None
	upper = None
	i = 0
	while i < len(first) and i < len(second) and lower is None and upper is None:
		if second[i] != first[i]:
			lower = first[i]
			upper = second[i]
		i = i + 1
	return lower, upper

def get_ordered_alphabet():
	"""
	This algorithm solves the ordered alphabet problem in two parts:
	1. Use the first letter of every word by iterating over every word.
	2. After that process, go through a complete set to find letters that are not
	in the ordered alphabet. Then take that missing letter and iterate through
	the ordered alphabet, and use the pairwise inference checks to find where it
	fits in the ordering.

	:return: ordered alphabet
	"""

	# this represents the entire set of characters in the alphabet
	alphabet = set()

	# represents the pair results from the prev/curr text letter order inference check
	all_upper_lower_pairs = {}

	# the resulting ordered alphabet
	ordered_alphabet = []

	# load up the file
	f = open('words_no_g.txt')
	line = f.readline().lower().rstrip('\n')

	# initialize
	previous_line = None
	curr = line[0]
	ordered_alphabet.append(line[0])

	# loop through all the lines
	while line:
		# add all the characters using a set hash.
		for character in line:
			alphabet.add(character)

		# get the pairwise inference
		if previous_line:
			lower, upper = get_ordered_pair(previous_line, line)
			if not all_upper_lower_pairs.get('{}{}'.format(lower, upper)):
				all_upper_lower_pairs['{}{}'.format(lower, upper)] = True

		# use the first letter of the dictionary to set the order. When a new letter
		# is found, that triggers the addition to the ordered list.
		if line[0] != curr:
			ordered_alphabet.append(line[0])
			curr = line[0]

		# move the previous line for use in pairwise inference
		previous_line = line

		# end of loop stuff
		line = f.readline()
		if line:
			line = line.lower().rstrip('\n')

	f.close()

	# this is step 2 where we match the characters that didn't appear as the first
	# character in any word.
	for character in alphabet:
		if character not in ordered_alphabet:
			for i in range(0, len(ordered_alphabet) - 1):
				pair_one = '{}{}'.format(ordered_alphabet[i], character)
				pair_two = '{}{}'.format(character, ordered_alphabet[i+1])
				if all_upper_lower_pairs.get(pair_one) and all_upper_lower_pairs.get(pair_two):
					ordered_alphabet.insert(i+1, character)

	return ordered_alphabet

ordered_alphabet = get_ordered_alphabet()
print ordered_alphabet