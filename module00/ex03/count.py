# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: otmallah <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/28 20:53:29 by otmallah          #+#    #+#              #
#    Updated: 2022/02/28 20:53:29 by otmallah         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from os import PRIO_USER
import string
import sys
from turtle import pu

punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

def text_analyzer(var):
	'''What is the text to analyze?'''
	if var.isnumeric():
		print("AssertionError: argument is not a string")
		exit(1)
	l = len(var)
	print(f"The text contains {l} character(s):")
	test(var)

def test(string):
	num_low = 0
	num_spa = 0
	num_upp = 0
	num_punk = 0
	for i in string:
		if i in punc:
			num_punk += 1
		if i.islower():
			num_low += 1
		elif i.isupper():
			num_upp += 1
		elif i == ' ':
			num_spa += 1
	print("space " + str(num_spa))
	print("lower letter(s) " + str(num_low))
	print("upper letter(s) " + str(num_upp))
	print("punctuation mark(s) " + str(num_punk))
   
a = len(sys.argv)
if a == 1:
	print(text_analyzer.__doc__)
if a == 2:
	text_analyzer(sys.argv[1])

	