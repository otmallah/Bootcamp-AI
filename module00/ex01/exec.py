# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: otmallah <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/28 17:18:08 by otmallah          #+#    #+#              #
#    Updated: 2022/02/28 17:18:15 by otmallah         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

i = 1
a = len(sys.argv)
jomla = ''

if a == 1:
    print("please enter string to rev")
    exit(0)
if (a == 2):
    string = sys.argv[i].swapcase()
    print(string[::-1]) 
if a > 2:
    while i < a:
        string = sys.argv[i].swapcase()
        jomla = jomla + string + ' '
        i += 1
    print(jomla)
