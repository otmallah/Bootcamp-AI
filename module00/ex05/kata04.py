# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: otmallah <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/02 15:43:21 by otmallah          #+#    #+#              #
#    Updated: 2022/03/02 15:53:02 by otmallah         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import string

kata = (2, 4, 132.42222, 107520, 12345.67)

fir_str = "module_0" + str(kata[0])
sec_str = ", kata0" + str(kata[1]) + '.py'
thir_str = ": {:.2f}".format(kata[2])
for_str = ", {:.2e}".format(kata[3])
sic_str =". {:.2e}".format(kata[4]) 

string = fir_str + sec_str + thir_str + for_str + sic_str

print(string)
