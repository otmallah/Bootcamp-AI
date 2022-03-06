# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: otmallah <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/03 22:19:54 by otmallah          #+#    #+#              #
#    Updated: 2022/03/03 22:19:55 by otmallah         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


#secret_num = 21
#
#a = '''This is an interactive guessing game!
#You have to enter a number between 1 and 30 to find out the secret number.
#Type 'exit' to end the game.
#Good luck!')'''
#
#b = '''Congratulations, you've got it!
#You won in 5 attempts!'''
#
#print(a)
#i = 0
#print('What\'\s your guess between 1 and 99?')
#str2 = input('=')
#while str2:
#    str2 = input('=')
#    if str2 == 'exit':
#        print('Goodbye !!')
#        exit(0)
#    elif int(str2) < 15:
#        print('zid mazal')
#    elif int(str2) > 15:
#        print('ba3adty')
#    if int(str2) == secret_num:
#        print(b)
#        exit(0)

import random

a = random.randint(0, 99)
num = 1
number = a
fir = '''This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!')'''
b = '''Congratulations, you've got it!'''
spe = '''The answer to the ultimate question of life,
	the universe and everything is 42 Congratulations! You got it on your first try! '''
print(fir)
string = int(input('number = '))

while 1:
	if string == number and num == 1:
		print("Congratulations, You got it in on your first try!! ")
		exit(0)
	elif string == number and number == 42 and num == 1:
		print(spe)
		exit(0)
	elif string > number:
		print('Too high !')
		print('What\'\s your guess between 1 and 99?')
	elif string < number:
		print('Too low !')
		print('What\'\s your guess between 1 and 99?')
	elif string == number:
		print(b)
		print('You won in ' + str(num) + ' attempts')
		exit(0)
	elif str(string) == 'exit':
		print('Goodbye!!')
	num += 1
	string = int(input('number = '))

