empty_list = []
users = ['foo' , 'bar' , 'baz']
mix = [True , 3.14 , 'lorem ipsum' , None ,[123 , 42]]

mix = [
    True,
    3.14,
    'lorem ipsum',
    None,
    [123 , 42]
]

# accés en lecture
#0 est l'index du premier element
print(users[0])

#len - 1 est l'index du dernier élément
i = len(users) -1
print(users[i])

#l'index depasse la taille de la liste
#print(users[100 + 42 - i])

# accés en écriture
users[0] = 'lorem'

#ajouter un nouvel élement
users.append('ipsum')

#ajouter un nouvel élement au debut ou milieu
users.insert(0 , 'sit')
users.insert(2 , 'dolores' )
print(users)

#retrait du dernier élément
last_user = users.pop()
print(last_user)
print(users)

#retrait par index
first_user = users.pop(0)
print(first_user)
print(users)

#suppresion par valeur
users.remove('bar')
print(users)

fruits = ['ananas ', 'banane' , 'cerise' ]
legumes = ['artichaud','brocoli', 'carotte' ]
ingredients = fruits + legumes
print(ingredients)

fruits += legumes
print(fruits)

numbers = ['g' , 'd' ,'a' , 'c' , 'b' , 'Z']
numbers = sorted(numbers)
print(numbers)