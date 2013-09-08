#!/usr/bin/python

def main():
	fp = open('sam.txt','r+')
	
	for line in fp:
		print line 
	
	fp.seek(0)
	c = fp.readlines()
	print("Hero=%s" %c)
main()
