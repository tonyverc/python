import random
users = ['foo','bar','baz']

#boucle for classique
# cette boucle est la meme que celle de javascript 
#for (let i = 0, i< n; i++){}
for i in range(len(users)):
    print(i, users[i])

#boucle for classique avec un pas de 2 (step)
#seule cette boucle permet de sauter des éléments dans une liste
for i in range(0, len(users), 2):
    print(i, users[i])

#boucle for each
for user in users:
    print(user)

#boucle for each avec enumerate
#equivalent fonctionnel de la boucle for classique
#mais celle ci est préferée par les codeurs python
for i, user in enumerate(users):
    print(i, user)

# une boucle while
while True:
    r = random.randint(1, 100)
    print(r)

    if r == 100:
        break

r = random.randint(1, 100)
print(r)

#equivalant de la boucle while
while r != 100:
    r = random.randint(1, 100)
    print(r)

#str
text1 = 'foo bar baz foo foo bar baz foo'

for i, char in enumerate(text1):     #char= caractére  #i= index donc place dans la chaine de caractére
    print(i, char)

print(text1.find('bar'))      #retrouver l'index de bar dans la chaine de caractére
print(text1.find('Bar')) 
print(text1.find('foo') )
print(text1.find('foo', 1))   # retrouver un meme mot plus loin dans la chaine
position = text1.find('foo')
print(position)
print(text1.find('foo', position +1))

keyword = 'foo'
position = -1

while True:
    position = text1.find(keyword, position + 1)   # -1 et +1 s'annule donc la recherche commence à 0
    print(position)

    #if position != -1:
    #    count += 1
    #else: # position == -1
    #   break

    if position == -1:
        break
    #else:
      #count +=1

print(text1.count('foo'))  # trouver tout les mots dans la chaine



# code ASCII d'un caractére
print(ord('A'))
print(ord('a'))

#récupérer un caractére à partir de son code ASCII
print(chr(65))
print(chr(97))

text2 = 'lorem ipsum'

# afiiche le iéme caractére de la chaine
print(text2[1])

#affiche les caractére de l'index 1 inclus à l'index 7 exclus
# c'est à dire jusque 6 inclus
print(text2[1:7])

#affiche un caractére sur deux,de l'index 1 inclus à l'index 7 exclus
#c'est a dire jusque 6inclus
print(text2[1:7:2])

#affiche à rebours (-1) les caractéres de l'index 6 inclus à l'index 0 exclus
#c'est a dire jusque 1 inclus
print(text2[6:0:-1])

#syntaxe
#str[start:end:step]
#ATTENTION: end est exclue

text3 = 'foo bar baz'
text3_list = text3.split('bar') #séparer chaine de caractére
print(text3_list)
text3 = 'lorem'.join(text3_list) # remplace le mot voulu dans la chaine
print(text3)

#algotithmes récursives VS algorithmes itératifs

#suite de fibonacci
#index:  0 1 2 3 4 5 6 7  8  9 
# valeur:0 1 1 2 3 5 8 13 21 34 ...
#f(n) = f(n-1) + f(n-2)
#exemple :
#f(9) = f(8) + f(7)
#34   = 21   +  13

memo = { 
    0: 0,
    1: 1
}

def fibonacci(n):
    #si le résultat est déja dans le memo,
    #on renvoie le résultat
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        #on calcule le résultat
        result = fibonacci(n - 1) + fibonacci(n - 2)
        #on stock le résultat dans le mémo
        memo[n] = result
        return result
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(150))

