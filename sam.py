#!/usr/bin/python

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
	print("Enter your choice\n1)Addition\t2)Subtraction")
	a = int(input("choice = "))

	if a==1:
		sum1()

	if a==2:
		subtract1()

main()
