# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: otmallah <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/03 19:07:41 by otmallah          #+#    #+#              #
#    Updated: 2022/03/03 19:07:42 by otmallah         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from cmath import inf
import string
import sys

cookbook = {
    "Sandwich" : {
        'Ingredients' : 'ham' ', bread' ', cheese' ', tomatoes',
        'meal' : 'lunch',
        'prep_time' : '10 min'
    },

    "cake" : {
        'Ingredients' : 'flour' ', sugar' ', eggs',
        'meal' : 'lunch',
        'prep_time' : '60 min'
    },

    "salad" : {
        'Ingredients' : 'avocado' ', arugila' ', tomatoes',
        'meal' : 'dessert',
        'prep_time' : '15 min'
    }
}
def print_reciep(var):
    k = 0
    for a , info in cookbook[var].items():
        if k == 0:
            print(a + ' :' , info)
            k = 1
        elif k == 1:
            print('to be eaten for ' , info)
            k = 2
        elif k == 2:
            print('take ', info + ' of cooking')

def delet_reciep(var):
    del cookbook[var]
    print('delet ' + var)

def add_reciep(name, ingredients, Meal, time):
    cookbook[name] = {'Ingredients' : ingredients , 'meal' : Meal, 'prep_time' : time}

def print_all():
    for a, info in cookbook.items():
        print('\n id = ' , a)
        for elem in info:
            print(elem + ':' , info[elem])

a = '''Please select  option by typing the corresponding number :
1: Add a recipe
2: Delete a recipe
3: Print a recipe
4: Print the cookbook
5: Quit'''
print(a)
string = input('= ')
i = 1
wrong = '''this option does not exist, please type the corresponding number.
to exit, enter 5'''
while 1:
    if (string == '5'):
        print('Cookbook closed!')
        exit()
    elif (string == '1'):
        a = input('please enter name of recipe : ')
        b = input('Ingredients  : ')
        c = input('meal  : ')
        d = input('prep_time  : ')
        add_reciep(a,b,c,d)
        print_reciep(a)
    elif (string == '2'):
        jomla = input("enter recipe : ")
        delet_reciep(jomla)
    elif string == '3':
        k = input('Please enter the recipe\'s name to get its details : ')
        print_reciep(k)
    elif string == '4':
         print_all()
    else:
        print(wrong)
    #print(a)
    string = input(' = ')