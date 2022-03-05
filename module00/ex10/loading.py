# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: otmallah <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/05 15:49:47 by otmallah          #+#    #+#              #
#    Updated: 2022/03/05 15:49:47 by otmallah         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from asyncore import write
from ctypes import sizeof
from time import sleep


listy = range(100)

def	func(list):
	for elem in list:
		yield elem
jomla = '>'

ret = 0
for elem in func(listy):
	ret += (elem + 3) % 5
	jomla = '=' + jomla2
	print(jomla2)
	sleep(0.2)
	jomla2 = jomla
	del jomla

print(ret)


