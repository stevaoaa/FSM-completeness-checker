#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys


#verification to avoid executions without the lib properly instaled
try:
	from treelib import Tree
except:
	print 'Please, verify README.md file and follow instructions'
	sys.exit(-1)





"""
	Take a list with sequences formed by input/output and build the test tree. Will use treelib
"""
def build_test_tree(sequences):
	
	"""
		Args:
			sequences = a list that contanis the set of sequences. Format [[seq1], [seq2], [...]]
	"""

	tree = Tree() #test tree
	
	#add root to the tree
	node = tree.create_node('empty', 0)

	#get the root id to identify some parents nodes bellow
	root_id = node.identifier

	#just a counter to mantain a id to each node in the tree. 
	i = 0

	#sequence is as list with the inputs off each sequence 
	for sequence in sequences:

		#as tree already have one element, begin the counter at 1.
		i = i + 1

		#get the first element of the sequence
		init = sequence.pop(0)

		#add to the tree
		node = tree.create_node(init, i, parent = root_id)

		#parent to the nexts childs
		parent_id = node.identifier

		#now go through every input in the sequence. Every input will be a node into the teste tree
		for s in sequence:

			#increment the ID counter
			i = i + 1

			#add s node to the tree
			node = tree.create_node(s, i, parent = parent_id)

			#update parent for next iteration
			parent_id = node.identifier

	#to vizualize a representation of the tree in terminal uncomment the line bellow
	#tree.show()

	return tree