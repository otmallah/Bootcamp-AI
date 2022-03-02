# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: otmallah <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/02 15:11:12 by otmallah          #+#    #+#              #
#    Updated: 2022/03/02 15:11:12 by otmallah         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

kata['Python'] = 'Python was created by Guido van Rossum'
kata['Ruby'] = 'Ruby was created by Yukihiro Matsumoto'
kata['PHP'] = 'PHP was created by Rasmus Lerdorf'

for elem in kata.values():
    print(elem)