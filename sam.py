#!/usr/bin/python

import time
def subtract1():
		print("Enter two numbers")
                x = int(input('A='))
                y = int(input('B='))
                z=x-y;
                print ('Subtraction of two numbers = %s' %z);
        

def sum1():
	print("Enter two numbers\n");
	x=int(input("A="))
	y=int(input("B="))
	z=x+y
	print ("Addition of two number = %s\n" %z)


def main():
	while True:
		print("Enter your choice\n1)Addition\t2)Subtraction\t3)Exit")
		a = int(input("choice = "))

	#while True:
		if a==1:
			sum1()

		elif a==2:
			subtract1()
		elif a==3:
			break
		else:
			print("Please Enter Correct Input\n")
			time.sleep(2)

main()
