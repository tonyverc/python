# exo 6.14
# Créez une deuxième liste nommée `new_list` ne contenant que les nombres entiers de la liste
#
# ATTENTION : cet exercice nécessite l'utilisation d'une boucle `for`

my_list = [2.71, 42, 123, 2, 3.14, 1.61]

# réponse 6.14

import math

my_list = [2.71, 42, 123, 2, 3.14, 1.61]
new_list = []

for number in my_list:
    if number == math.floor(number):
       new_list.append(number)

print(new_list)








