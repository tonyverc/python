# exo 6.7
# Inversez la position des valeurs `bar` et `lorem` puis affichez le résultat
#
# ATTENTION : Dans l'énoncé, quand il est écrit Xème position, cela correspond à l'index X-1

my_list = ['foo', 'bar', 'baz', 'lorem', 'ipsum']

# réponse 6.7

index_bar = my_list.index('bar')
index_lorem = my_list.index('lorem')
my_list[index_bar], my_list[index_lorem] = my_list[index_lorem], my_list[index_bar]

print(my_list)