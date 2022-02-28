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
if a == 1:
    print("please enter string to rev")
    exit(0)
while i < a:
    string = sys.argv[i]
    print(string[::-1])
    i += 1
