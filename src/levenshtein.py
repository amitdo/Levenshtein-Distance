import sys

def print_tab ( d, len1, len2 ):
	for y in range ( 0, len2 ):
		for x in range ( 0, len1 ):
			print ( " {} ".format ( d [ x + y * len1 ] ) ),
		print

def levenshtein ( word1, word2 ):
	len1 = len ( word1 ) + 1
	len2 = len ( word2 ) + 1

	d = [ 0 ] * ( len1 * len2 )

	for i in range ( len1 ):
		d [ i ] = i
	for j in range ( len2 ):
		d [ j * len1 ] = j

	for j in range ( 1, len2 ):
		for i in range ( 1, len1 ):
			remove = d [ i - 1 + j * len1 ] + 1
			insert = d [ i + ( j - 1 ) * len1 ] + 1
			substitute = d [ i - 1 + ( j - 1 ) * len1 ] + ( 0 if word1 [ i - 1 ] == word2 [ j - 1 ] else 1 )
			d [ i + j * len1 ] = min ( remove, insert, substitute )
	print_tab ( d, len1, len2 )
	return d [ -1 ]

if len ( sys.argv ) != 3 :
	sys.stderr.write ( "Usage: python levenshtein.py [ word 1 ] [ word 2 ]\n" )
else:
	arg1 = sys.argv [ 1 ]
	arg2 = sys.argv [ 2 ]
	lev = levenshtein ( sys.argv [ 1 ], sys.argv [ 2 ] )
	print ( "The Levenshtein distance between '{}' and '{}' is {}".format ( sys.argv [ 1 ], sys.argv [ 2 ], lev ) )
