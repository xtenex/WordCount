#!/usr/bin/python

import sys

def main():
	
	w = {}
	f = open(sys.argv[1])
	for i in f.readlines():
		for l in i.split():
			if w.has_key(l) == True:
				w[l] += 1
			else:
				w[l] = 1
	f.close()
	for k in w.keys():
		print k + ": " + str(w[k])

if __name__ == '__main__':
	main()
