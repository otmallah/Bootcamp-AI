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


from cgi import test
from curses.ascii import isupper


#str = 'kkKKKK'
#upp = 0
#low = 0
#spa = 0
#
#def test_analyse(str):
#    for elem in str:
#        if elem.isupper():
#            upp += 1
#        elif elem.islower():
#            low += 1
#        elif elem == ' ':
#            spa += 1
#        print("num space " + spa)

def tes(str):
    if str.isalnum():
        print("ok")


tes("cksjdkjsbfvjsk84bdf")


#rom curses.ascii import isupper
#mport sys
#
#
#ef text_analyzer(string):
#   for elem in string:
#       if elem.isupper():
#           upp += 1
#       elif elem.islower():
#           low += 1
#       elif elem == ' ':
#           spa += 1
#   print("num upper " + upp)
#   print("num lower " + low)
#   print("num space " + spa)
#
#
#ext_analyzer("sys.argv[3]")