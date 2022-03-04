# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: otmallah <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/04 17:48:31 by otmallah          #+#    #+#              #
#    Updated: 2022/03/04 17:48:31 by otmallah         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string
import sys

size = len(sys.argv)
newlist = []
if size == 2 or size == 1:
	print('ERROR')
	exit()
if size == 3:
	string = sys.argv[1]
	jomla = ''
	check = len(string)
	for i in string:
		if i != ' ' and i != check:
			jomla = jomla + i
		else:
			if len(jomla) > int(sys.argv[2]):
				newlist.append(jomla)
				jomla = ''

print(newlist)