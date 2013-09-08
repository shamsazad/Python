#!/usr/bin/python

def reading_file(fp1):
	i = 0
	fp2 = open('sam.txt','r+') 
	array = []
	for line in fp1:
		array.append(line)
		i=i+1
	for j in range (i):
		print(j,array[j])

def main():
	fp = open('sam.txt','r+')
	reading_file(fp)	
	
	fp.seek(0)
	c = fp.readlines()
	print("Hero=%s" %c)
main()
