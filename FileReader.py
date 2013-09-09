#!/usr/bin/python

import psycopg2
import sys

connectN = None

#function for reading file
def reading_file(fp1):
	i = 0
	fp2 = open('sam.txt','r+') 
	array = []
	for line in fp1:
		array.append(line)
		i=i+1
	for j in range (i):
		print(j,array[j])


#function for reading database
def db_reading():
	#creating connection with DB
	try:
		connectN = psycopg2.connect(database='mapreduce',user='postgres',host='localhost',password='spw666')
		print "connection successful"

	except psycopg2.DatabaseError, e:
		print "unable to connect db"
		print 'Error %s' %e

#main function 
def main():
	fp = open('sam.txt','r+')
	
	#calling different function
	reading_file(fp)	
	db_reading()

	
	fp.seek(0)
	c = fp.readlines()
	print("Hero=%s" %c)
main()
