import sys

def print_tab ( d, len1, len2 ):
	for x in range ( 0, len1 ):
		for y in range ( 0, len2 ):
			print ( " {} ".format ( d [ x ] [ y ] ) ),
		print

def levenshtein ( word1, word2 ):
	len1 = len ( word1 )
	len2 = len ( word2 )
	d = [ [ 0 for x in range ( len1 + 2 ) ] for y in range ( len2 + 2 ) ]
	for i in range ( 0, len1 + 1):
		d [ i ] [ 0 ] = i
	for j in range ( 0, len2 + 1):
		d [ 0 ] [ j ] = j
	for i in range ( 1, len1 + 1 ):
		for j in range ( 1, len2 + 1):
			remove = d [ i - 1 ] [ j ] + 1
			insert = d [ i ] [ j - 1 ] + 1
			substitute = d [ i - 1 ] [ j - 1 ] + ( 0 if word1 [ i - 1 ] == word2 [ j - 1 ] else 1 )
			d [ i ] [ j ] = min ( remove, insert, substitute )
	print_tab ( d, len1 + 1, len2 + 1 )
	return d [ len1 ] [ len2 ]

if len ( sys.argv ) != 3 :
	sys.stderr.write ( "Usage: python levenshtein.py [ word 1 ] [ word 2 ]\n" )
else:
	arg1 = sys.argv [ 1 ]
	arg2 = sys.argv [ 2 ]
	if len ( arg1 ) < len ( arg2 ):
		lev = levenshtein ( arg1, arg2 )
	else:
		lev = levenshtein ( arg2, arg1 )
	print ( "The Levenshtein distance between '{}' and '{}' is {}".format ( sys.argv [ 1 ], sys.argv [ 2 ], lev ) )
