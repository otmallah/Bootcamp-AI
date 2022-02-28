# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: otmallah <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/28 19:21:58 by otmallah          #+#    #+#              #
#    Updated: 2022/02/28 19:21:59 by otmallah         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

a = len(sys.argv)
i = 1

if a > 2:
    print("AssertionError: more than one argument are provided")
    exit(0)
if a == 2: 
    check = sys.argv[i].isnumeric()
    if (check == False):
        print("AssertionError: argument is not an integer")
        exit(1)
    num = int(sys.argv[i])
    if num == 0:
        print("I'm Zero.")
    elif num % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
