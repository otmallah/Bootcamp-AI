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


secret_num = 21

a = '''This is an interactive guessing game!
You have to enter a number between 1 and 30 to find out the secret number.
Type 'exit' to end the game.
Good luck!')'''

b = '''Congratulations, you've got it!
You won in 5 attempts!'''

print(a)
i = 0
print('What\'\s your guess between 1 and 99?')
while i < 5:
    str2 = input('=')
    if str2 == 'exit':
        print('Goodbye !!')
        exit(0)
    elif int(str2) < 15:
        print('zid mazal')
    elif int(str2) > 15:
        print('ba3adty')
    if int(str2) == secret_num:
        print(b)
        exit(0)
    i += 1
    