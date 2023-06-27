# scope = portée des variables

my_var1 = 123

def my_func1():
    print(my_var1)

my_var2 = 42

#la fonction voit les variables définies à l'exterieur au préalable ou à posteriori
my_func1()

def my_func2():
    my_var3 = 3.14

# il n'est pas possible d'accéder à un evariable definie à l'interieur d'une fonction
#que celle ci est exécutée ou non
#principe du verre teinté(comme avec une limousine)
# NameError : name 'my_var3 is not defined.
#print(my_var3)

my_var4 = 'foo'

def my_func3(my_var4):
    # le paramétre my_var4 masque la variable définie à l'exterieur de la fonction
    print(my_var4)

#cet appel affiche 'bar'
my_func3('bar')

my_var4 = 'foo'

def my_func4():
    # la variable my_var4 fait de l'ombre(shadowing) à la variable définie à l'exterieur de la fonction
    my_var4 = 'baz'
    print(my_var4)

my_func4()
# la variable my_var4 définie à l'exterieur de la fonction reste inchangée
print(my_var4)

def my_func5(my_var5):
    my_var5 = 'foo'
    print(my_var5)

my_var6 = 123
# les variables de type int, float, bool ou str sont passées par valeur
# c'est a dire que la fonction ne pourra accéder qu'a une copie de la variable originale  definie à l'exterieur
#c'est à dire que python copie la valeur dans une autre variable(qui est le paramétre de la fonction)
# les types de base comme int, float,bool sont passés par valeur
my_func5(my_var6)
print(my_var6)

def my_func6(my_var7: list):
    my_var7.append('foo')

my_var8 = [123, 45, 3.14]
# les variables de type list, dict, tuple ou objet sont passées par référence
# c'est a dire aue la fonction pourra accéder à la variable originale  definie à l'exterieur
my_func6(my_var8)
print(my_var8)


