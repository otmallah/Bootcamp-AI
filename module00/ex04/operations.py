# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: otmallah <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/01 16:55:27 by otmallah          #+#    #+#              #
#    Updated: 2022/03/01 16:55:29 by otmallah         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

a = len(sys.argv)

if a == 1:
	print("Usage: python operations.py <number1> <number2>")
	print("Example:")
	print("       python operations.py 10 3")
if a == 2:
	print("more arg")
if a > 3:
	print("AssertionError: too many arguments")
if a == 3:
	if sys.argv[1].isalpha() or sys.argv[2].isalpha():
		print ("AssertionError: only integers")
		exit(1)
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	check_a = isinstance(a, int)
	check_b = isinstance(b, int)
	if check_a == True and check_b == True:
		print("sum       : " + str(a + b))
		print("Difference: " + str(a - b))
		print("Product   : " + str(a * b))
		if b != 0:
			print("Quotient  : " + str(a / b))
			print("Remainder : " + str(a % b))
		if b == 0:
			print("Quotient  : ERROR (division by zero)")
			print("Remainder : ERROR (modulo by zero)")
	else:
		print("only integer")
