#import du module random(pour les nombres aléatoires)
import random

#arithmétique
a= 123 + 42
a= 123 - 42
a= 123 * 42
a= 123 / 42

#division entiére, integer division
a=123 // 42
print(a)

#modulo ou reste de la division (euclidienne)
a= 53
#s'il y a un reste,le nombre n'est pas divisible par deux,donc il n'est pas pair
print(a % 2)

a = 74


#puissance,exponentiation
#deux puissance trois
#equivalent de 2 * 2 * 2
a= 2 ** 3
print(a)

#opérateurs de comparaison
#operateur d'egalité
result = 123 == 42
print(result)

password ="abc"
user_input = "def"
print(password == user_input)

#(strictement )plus grand que
123 > 42  

#plus grand ou égal à 123 >= 42


#plus petit que
123 < 42

#plus petit ou égal à
123 <= 42

#différent de
123 != 42

#opérateurs composés
b = 0

#incrémentation
# b = b + 1
b += 1
b += 1
print(b)

#incrémentation
# b = b - 1
b -= 1
b -= 1
print(b)

#multiplication
c = 3
# c = c* 2
c *= 2
print(c)

#division
d = 10
# d = d / 3
d /= 3
print(d)

#division entiére
d = 10
# d = d // 3
d //= 3
print(d)

#opérateur d'inclusion
text1 = "lorem ipsum"

result = "e" in text1
print(result)
print("e"in text1)

list1 = ['lorem','ipsum']
print("e" in list1)
print("ipsum" in list1)

#comparaison avec des nombres aléatoires
e = random.randint(0 , 100)
f = random.randint(0 ,100)

print(f'{e = }')
print(f'{f = }')

result = e == f
print(result)

result = e < f
print(result)


#est une expression
# 1 + 1 -> 2
#(100 + 2) * 3 = 102 * 3 -> 306
#1 + 1 >(100 + 2) * 3 -> 2 > 306 -> False
# random.randint(0 , 100) -> 100

#pas une expression
# print(100) ->



